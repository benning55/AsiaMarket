<template>
    <div class="sm:mx-0 md:mx-24 lg:mx-0 xl:mx-0">
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <div class="bg-white w-full border-green-top px-4 sm:h-full lg:px-24 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
            <div class="flex-col py-4 w-full mx-auto" style="max-width: 400px">
                <div class="px-2 bg-green" ref="paypal"></div>
                <div style="z-index: 1" id="paypal-button-container"></div>
                <div>or</div>

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
                                <h1 v-else class="center-y">No image selected</h1>
                            </div>
                        </div>
                        <input type="file" @change="previewImage" accept="image/*"/>
                    </div>
                </div>
                <div class="mb-4">
                    <div>
                        <label v-if="!validation.firstError('last4digit')"
                               class="block text-sm mb-2"
                               for="last4digit">Last 4 digit in your bank account</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="last4digit">Please input Username</label>
                        <el-input id="last4digit"
                                  type="number"
                                  placeholder="Please input"
                                  v-model="last4digit">
                        </el-input>
                    </div>

                    <div>
                        <label v-if="!validation.firstError('last4digit')"
                               class="block text-sm mb-2"
                               for="last4digit">Transfer Time (approx).</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="last4digit">Please input Username</label>
                        <el-time-picker
                                v-model="time"
                                format="HH:mm"
                                placeholder="input time"
                                :readonly="true">
                        </el-time-picker>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    // import axios from 'axios'
    import {Validator} from "../main";


    export default {
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
                time: Date.now()
            };
        },
        validators: {
            last4digit(value) {
                return Validator.value(value)
                    .required("last4digit");
            },
            // password(value) {
            //     return Validator.value(value)
            //         .required("password")
            //     // .minLength(6, "รหัสผ่านต้องมีมากกว่า 6 ตัวขึ้นไป");
            // }
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
                                            value: "15.00"
                                        },
                                    }
                                ],
                                payer: {
                                    name: {
                                        given_name: "PayPal",
                                        surname: "Customer"
                                    },
                                    address: {
                                        address_line_1: "123 ABC Street",
                                        address_line_2: "Apt 2",
                                        admin_area_2: "San Jose",
                                        admin_area_1: "CA",
                                        postal_code: "95121",
                                        country_code: "US"
                                    },
                                    email_address: "customer@domain.com",
                                    phone: {
                                        phone_type: "MOBILE",
                                        phone_number: {
                                            national_number: "14082508100"
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
                        },
                        onError: err => {
                            console.log(err);
                        }
                    })
                    .render('#paypal-button-container');
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