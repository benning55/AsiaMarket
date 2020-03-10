<template>
    <div class="sm:mx-0 md:mx-24 lg:mx-0 xl:mx-0">
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <div v-if="$store.state.isAuthenticated" class="px-3 pt-4 md:px-0">
            <a href="#payment">
                <el-alert v-if="!order.payment_status && !order.receipt"
                          type="warning"
                          show-icon
                          :closable="false">
                    <h1 class="text-lg">Not Paid</h1>
                </el-alert>
                <el-alert v-if="!order.payment_status && order.receipt"
                          type="warning"
                          show-icon
                          :closable="false">
                    <h1 class="text-lg">Sent Slip. Please wait checked from Admin</h1>
                </el-alert>
            </a>

        </div>

        <h1 v-if="$store.state.isAuthenticated" class="py-1 text-xl font-l">Product</h1>

        <div v-if="!$store.state.isAuthenticated" class="bg-white w-full px-1 h-64 lg:px-10 xl:px-24 pb-10 mx-auto relative mt-10">
            <NoLoginText/>
        </div>

        <!--        show when have item in cart-->
        <div v-else>
            <div class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 pb-10 mx-auto ">
                <table id="orderTable" class="table-auto w-full">
                    <thead class="border-bottom">
                    <tr class="">
                        <th class="px-2 py-2 w-2/12 sm:1/12"></th>
                        <th class="px-2 py-2 w-3/12 text-left" style="font-weight: normal">Name</th>
                        <th class="p-0 sm:p-2 w-1/12" style="font-weight: normal">Price</th>
                        <th class="p-0 sm:p-2 w-1/12 hidden sm:table-cell" style="font-weight: normal">Quantity</th>
                        <th class="p-0 sm:p-2 w-1/12 table-cell sm:hidden" style="font-weight: normal">(Q)</th>
                        <th class="p-0 sm:p-2 w-1/12" style="font-weight: normal">Total</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="item in orderDetail" :key="item.id" class="border-bottom">
                        <td class="px-2 py-2">
                            <img class="w-full mx-auto" style="max-width: 120px;height: 120px; object-fit: contain"
                                 :src="$store.state.endpoints.host + item.product.pic1"
                                 alt="">
                        </td>
                        <td class="px-2 py-2">{{item.product.title}}</td>
                        <td class="px-2 py-2 text-center text-green">{{item.product.price}}</td>
                        <td class="px-2 py-2 text-center">{{item.quantity}}</td>
                        <td class="px-2 py-2 text-center text-green">{{(item.product.price*item.quantity).toFixed(2)}}</td>
                    </tr>
                    </tbody>
                </table>
                <div class="px-5 md:px-10 font-l mt-5 text-xl">
                    <div class="flex justify-between">
                        <h1 class="">SubTotal</h1>
                        <h1 class="text-green">{{order.total_price}} €</h1>
                    </div>
                    <div class="flex justify-between">



                        <h1 class="">Shipping</h1>
                        <h1 class="">{{order.shipping_fee}} €</h1>
                    </div>
                    <div class="flex justify-between">
                        <h1 class="">Coupon Code</h1>
                        <h1 v-if="order.code != null" class="">{{order.code}}</h1>
                        <h1 v-else>No Code</h1>
                    </div>
                    <div class="flex justify-between">
                        <h1 class="">Total</h1>
                        <h1 class="text-green">{{order.price}} €</h1>
                    </div>
                </div>
            </div>

            <div class="flex justify-between px-1 sm:px-0">
                <h1 class="mt-5 py-1 text-xl font-l">Shipping Information</h1>
            </div>
            <div class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 mx-auto py-5">
                <div class="px-5 md:px-10 font-l text-lg">
                    <div class="flex justify-between">
                        <h1 class="">Recipient</h1>
                        <h1 class="text-right">
                            {{order.address}}
                        </h1>
                    </div>
                </div>
            </div>

            <div id="payment" class="flex justify-between px-1 sm:px-0">
                <h1 class="mt-5 py-1 text-xl font-l">Payment</h1>
            </div>
            <SelectPayment v-if="!order.payment_status && !order.receipt" :id="$route.params.id" :order="order"/>
            <div v-else-if="!order.payment_status && order.receipt" class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 mx-auto py-5">
                <div class="px-5 md:px-10 font-l text-lg">
                    Sent Slip. Please wait checked from Admin
                </div>
            </div>
            <div v-else class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 mx-auto py-5">
                <div class="px-5 md:px-10 font-l text-lg">
                    Payment Success
                </div>
            </div>


            <div class="flex justify-between pt-10">
                <button class="w-32 text-black_p py-2 focus:outline-none flex justify-start"
                        type="button">
                    <p class="inline-flex ml-0">
                        <i class="material-icons">keyboard_arrow_left</i><span>Previous</span>
                    </p>
                </button>
            </div>
            {{order}}
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    // import {Validator} from "../main";
    // import moment from 'moment'
    import SelectPayment from "./SelectPayment";
    import NoLoginText from "../components/NoLoginText";

    export default {
        components: {
            SelectPayment,
            NoLoginText
        },
        data() {
            return {
                orderData: {},
                order: {
                    total_price: ''
                },
                orderDetail: null
            }
        },
        created() {
            axios.get(`http://${window.location.hostname}:8000/api/orders/order/` + this.$route.params.id + '/', {
                headers: {
                    Authorization: `JWT ${this.$store.state.jwt}`,
                    'Content-Type': 'application/json'
                }
            }).then(res => {
                this.order = res.data.data.order[0]
                this.orderDetail = res.data.data.order_detail
            }).catch()
        }
    }
</script>

<style scoped>
    .el-alert__description {
        margin-top: 0;
    }
</style>