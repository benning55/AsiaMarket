<template>

    <div class="bg-white w-full px-4 sm:h-full lg:px-24 pb-16 mx-auto pt-5">
        <Loader v-if="isLoading"/>

        {{$t('paypal_debit_or_credit_card')}}
        <div class="flex-col py-4 w-full mx-auto" style="max-width: 400px">
            <div class="px-2 bg-green" ref="paypal"></div>
            <div id="paypal-button-container"></div>
        </div>

        <el-divider> {{$t('or')}}</el-divider>
        {{$t('bank_transfer')}}
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
                data: {}
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
        created() {

        },
        methods: {
            nameTranslate(text) {
                let list = text.split(')').join('(').split('(')
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
                                    this.$alert(this.nameTranslate('Payment success(ชำระเงินสำเร็จ)'), this.nameTranslate('Success(สำเร็จ)'), {
                                        confirmButtonText: this.nameTranslate('OK(ตกลง)'),
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
                    this.$alert(this.nameTranslate('Upload success(อัปโหลดสำเร็จ)'), this.nameTranslate('Upload Slip(อัปโหลดสหลักฐานการโอนเงิน)'), {
                        confirmButtonText: this.nameTranslate('OK(ตกลง)'),
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

        },
        mounted: function () {
            const script = document.createElement("script");
            script.src =
                "https://www.paypal.com/sdk/js?client-id=AVT3yQTUXd2oByh2YuOlVhGhoTLGsyb5-BYgzX53YG7Wc-nqBF60Ugmk8kZljHxj4EA1wLWrexXwd8lj&currency=EUR";
            script.addEventListener("load", this.setLoaded);
            document.body.appendChild(script);
        },
        watch: {
            order() {
                if (this.order != null) {
                    let address = this.order.address.split(',')
                    let city_code = address[address.length-1].split(' ')

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
                                admin_area_2: address[address.length-2],
                                admin_area_1: city_code[city_code.length -2],
                                postal_code: city_code[city_code.length -1],
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