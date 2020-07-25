<template>

    <div class="bg-white w-full px-4 sm:h-full lg:px-24 pb-16 mx-auto pt-5">
        <Loader v-if="isLoading"/>

        {{$t('paypal_debit_or_credit_card')}}
        <div class="flex-col py-4 w-full mx-auto" style="max-width: 400px">
            <div class="px-2 bg-green" ref="paypal"></div>
            <div id="paypal-button-container"></div>
        </div>

        <div @click="openKlarna" class="w-32 h-12 bg-orange mx-auto py-3 cursor-pointer">
            <p class="text-center">
                Open Klarna
            </p>
        </div>

        <div id="klarna-payments-container"></div>

        <el-divider> {{$t('or')}}</el-divider>
        {{$t('bank_transfer')}}


        <el-card class="box-card mt-3">
            <h1 class="text-center text-2xl my-4">{{$t('account_name')}} : Nat Muannamon</h1>
            <h1 class="text-center my-2">IBAN: DE10 5209 0000 0053 9340 05
                <el-tooltip class="item" effect="dark" :content="textTooltip" placement="top">
                    <i v-on:mouseleave="mouseleave" @click="copyIBAN('DE10520900000053934005')"
                       class="fas fa-copy text-key_column cursor-pointer pl-2"></i>
                </el-tooltip>
            </h1>
            <h1 class="text-center my-2">BIC: GENODE51KS1
                <el-tooltip class="item" effect="dark" :content="textTooltip" placement="top">
                    <i v-on:mouseleave="mouseleave" @click="copyIBAN('GENODE51KS1')"
                       class="fas fa-copy text-key_column cursor-pointer pl-2"></i>
                </el-tooltip>
            </h1>
            <h1 class="text-center mb-4">{{$t('bank_name')}} : Volksbank Kassel Göttingen</h1>
            <img class="mx-auto" style="width: 200px;display: block;"
                 src="../assets/png/Logo_Volksbank_Kassel_Göttingen_eG.png">
        </el-card>


        <div class="flex-col py-4 w-full mx-auto" style="max-width: 400px">
            <div class="col-12 upload-section">
                <div class="upload-btn-wrapper w-full">
                    <div class="">
                        <div class="image-cropper border-2 border-dashed border-black text-center">
                            <img
                                    v-if="imageData!=null"
                                    :src="profileImageURL"
                                    alt="avatar"
                                    class="profile-pic"
                            />
                            <p v-else class="center-y">{{$t('upload_your_slip_here')}}</p>
                        </div>
                    </div>
                    <input type="file" @change="previewImage" accept="image/*"/>
                </div>
            </div>
            <div class="mb-4">
                <div>
                    <label v-if="!validation.firstError('date')"
                           class="block text-sm mb-2">{{$t('transfer_date')}}</label>
                    <label v-else
                           class="block text-red text-sm mb-2">{{validation.firstError('date')}}</label>
                    <el-date-picker
                            v-model="date"
                            type="date"
                            placeholder="Pick a day"
                            format="dd MMMM yyyy"
                            value-format="yyyy-MM-dd"
                            :editable="false"
                            :picker-options="pickerOptions">
                    </el-date-picker>

                    <label v-if="!validation.firstError('time')"
                           class="block text-sm mb-2 mt-3">{{$t('transfer_time')}}</label>
                    <label v-else
                           class="block text-red text-sm mb-2 mt-3">{{validation.firstError('time')}}</label>
                    <el-time-picker
                            v-model="time"
                            placeholder="Arbitrary time"
                            format="HH:mm"
                            :editable="false"
                            value-format="HH:mm">
                    </el-time-picker>
                    <div @click="sendSlip" class="bg-green text-white text-center p-2 mt-8">{{$t('send')}}</div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
    import axios from 'axios'
    import {Validator} from "../main";
    import moment from 'moment'
    import Loader from "../components/Loader";


    export default {
        props: ["id", "order"],
        components: {
            Loader
        },
        data: function () {
            return {
                loaded: false,
                paidFor: false,
                profileImageURL: null,
                imageURL: null,
                imageData: null,
                last4digit: '',
                date: '',
                time: '',
                pickerOptions: {
                    disabledDate(time) {
                        return time.getTime() > Date.now();
                    },
                },
                isLoading: false,
                data: {},
                textTooltip: this.$t('click_to_copy'),
                klarnaResponse: null,
                tokenKlana: 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc0OWM5M2U2LTJkNWQtMzJmNC04ZTk1LWJhNWUwZDA1OTJiYSJ9.ewogICJzZXNzaW9uX2lkIiA6ICJkY2EzNTgxNS0yZWY5LTc4YzUtODg5Ny00NTU3Nzk2MmU1YjMiLAogICJiYXNlX3VybCIgOiAiaHR0cHM6Ly9rbGFybmEtcGF5bWVudHMtZXUua2xhcm5hLmNvbS9wYXltZW50cyIsCiAgImRlc2lnbiIgOiAia2xhcm5hIiwKICAibGFuZ3VhZ2UiIDogImVuIiwKICAicHVyY2hhc2VfY291bnRyeSIgOiAiREUiLAogICJ0cmFjZV9mbG93IiA6IGZhbHNlLAogICJlbnZpcm9ubWVudCIgOiAicHJvZHVjdGlvbiIsCiAgIm1lcmNoYW50X25hbWUiIDogIk5hdCBNdWFubmFtb24iLAogICJzZXNzaW9uX3R5cGUiIDogIlBBWU1FTlRTIiwKICAiY2xpZW50X2V2ZW50X2Jhc2VfdXJsIiA6ICJodHRwczovL2V1LmtsYXJuYWV2dC5jb20iLAogICJleHBlcmltZW50cyIgOiBbIF0KfQ.mIFjDICTUwlqu1mSgxed67qz9tNT7CXYTKLmDMTQ2rf8XSwoOOav19qS7Q0b1rHmOpmR3-zaN7qxB0HtfvPA359HpbzM3RcIKHpfFQRgkQFslSs0suK5v3ihKvcn2AyO8M1CNHgUWZuOn_fb00f6VlFzkN3hvK-4i0HOGcsN9Gvh9wJKdEOeYHtNuc1qtqUDqQLFQddq0ba1Q3wwbT6I_Cc9IKI5HPBd2DkGnWHsdVhu4a1V9vkDf6A8syB7Vj3WeJVtf_-BvGOze_JkNIU8cq1_OylzDeNnQ2J_q1Bca0YOSDrdd51O92Lk8AGu2NNkYe9D8uIpAendjU4voD2V7A'
            };
        },
        validators: {
            date(value) {
                return Validator.value(value)
                    .required("date");
            },
            time(value) {
                return Validator.value(value)
                    .required("time");
            },
        },
        // beforeCreate() {
        //     let data = {
        //         "purchase_country": "GB",
        //         "purchase_currency": "GBP",
        //         "locale": "en-GB",
        //         "order_amount": 50000,
        //         "order_tax_amount": 4545,
        //         "order_lines": [
        //             {
        //                 "type": "physical",
        //                 "reference": "19-402-USA",
        //                 "name": "Red T-Shirt",
        //                 "quantity": 5,
        //                 "quantity_unit": "pcs",
        //                 "unit_price": 10000,
        //                 "tax_rate": 1000,
        //                 "total_amount": 50000,
        //                 "total_discount_amount": 0,
        //                 "total_tax_amount": 4545
        //             }
        //         ],
        //         "merchant_urls": {
        //             "terms": "https://www.example.com/terms.html",
        //             "checkout": "https://www.example.com/checkout.html?order_id={checkout.order.id}",
        //             "confirmation": "https://www.example.com/confirmation.html?order_id={checkout.order.id}",
        //             "push": "https://www.example.com/api/push?order_id={checkout.order.id}"
        //         }
        //     }
        //     axios.post('http://localhost/api/utils/klarna/', data,
        //         {
        //             headers: {
        //                 // Authorization: `Basic UEsyMTE5N183Zjc0NTEyMzFhYjI6MUN0eUE2V0NoblVGdkM3aw==`,
        //                 Authorization: `Basic Szc2NTU5NV84YjY2MzM2OTE5N2E6VTdONUxiMlQyYks1UXRodg==`,
        //                 'Content-Type': 'application/json',
        //                 "cache-control": "no-cache",
        //                 "postman-token": "b6047eb4-877d-0f02-e5fb-1791e5708033"
        //             }
        //         })
        //         .then((res) => {
        //             this.klarnaResponse = res.data.client_token;
        //             console.log(this.klarnaResponse)
        //         })
        // },
        methods: {
            nameTranslate(text) {
                let list = text.split('|')
                if (list.length == 1) {
                    return text
                } else {
                    if (this.$i18n.locale == 'th') {
                        return list[1]
                    } else {
                        return list[0]
                    }
                }
            },
            previewImage(event) {
                this.imageData = event.target.files[0]
                this.profileImageURL = URL.createObjectURL(this.imageData)
            },
            copyIBAN(text) {
                let dummy = document.createElement("input");
                dummy.style.height = "1px"
                dummy.style.width = "1px"
                dummy.style.position = 'fixed'
                document.body.appendChild(dummy);
                dummy.value = text;
                dummy.select();
                document.execCommand("copy");
                this.textTooltip = this.$t('copied') + text;
            },
            mouseleave() {
                this.textTooltip = this.$t('click_to_copy')
            },
            setLoaded: function () {
                this.loaded = true;
                window.paypal
                    .Buttons({
                        style: {
                            layout: "vertical",
                            color: "gold",
                            shape: "rect",
                            label: "paypal",
                        },
                        createOrder: (data, actions) => {
                            return actions.order.create(this.data);
                        },
                        onApprove: async (data, actions) => {
                            const order = await actions.order.capture();
                            this.paidFor = true;
                            if (order.status == "COMPLETED") {
                                axios.put(`${this.$store.state.endpoints.host}/api/orders/order/`, {
                                    id: this.id,
                                    payment_type: "PayPal",
                                    payment_status: true
                                }, {
                                    headers: {
                                        Authorization: `JWT ${this.$store.state.jwt}`,
                                        'Content-Type': 'application/json'
                                    }
                                }).then(res => {
                                    this.$emit('updatePayment');
                                    this.$alert(this.nameTranslate('Payment success|ชำระเงินสำเร็จ'), this.nameTranslate('Success|สำเร็จ'), {
                                        confirmButtonText: this.nameTranslate('OK|ตกลง'),
                                    });
                                }).catch(e => {
                                    // this.$message.error('Oops, Something is Error. code ' + e.status + ', at cart');
                                    this.$alert("Can't save Data, But payment success", 'Error', {
                                        confirmButtonText: 'OK',
                                    });
                                })
                            }

                        },
                        onError: e => {
                            // this.$message.error('Oops, Something is Error. code ' + e.status + ', at paypal');
                            this.$alert(`Oops, Something is Error. code ${e.response.status}, at paypal`, 'Error', {
                                confirmButtonText: 'OK',
                            });
                        }
                    })
                    .render('#paypal-button-container');
            },
            sendSlip() {
                this.isLoading = true
                let formData = new FormData();
                formData.append('pic', this.imageData);
                formData.append('order', this.$route.params.id);
                formData.append('time_transfer', moment(this.date + ' ' + this.time).format());

                axios.post(`${this.$store.state.endpoints.host}/api/orders/payment-bill/`, formData, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    }
                }).then(() => {
                    this.isLoading = false
                    this.$emit('updatePayment');
                    this.$alert(this.nameTranslate('Upload success|อัปโหลดสำเร็จ'), this.nameTranslate('Upload Slip|อัปโหลดสหลักฐานการโอนเงิน'), {
                        confirmButtonText: this.nameTranslate('OK|ตกลง'),
                        callback: action => {
                            if (action == 'confirm') {

                            }
                        }
                    });
                }).catch(e => {
                    this.isLoading = false
                    this.$alert('Error : ' + e.response, 'Upload slip', {
                        confirmButtonText: 'Ok',
                        callback: action => {
                            if (action == 'confirm') {
                            }
                        }
                    });
                })

            },
            openKlarna: function () {
                // let data = {
                //     "purchase_country": "GB",
                //     "purchase_currency": "GBP",
                //     "locale": "en-GB",
                //     "order_amount": 50000,
                //     "order_tax_amount": 4545,
                //     "order_lines": [
                //         {
                //             "type": "physical",
                //             "reference": "19-402-USA",
                //             "name": "Red T-Shirt",
                //             "quantity": 5,
                //             "quantity_unit": "pcs",
                //             "unit_price": 10000,
                //             "tax_rate": 1000,
                //             "total_amount": 50000,
                //             "total_discount_amount": 0,
                //             "total_tax_amount": 4545
                //         }
                //     ],
                //     "merchant_urls": {
                //         "terms": "https://www.example.com/terms.html",
                //         "checkout": "https://www.example.com/checkout.html?order_id={checkout.order.id}",
                //         "confirmation": "https://www.example.com/confirmation.html?order_id={checkout.order.id}",
                //         "push": "https://www.example.com/api/push?order_id={checkout.order.id}"
                //     }
                // }
                // axios.post('http://localhost/api/utils/klarna/', data,
                //     {
                //         headers: {
                //             // Authorization: `Basic UEsyMTE5N183Zjc0NTEyMzFhYjI6MUN0eUE2V0NoblVGdkM3aw==`,
                //             Authorization: `Basic Szc2NTU5NV84YjY2MzM2OTE5N2E6VTdONUxiMlQyYks1UXRodg==`,
                //             'Content-Type': 'application/json',
                //             "cache-control": "no-cache",
                //             "postman-token": "b6047eb4-877d-0f02-e5fb-1791e5708033"
                //         }
                //     })
                //     .then((res) => {
                //         this.klarnaResponse = res;
                //         let a = res.data.client_token
                //         console.log(a)
                //
                //     })
            }

        },
        mounted: function () {
            const script = document.createElement("script");
            script.src =
                "https://www.paypal.com/sdk/js?client-id=AYPJL4TE_OsKKYRY-xSErDmNeeIYl-3lPd8LFgGyC2vWBH33nuq7qNgZOpm3tcNQrcVjTlR5xah1jK7w&currency=EUR";
            script.addEventListener("load", this.setLoaded);
            document.body.appendChild(script);

            // this.openKlarna()
            const scripts = document.createElement("script");
            scripts.src = "https://x.klarnacdn.net/kp/lib/v1/api.js"
            document.body.appendChild(scripts);


            // this.openKlarna()
            // const script3 = document.createElement("script");
            // scripts.src = "https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"
            // document.body.appendChild(script3);


            window.klarnaAsyncCallback = function () {
                function readCookie(name) {
                    let nameEQ = name + "=";
                    let ca = document.cookie.split(';');
                    for (let i = 0; i < ca.length; i++) {
                        let c = ca[i];
                        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
                        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
                    }
                    return null;
                }

                let csrftoken = readCookie('csrftoken');

                fetch(window.location.protocol + '//' + window.location.hostname + '/api/utils/klarna/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        "X-CSRFToken": csrftoken
                    },
                    body: JSON.stringify({
                        "locale": "en-DE",
                        "order_amount": 2500,
                        "order_lines": [
                            {
                                "name": "Eggooo",
                                "quantity": 1,
                                "total_amount": 2500,
                                "unit_price": 2500
                            }
                        ],
                        "purchase_country": "DE",
                        "purchase_currency": "EUR"
                    }),
                })
                    .then(response => response.json())
                    .then(json => {

                        try {
                            Klarna.Payments.init({
                                client_token: json.client_token
                            })
                            Klarna.Payments.load({
                                container: '#klarna-payments-container',
                                payment_method_category: 'pay_now'
                            }, function (res) {
                                console.debug(res);
                            })
                        } catch (e) {
                            console.log("error")
                        }

                    });
                // let a = 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc0OWM5M2U2LTJkNWQtMzJmNC04ZTk1LWJhNWUwZDA1OTJiYSJ9.ewogICJzZXNzaW9uX2lkIiA6ICJkY2EzNTgxNS0yZWY5LTc4YzUtODg5Ny00NTU3Nzk2MmU1YjMiLAogICJiYXNlX3VybCIgOiAiaHR0cHM6Ly9rbGFybmEtcGF5bWVudHMtZXUua2xhcm5hLmNvbS9wYXltZW50cyIsCiAgImRlc2lnbiIgOiAia2xhcm5hIiwKICAibGFuZ3VhZ2UiIDogImVuIiwKICAicHVyY2hhc2VfY291bnRyeSIgOiAiREUiLAogICJ0cmFjZV9mbG93IiA6IGZhbHNlLAogICJlbnZpcm9ubWVudCIgOiAicHJvZHVjdGlvbiIsCiAgIm1lcmNoYW50X25hbWUiIDogIk5hdCBNdWFubmFtb24iLAogICJzZXNzaW9uX3R5cGUiIDogIlBBWU1FTlRTIiwKICAiY2xpZW50X2V2ZW50X2Jhc2VfdXJsIiA6ICJodHRwczovL2V1LmtsYXJuYWV2dC5jb20iLAogICJleHBlcmltZW50cyIgOiBbIF0KfQ.mIFjDICTUwlqu1mSgxed67qz9tNT7CXYTKLmDMTQ2rf8XSwoOOav19qS7Q0b1rHmOpmR3-zaN7qxB0HtfvPA359HpbzM3RcIKHpfFQRgkQFslSs0suK5v3ihKvcn2AyO8M1CNHgUWZuOn_fb00f6VlFzkN3hvK-4i0HOGcsN9Gvh9wJKdEOeYHtNuc1qtqUDqQLFQddq0ba1Q3wwbT6I_Cc9IKI5HPBd2DkGnWHsdVhu4a1V9vkDf6A8syB7Vj3WeJVtf_-BvGOze_JkNIU8cq1_OylzDeNnQ2J_q1Bca0YOSDrdd51O92Lk8AGu2NNkYe9D8uIpAendjU4voD2V7A'

            };


        },
        watch: {
            order() {
                if (this.order != null) {
                    let address = this.order.address.split(',')
                    let city_code = address[address.length - 1].split(' ')

                    this.data = {
                        application_context: {
                            shipping_preference: 'NO_SHIPPING',
                            locale: "en-US"
                        },
                        purchase_units: [
                            {
                                amount: {
                                    currency_code: "EUR",
                                    value: this.order.price
                                },
                            }
                        ],
                        payer: {
                            name: {
                                given_name: this.$store.state.authUser.user.first_name,
                                surname: this.$store.state.authUser.user.last_name
                            },
                            address: {
                                address_line_1: "-",
                                address_line_2: "-",
                                admin_area_2: address[address.length - 2],
                                admin_area_1: city_code[city_code.length - 2],
                                postal_code: city_code[city_code.length - 1],
                                country_code: "DE"
                            },
                            email_address: this.$store.state.authUser.user.email,
                            phone: {
                                phone_type: "MOBILE",
                                phone_number: {
                                    national_number: this.$store.state.authUser.profile.tel
                                }
                            }
                        }
                    }
                }
            }
        },
        loadKlara() {

        }
    }
</script>

<style scoped>
    .el-date-editor.el-input, .el-date-editor.el-input__inner {
        width: 100%;
    }

    .uneditable- input:focus {
        border-color: #36622b;
        box-shadow: none;
        -webkit-box-shadow: none;
        outline: none;
    }

    .image-upload {
        text-align: center;
    }

    .upload-section {
        padding-top: 1em;
        color: #1f1f1f;
    }

    .image-upload img {
        width: 300px;
    }

    .btn img {
        width: 2em;
    }

    .arrow-btn h5 {
        margin: 0;
    }

    .arrow-btn h5,
    img {
        display: inline-block;
    }

    button {
        background-color: #729d39;
        border: none;
    }

    button:hover {
        background-color: #36622b;
    }

    .free-space :nth-child(1) {
        width: 100%;
        margin-left: -72px;
    }

    /* add by leo */

    .upload-btn-wrapper {
        position: relative;
        overflow: hidden;
        display: inline-block;
    }

    .upload-btn-wrapper input[type="file"] {
        font-size: 30px;
        position: absolute;
        left: 0;
        top: 0;
        opacity: 0;
        width: 100%;
        height: 100%;
    }

    .image-cropper {
        width: 100%;
        height: 290px;
        position: relative;
        overflow: hidden;
        margin: auto;
    }

    .profile-pic {
        object-fit: contain;
        height: 100%;
        width: 99.8%;
    }


    @media screen and (max-width: 768px) {
        .free-space {
            display: none;
        }

        .next {
            float: right;
        }
    }
</style>