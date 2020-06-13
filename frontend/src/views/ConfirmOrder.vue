<template>
    <div class="sm:mx-0 md:mx-24 lg:mx-0 xl:mx-0">
        <Loader v-if="isLoading"/>
        <NavbarSpace/>
        <h1 class="mt-10 py-1 text-xl font-l">{{$t('product')}}</h1>

        <!--        show this when no item in cart-->
        <div v-if="$store.state.inCart.cart_detail.length == 0"
             class="bg-white w-full px-1 pb-16 mx-auto h-64 relative">
            <div class="center-y w-full">
                <h1 class="text-2xl text-center">{{$t('no_item_in_cart')}}</h1>
                <h1 @click="goHome" class="text-center text-orange cursor-pointer">{{$t('go_back_to_homepage')}}</h1>
            </div>
        </div>

        <!--        show when have item in cart-->
        <div v-else>
            <div class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 pb-16 mx-auto ">
                <table id="orderTable" class="table-auto w-full">
                    <thead class="border-bottom">
                    <tr class="">
                        <th class="px-2 py-2 w-2/12 sm:1/12"></th>
                        <th class="px-2 py-2 w-3/12 text-left" style="font-weight: normal">{{$t('product_name')}}</th>
                        <th class="p-0 sm:p-2 w-1/12" style="font-weight: normal">{{$t('product_price')}}</th>
                        <th class="p-0 sm:p-2 w-1/12 hidden sm:table-cell" style="font-weight: normal">
                            {{$t('product_quantity')}}
                        </th>
                        <th class="p-0 sm:p-2 w-1/12 table-cell sm:hidden" style="font-weight: normal">
                            {{$t('product_q')}}
                        </th>
                        <th class="p-0 sm:p-2 w-1/12" style="font-weight: normal">{{$t('total')}}</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="item in $store.state.inCart.cart_detail" :key="item.id" class="border-bottom">
                        <td class="px-2 py-2">

                            <img class="w-full mx-auto" style="max-width: 120px;height: 120px; object-fit: contain"
                                 :src="$store.state.endpoints.host + item.product.pic1"
                                 alt="">
                        </td>
                        <td class="px-2 py-2">{{nameTranslate(item.product.title)}}</td>
                        <td class="px-2 py-2 text-center text-green">{{item.product.price}}</td>
                        <td class="px-2 py-2 text-center">{{item.quantity}}</td>
                        <td class="px-2 py-2 text-center text-green">{{item.price}}</td>
                    </tr>
                    </tbody>
                </table>
                <div class="px-5 md:px-10 font-l mt-5 text-xl">
                    <div class="flex justify-between">
                        <h1 class="">{{$t('subTotal')}}</h1>
                        <h1 class="text-green">{{subTotal}} €</h1>
                    </div>

                    <div class="flex justify-between">
                        <h1 class="">{{$t('coupon_code')}}</h1>
                        <h1 v-if="this.$store.state.inCart.code == null">{{$t('no_code')}}</h1>
                        <h1 v-else>{{getCode.name}}</h1>
                    </div>

                    <div class="flex justify-between">
                        <h1 class="">{{$t('after_reduce_price')}}</h1>
                        <h1 class="text-green">{{totalWithCode}} €</h1>
                    </div>

                    <div class="flex justify-between">
                        <h1 class="">{{$t('shipping')}}</h1>
                        <h1 class="">{{shipping}} €</h1>
                    </div>


                    <div class="flex justify-between">
                        <h1 class="">{{$t('total')}}</h1>
                        <h1 class="text-green">{{totalWithShipping}} €</h1>
                    </div>
                </div>
            </div>

            <div class="flex justify-between px-1 sm:px-0">
                <h1 class="mt-5 py-1 text-xl font-l">{{$t('shipping_information')}}</h1>
                <h1 @click="showModal" class="mt-5 py-1 text-sm font-l self-end text-gray cursor-pointer">
                    {{$t('change')}}</h1>
            </div>

            <div class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 mx-auto py-5">
                <div v-if="!chooseNewAddress" class="px-5 md:px-10 font-l text-lg">
                    <div class="flex justify-between">
                        <h1 class="">{{$t('recipient')}}</h1>
                        <h1 class="text-right">
                            {{this.$store.state.userAddress[$store.state.indexUserAddress].recipient}}</h1>
                    </div>
                    <div class="flex justify-between">
                        <h1>{{$t('address')}}</h1>
                        <h1 class="text-right">
                            {{this.$store.state.userAddress[$store.state.indexUserAddress].address}},
                            {{this.$store.state.userAddress[$store.state.indexUserAddress].city}},
                            {{this.$store.state.userAddress[$store.state.indexUserAddress].state}}
                            {{this.$store.state.userAddress[$store.state.indexUserAddress].post_code}}
                        </h1>
                    </div>
                </div>

                <div v-else class="px-5 md:px-10 font-l text-lg">
                    <div class="flex justify-between">
                        <h1 class="">{{$t('recipient')}}</h1>
                        <h1 class="text-right">
                            {{newAddress.recipient}}</h1>
                    </div>
                    <div class="flex justify-between">
                        <h1>{{$t('address')}}</h1>
                        <h1 class="text-right">
                            {{newAddress.house_number}},
                            {{newAddress.street}},
                            {{newAddress.city}}
                            {{newAddress.post_code}}
                        </h1>
                    </div>
                </div>

                <div class="mt-5">
                    <div @click="toggleAddress = !toggleAddress"
                         :class="{'bg-red':toggleAddress,'bg-green':!toggleAddress}"
                         class="mx-auto lg:mr-0 w-64 text-white text-center py-2 px-2 focus:outline-none cursor-pointer">
                        <a v-if="!toggleAddress">New address</a>
                        <a v-else>{{$t('cancel')}}</a>
                    </div>
                </div>
                <transition name="fade">
                    <TypeAddress v-if="toggleAddress" :chooseNewAddress="chooseNewAddress" :dataAddress="newAddress"
                                 @updateAddress="insertAddress"/>
                </transition>
            </div>

            <div class="flex justify-between pt-10">
                <button class="w-32 text-black_p py-2 focus:outline-none flex justify-start"
                        type="button">
                    <p @click="$router.go(-1)" class="inline-flex ml-0">
                        <i class="material-icons">keyboard_arrow_left</i><span>{{$t('previous')}}</span>
                    </p>
                </button>
                <div @click="goPayment"
                     :class="{'opacity-50':toggleAddress,'cursor-not-allowed':toggleAddress}"
                     class="mr-2 lg:mr-0 w-64 bg-green text-white text-center py-2 px-2 focus:outline-none cursor-pointer">
                    {{$t('confirm_order_and_go_payment')}}
                </div>
            </div>
        </div>

        <el-dialog :title="nameTranslate(titleModal())" :visible.sync="addressDialog">
            <section class="modal-body" id="modalDescription" style="max-height: 500px;height: 50%">
                <div class="overflow-auto" style="max-height: 500px">
                    <div v-for="(address,index) in $store.state.userAddress" :key="address.id">
                        <div @click="swapIndex(index)" class="round px-2 flex cursor-pointer"
                             :class="{ 'select': $store.state.indexUserAddress == index && chooseNewAddress == false }">
                            <div class="w-6/12 text-left text-black px-1 py-2 h-full text-center">
                                {{address.recipient}}
                            </div>
                            <div class="w-6/12 text-left text-black px-1 py-2 h-full">
                                {{address.address}} {{address.city}} {{address.state}} {{address.post_code}}
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </el-dialog>

        <el-dialog :title="nameTranslate(titleModal())" :visible.sync="confirmDialog">
            <section>
                <!--                        show when complete-->
                <div v-if="isOrderComplete" class="h-full flex flex-wrap">
                    <div class="w-full text-center text-green" style="font-size: 6.2rem;padding-bottom: 26px">
                        <i class="far fa-check-circle"></i></div>
                    <p class="pb-5">{{$t('you_order_complete')}}</p>
                    <span slot="footer" class="dialog-footer flex justify-between w-full">
                        <el-button @click="goHome">{{$t('back_to_homepage')}}</el-button>
                        <el-button type="primary" @click="goEachOrder">{{$t('go_payment')}}</el-button>
                    </span>
                </div>

                <!--                        show before select-->
                <div v-else class="flex flex-wrap content-between">
                    <p class="mb-12">{{$t('are_you_sure_to_confirm')}}</p>
                    <span slot="footer" class="dialog-footer flex justify-between w-full">
                        <el-button @click="confirmDialog = false">{{$t('cancel')}}</el-button>
                        <el-button type="primary" @click="confirmOrder">{{$t('confirm')}}</el-button>
                    </span>
                    <!--                        <div class="flex justify-between w-full">-->
                    <!--                            <div @click="$emit('close')" class="bg-red py-2  px-4 text-white cursor-pointer">-->
                    <!--                                {{$t('cancel')}}-->
                    <!--                            </div>-->
                    <!--                            <div @click="confirmOrder" class="bg-green py-2 px-4 text-white cursor-pointer">-->
                    <!--                                {{$t('confirm')}}-->
                    <!--                            </div>-->
                    <!--                        </div>-->
                </div>
            </section>
        </el-dialog>

    </div>
</template>

<script>
    import axios from "axios";
    // import Modal from "../components/Modal";
    import Loader from "../components/Loader";
    import NavbarSpace from "../components/NavbarSpace";
    import TypeAddress from "../components/TypeAddress";

    export default {
        components: {
            // Modal,
            Loader,
            NavbarSpace,
            TypeAddress
        },
        data() {
            return {
                isModalVisible: false,
                isConfirmModalVisible: false,
                typeModal: '',
                isPass: false,
                isLoading: false,
                addressDialog: false,
                confirmDialog: false,
                // centerDialogVisible: false,
                chooseNewAddress: false,
                toggleAddress: false,
                newAddress: {
                    recipient: '',
                    house_number: '',
                    street: '',
                    city: '',
                    post_code: ''
                },
                isOrderComplete: false
            }
        },
        created() {
            this.loadAddress()
            window.scrollTo(0, 0);
        },
        methods: {
            // nameTranslate(text) {
            //     let list = text.split('|')
            //     if (list.length == 1) {
            //         return text
            //     } else {
            //         if (this.$i18n.locale == 'th') {
            //             return list[1]
            //         } else {
            //             return list[0]
            //         }
            //     }
            // },
            loadAddress() {
                this.isLoading = true
                axios.get(this.$store.state.endpoints.addressUrL, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    }
                }).then(
                    res => {
                        this.$store.commit("setUserAddress", res.data.address);
                        this.isLoading = false
                    }
                ).catch(e => {
                    this.isLoading = false
                    this.$message.error(this.$t('error_Oops_') + e.response.status + ', add load address');
                })
            },
            swapIndex(index) {
                this.$store.commit("setIndexUserAddress", index);
                this.chooseNewAddress = false
                this.addressDialog = false
                this.toggleAddress = false
            },
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
            titleModal() {
                if (this.typeModal == 'address') {
                    return 'Select Address|โปรดเลือกที่อยู่'
                } else {
                    return 'Confirm Order|ยืนยันการสั่งซื้อ'
                }
            },
            goHome() {
                this.$router.push({
                    name: 'HomePage'
                })
            },
            showModal() {
                $(".el-dialog").css({"max-width": "500px", "height": "initial"});
                this.typeModal = 'address'
                this.addressDialog = true
            },
            insertAddress(recipient, address, city, state, post_code, checked) {
                this.newAddress.recipient = recipient
                this.newAddress.house_number = address
                this.newAddress.street = city
                this.newAddress.city = state
                this.newAddress.post_code = post_code
                console.log(checked)
                if (checked) {
                    if (checked) {
                        axios.post(this.$store.state.endpoints.host + '/api/accounts/user/address/', {
                            recipient: recipient,
                            address: address,
                            city: city,
                            state: state,
                            post_code: post_code
                        }, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(() => {
                            this.$store.state.userAddress.unshift({
                                "recipient": recipient,
                                "city": city,
                                "address": address,
                                "post_code": post_code,
                                "state": state
                            })
                            this.$store.commit("setIndexUserAddress", 0)
                            this.isLoading = false
                            this.chooseNewAddress = false
                        }).catch(e => {
                            this.isLoading = false
                            this.$message.error(this.$t('error_Oops_') + e.response.status + ', at add address');
                        })
                    }
                } else {
                    this.chooseNewAddress = true
                }
                this.toggleAddress = false
            },
            chooseExist() {
                this.chooseNewAddress = false
            },
            goPayment() {
                if (!this.toggleAddress) {
                    $(".el-dialog").css({"max-width": "350px"});
                    this.typeModal = 'check_confirm'
                    // this.isModalVisible = true
                    this.confirmDialog = true
                }
            },
            confirmOrder() {
                let address = ''
                if (this.chooseNewAddress) {
                    address = this.newAddress.recipient + " " +
                        this.newAddress.house_number + "," +
                        this.newAddress.street + "," +
                        this.newAddress.city + " " +
                        this.newAddress.post_code
                } else {
                    address = this.$store.state.userAddress[this.$store.state.indexUserAddress].recipient + ' ' + this.$store.state.userAddress[this.$store.state.indexUserAddress].address + ', ' + this.$store.state.userAddress[this.$store.state.indexUserAddress].city + ', ' + this.$store.state.userAddress[this.$store.state.indexUserAddress].state + ' ' + this.$store.state.userAddress[this.$store.state.indexUserAddress].post_code
                }
                axios.post(`${this.$store.state.endpoints.host}/api/orders/order/`, {
                    address: address,
                    total_price: this.subTotal,
                    payment_type: "",
                    payment_status: false,
                    shipping_fee: this.shipping,
                    price: this.totalWithShipping

                }, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    }
                }).then(res => {
                    this.isOrderComplete = true
                    this.id = res.data.data.id
                    this.$store.commit("setIncart", {
                        cart_detail: []
                    });
                    // $(".el-dialog").css({"max-width": "350px", "height": "300px"});
                }).catch(e => {
                    this.$message.error(this.$t('error_Oops_') + e.response.status + ', at confirm order');
                })
            },
            goEachOrder() {
                this.$router.push({
                    name: 'ViewEachOrder',
                    params: {id: this.id}
                })
            },
        },
        computed: {
            checkPass() {
                let p = []
                this.$store.state.inCart.cart_detail.reduce(function (accumulate, data) {
                    if (data.overStatus == true || data.product.quantity == 0) {
                        return p.push('4')
                    }
                }, 0);
                return p
            },

            subTotal() {
                let sum = this.$store.state.inCart.cart_detail.reduce(function (accumulate, data) {
                    if (data.overStatus == true || data.product.quantity == 0) {
                        return accumulate + 0;
                    } else {
                        return accumulate + Number(data.price);
                    }
                }, 0);
                return (sum).toFixed(2);
            },
            reduceValue() {
                if (this.$store.state.inCart.code == null) {
                    return "0.00"
                } else {
                    console.log(Number((this.subTotal / 100) * this.getCode.percent).toFixed(2))
                    return Number((this.subTotal / 100) * this.getCode.percent).toFixed(2)
                }

            },
            shipping() {
                if (this.subTotal == 0) {
                    return 0
                } else {
                    return this.$store.state.shippingFee
                }
                return 0
            },
            totalWithCode() {
                // return Number(this.subTotal) + Number(this.shipping)
                if (this.$store.state.inCart.code == null) {
                    return Number(this.subTotal).toFixed(2)
                } else {
                    return (Number(this.subTotal) - this.reduceValue).toFixed(2)
                }
            },
            getCode() {
                if (this.$store.state.inCart.code == null) {
                    return {
                        name: 'No Code',
                        percent: 0
                    }
                } else {
                    return this.$store.state.inCart.code[0]
                }
            },
            totalWithShipping() {
                return Number(Number(this.totalWithCode) + Number(this.shipping)).toFixed(2)
            }
        }
    }
</script>

<style>
    .el-dialog {
        width: 95% !important;
        top: 30%;
        -ms-transform: translate(0%, -50%);
        transform: translate(0%, -50%);
    }

    .fade-enter-active {
        transition: opacity .5s;
    }

    .fade-leave-active {
        transition: opacity .0s;
    }

    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
    {
        opacity: 0;
    }

    .select {
        background-color: rgba(97, 159, 33, .3);
    }

</style>