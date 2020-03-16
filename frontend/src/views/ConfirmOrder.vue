<template>
    <div class="sm:mx-0 md:mx-24 lg:mx-0 xl:mx-0">
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <h1 class="mt-10 py-1 text-xl font-l">Product</h1>

        <!--        show this when no item in cart-->
        <div v-if="$store.state.inCart.cart_detail.length == 0"
             class="bg-white w-full px-1 pb-16 mx-auto h-64 relative">
            <div class="center-y w-full">
                <h1 class="text-2xl text-center">No Item in Cart</h1>
                <h1 @click="goHome" class="text-center text-orange cursor-pointer">Go back to Homepage</h1>
            </div>
        </div>

        <!--        show when have item in cart-->
        <div v-else>
            <div class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 pb-16 mx-auto ">
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
                    <tr v-for="item in $store.state.inCart.cart_detail" :key="item.id" class="border-bottom">
                        <td class="px-2 py-2">

                            <img class="w-full mx-auto" style="max-width: 120px;height: 120px; object-fit: contain"
                                 :src="$store.state.endpoints.host + item.product.pic1"
                                 alt="">
                        </td>
                        <td class="px-2 py-2">{{item.product.title}}</td>
                        <td class="px-2 py-2 text-center text-green">{{item.product.price}}</td>
                        <td class="px-2 py-2 text-center">{{item.quantity}}</td>
                        <td class="px-2 py-2 text-center text-green">{{item.price}}</td>
                    </tr>
                    </tbody>
                </table>
                <div class="px-5 md:px-10 font-l mt-5 text-xl">
                    <div class="flex justify-between">
                        <h1 class="">SubTotal</h1>
                        <h1 class="text-green">{{subTotal}} €</h1>
                    </div>
                    <div class="flex justify-between">
                        <h1 class="">Shipping</h1>
                        <h1 class="">{{shipping}} €</h1>
                    </div>
                    <div class="flex justify-between">
                        <h1 class="">Coupon Code</h1>
                        <h1 class="">{{getCode.name}}</h1>
                    </div>
                    <div class="flex justify-between">
                        <h1 class="">Total</h1>
                        <h1 class="text-green">{{total}} €</h1>
                    </div>
                </div>
            </div>

            <div class="flex justify-between px-1 sm:px-0">
                <h1 class="mt-5 py-1 text-xl font-l">Shipping Information</h1>
                <h1 @click="showModal" class="mt-5 py-1 text-sm font-l self-end text-gray cursor-pointer">Change</h1>
            </div>
            <div class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 mx-auto py-5">
                <div class="px-5 md:px-10 font-l text-lg">
                    <div class="flex justify-between">
                        <h1 class="">Recipient</h1>
                        <h1 class="text-right">
                            {{this.$store.state.userAddress[$store.state.indexUserAddress].recipient}}</h1>
                    </div>
                    <div class="flex justify-between">
                        <h1>Address</h1>
                        <h1 class="text-right">
                            {{this.$store.state.userAddress[$store.state.indexUserAddress].house_number}},
                            {{this.$store.state.userAddress[$store.state.indexUserAddress].street}},
                            {{this.$store.state.userAddress[$store.state.indexUserAddress].city}}
                            {{this.$store.state.userAddress[$store.state.indexUserAddress].post_code}}
                        </h1>
                    </div>
                </div>
            </div>


            <div class="flex justify-between pt-10">
                <button class="w-32 text-black_p py-2 focus:outline-none flex justify-start"
                        type="button">
                    <p class="inline-flex ml-0">
                        <i class="material-icons">keyboard_arrow_left</i><span>Previous</span>
                    </p>
                </button>
                <div @click="goPayment"
                     class="w-64 bg-green text-white text-center py-2 px-2 focus:outline-none cursor-pointer">
                    Confirm Order and Go Payment
                </div>
            </div>
        </div>

        <!--        modal-->
        <modal :type="typeModal" :total="[subTotal,shipping,getCode.name,total]" v-show="isModalVisible"
               @close="closeModal"/>

        <!--        <modal type="check_confirm" v-show="isConfirmModalVisible" @close="closeConfirmModal"/>-->
    </div>
</template>

<script>
    import axios from "axios";
    import Modal from "../components/Modal";

    export default {
        components: {
            Modal
        },
        data() {
            return {
                isModalVisible: false,
                isConfirmModalVisible: false,
                typeModal: '',
                isPass: false
            }
        },
        created() {
            this.loadAddress()
        },
        methods: {
            goHome() {
                this.$router.push({
                    name: 'HomePage'
                })
            },
            showModal() {
                this.typeModal = 'address'
                this.isModalVisible = true;
            },
            closeModal() {
                this.isModalVisible = false;
            },
            loadAddress() {
                axios.get(this.$store.state.endpoints.addressUrL, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    }
                }).then(
                    res => {
                        // this.addresses = res.data.address
                        this.$store.commit("setUserAddress", res.data.address);
                    }
                ).catch(e => {
                    this.$message.error('Oops, Something is Error. code ' + e.status + ', add load address');
                })
            },
            goPayment() {
                this.typeModal = 'check_confirm'
                this.isModalVisible = true

            },
            confirmOrder() {
                console.log('save')

            }
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
            shipping() {
                let shipping = 2
                if (this.subTotal == 0) {
                    return 0
                } else {
                    return shipping
                }
            },
            totalShipping() {
                return Number(this.subTotal) + Number(this.shipping)
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
            total() {
                return (this.totalShipping - ((this.totalShipping / 100) * this.getCode.percent)).toFixed(2)
            }
        }
    }
</script>

<style scoped>
</style>