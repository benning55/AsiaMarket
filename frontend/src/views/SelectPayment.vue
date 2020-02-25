<template>

    <div class="bg-white w-full px-4 sm:h-full lg:px-24 pb-16 mx-auto pt-5">
        PayPal, Debit or Credit Card
        <div class="flex-col py-4 w-full mx-auto" style="max-width: 400px">
            <div class="px-2 bg-green" ref="paypal"></div>
            <div id="paypal-button-container"></div>
        </div>
        <hr class="bg-lightGray text-white mb-5">
        Bank Transfer
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
                            <h1 v-else class="center-y">Upload your slip here</h1>
                        </div>
                    </div>
                    <input type="file" @change="previewImage" accept="image/*"/>
                </div>
            </div>
            <div class="mb-4">
                <div>
                    <label v-if="!validation.firstError('date')"
                           class="block text-sm mb-2">Transfer Time (approx).</label>
                    <label v-else
                           class="block text-red text-sm mb-2">Please input Username</label>
                    <el-date-picker
                            v-model="date"
                            type="date"
                            placeholder="Pick a day"
                            format="dd MMMM yyyy"
                            value-format="yyyy-MM-dd"
                            :picker-options="pickerOptions">
                    </el-date-picker>

                    <label v-if="!validation.firstError('time')"
                           class="block text-sm mb-2 mt-3">Transfer Date</label>
                    <label v-else
                           class="block text-red text-sm mb-2 mt-3">Please input Username</label>
                    <el-time-picker
                            v-model="time"
                            placeholder="Arbitrary time"
                            format="HH:mm"
                            value-format="HH:mm">
                    </el-time-picker>
                    <div @click="sendSlip" class="bg-green text-white text-center p-2 mt-8">Send</div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import axios from 'axios'
    import {Validator} from "../main";
    import moment from 'moment'


    export default {
        props: ["id", "order"],
        data: function () {
            return {
                loaded: false,
                paidFor: false,
                product: {
                    price: 7.77,
                    description: "leg lamp from that one movie",
                    img: "./assets/lamp.jpg"
                },
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
                }

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
        methods: {
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
                            label: "paypal"
                        },
                        createOrder: (data, actions) => {
                            return actions.order.create({
                                application_context: {
                                    shipping_preference: 'NO_SHIPPING',
                                    locale: "en-US"
                                },
                                purchase_units: [
                                    {
                                        amount: {
                                            currency_code: "EUR",
                                            value: this.order.total_price
                                        },
                                    }
                                ],
                                payer: {
                                    name: {
                                        given_name: this.$store.state.authUser.user.first_name,
                                        surname: this.$store.state.authUser.user.last_name
                                    },
                                    address: {
                                        address_line_1: "123 ABC Street",
                                        address_line_2: "Apt 2",
                                        admin_area_2: "San Jose",
                                        admin_area_1: "CA",
                                        postal_code: "95121",
                                        country_code: "US"
                                    },
                                    email_address: this.$store.state.authUser.user.email,
                                    phone: {
                                        phone_type: "MOBILE",
                                        phone_number: {
                                            national_number: this.$store.state.authUser.profile.tel
                                        }
                                    }
                                }
                            });
                        },
                        onApprove: async (data, actions) => {
                            const order = await actions.order.capture();
                            this.data;
                            this.paidFor = true;
                            console.log(order);
                            if (order.status == "COMPLETED") {
                                console.log('complete')
                                axios.put(`http://${window.location.hostname}:8000/api/orders/order/`, {
                                    id: this.id,
                                    payment_type: "PayPal",
                                    payment_status: true
                                }, {
                                    headers: {
                                        Authorization: `JWT ${this.$store.state.jwt}`,
                                        'Content-Type': 'application/json'
                                    }
                                }).then(res => {
                                    console.log(res)
                                }).catch()
                            }

                        },
                        onError: err => {
                            console.log(err);
                        }
                    })
                    .render('#paypal-button-container');
            },
            sendSlip() {
                let formData = new FormData();
                formData.append('pic', this.imageData);
                formData.append('order', this.$route.params.id);
                formData.append('time_transfer', moment(this.date + ' ' + this.time).format());

                axios.post(`http://${window.location.hostname}:8000/api/orders/payment-bill/`, formData, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    }
                }).then(() => {
                    this.$alert('Upload Complete', 'Upload slip', {
                        confirmButtonText: 'Ok',
                        callback: action => {
                            if (action == 'confirm') {
                                // this.$router.push({
                                //     name: 'login'
                                // })
                            }
                        }
                    });
                }).catch(e => {
                    this.$alert('Error : '+e.response, 'Upload slip', {
                        confirmButtonText: 'Ok',
                        callback: action => {
                            if (action == 'confirm') {
                                // this.$router.push({
                                //     name: 'login'
                                // })
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