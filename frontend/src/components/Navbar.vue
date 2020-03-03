<template>
    <div>
        <!--        navbar desktop version-->
        <nav class="hidden sm:hidden md:hidden lg:block shadow-lg flex items-center justify-between flex-wrap bg-white py-6 fixed w-full z-110">
            <ul class="w-full">
                <li @click="goHome" class="hidden sm:hidden md:hidden lg:inline-block px-5 cursor-pointer">LOGO</li>
                <li class="float-right px-5 flex-grow">
                    <a @click="changeLocale(`en`)" class="cursor-pointer" :class="{'text-green':$i18n.locale == 'en'}">EN </a>
                    |
                    <a @click="changeLocale(`th`)" class="cursor-pointer" :class="{'text-green':$i18n.locale == 'th'}">
                        TH</a>
                </li>
            </ul>
        </nav>


        <!--        navbar mobile version-->
        <nav class="block sm:block md:block lg:hidden shadow-lg flex items-center justify-between flex-wrap bg-white py-5 fixed w-full z-110"
             style="height: 72px;">
            <ul class="w-full flex justify-between">
                <li @click="mobileDrawer = !mobileDrawer,cartDrawer = false"
                    class="inline-block sm:inline-block md:inline-block lg:hidden px-5 "><i
                        class="material-icons text-3xl">menu</i>
                </li>
                <li @click="goHome" class="inline-block cursor-pointer">Logo</li>
                <li class="float-right px-5">
                    <div @click="cartDrawer = !cartDrawer, mobileDrawer =false" class="relative">
                        <el-badge :value="$store.state.inCart.cart_detail.length" class="item" type="primary">
                            <img class="w-8 mx-auto" src="../assets/icon/supermarket.svg">
                        </el-badge>
                        <!--                        <img class="w-8 mx-auto" src="../assets/icon/supermarket.svg">-->
                        <!--                        <div class="absolute text-white rounded-full h-5 w-5 flex items-center justify-center bg-green count-position3">-->
                        <!--                            {{$store.state.inCart.cart_detail.length}}-->
                        <!--                        </div>-->
                    </div>
                </li>
            </ul>
        </nav>

        <!--        left menu on screen-->
        <!--        <div class="inset-y-0 left-0 fixed hidden sm:hidden md:hidden lg:block">-->
        <!--            <div class="container px-5">-->
        <!--                <ul class="mt-24">-->
        <!--                    <li @click="goHome" class="mb-4 hover:text-green cursor-pointer">Home</li>-->
        <!--                    <li class="mb-1 text-gray cursor-pointer">Promotion</li>-->
        <!--                    <li class="mb-1 text-gray cursor-pointer">Recomment</li>-->
        <!--                    <li @click="goCategory({id:'new-product'})" class="mb-4 hover:text-green cursor-pointer">New-->
        <!--                        Product-->
        <!--                    </li>-->
        <!--                    <li v-for="category in categorys" :key="category.id" class="mb-1 hover:text-green cursor-pointer">-->
        <!--                        <span @click="goCategory(category)">{{category.type}}</span>-->
        <!--                    </li>-->
        <!--                </ul>-->
        <!--            </div>-->
        <!--        </div>-->

        <!--        mini button right screen-->
        <div class="inset-y-0 right-0 fixed hidden sm:hidden md:hidden lg:block z-105">
            <div class="container">
                <div class="vertical-center">
                    <div class="shadow-md">
                        <div @click="cartDrawer = !cartDrawer"
                             class="w-20 bg-white hover:bg-unHilight py-3 rounded-tl-lg border-bottom cursor-pointer">
                            <img class="w-8 mx-auto" src="../assets/icon/supermarket.svg">
                            <h1 class="text-lg text-center text-green">{{total}} €</h1>
                            <div class=" text-white rounded-full h-5 w-5 flex items-center justify-center bg-green absolute count-position">
                                {{$store.state.inCart.cart_detail.length}}
                            </div>
                        </div>
                        <div @click="accountDrawer = !accountDrawer"
                             class="w-20 bg-white hover:bg-unHilight py-3 rounded-bl-lg cursor-pointer">
                            <img class="w-8 mx-auto " src="../assets/icon/user.svg">
                            <h1 class="text-md text-center">Account</h1>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!--        mini button left screen-->
        <div class="inset-y-0 left-0 fixed hidden sm:hidden md:hidden lg:block z-105">
            <div class="container">
                <div class="vertical-center-left">
                    <div class="shadow-md">
                        <div @click="mobileDrawer = !mobileDrawer"
                             class="w-20 bg-white hover:bg-unHilight py-3 rounded-r-lg cursor-pointer">
                            <img class="w-8 mx-auto " src="../assets/icon/next.svg">
                            <h1 class="text-md text-center">Category</h1>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!--        opacity background -->
        <transition name="fade">
            <div v-if="accountDrawer || mobileDrawer || cartDrawer" @click="toggleOpacity"
                 class="w-full h-screen fixed bg-black opacity-50 z-105"></div>
        </transition>

        <!--left screen mobile version-->
        <transition name="slide-left">
            <div v-if="mobileDrawer"
                 class="inset-y-0 left-0 fixed bg-gray_bg fixed z-20 shadow-md w-70  overflow-auto h-screen z-105">
                <ul class="w-full py-6">L</ul>
                <div class="relative h-100 w-70 bg-white">
                    <div class="py-3 px-10 text-xl text-center border-bottom font-l bg-gray_bg cursor-pointer block lg:hidden">
                        <a @click="changeLocale(`en`)" class="cursor-pointer"
                           :class="{'text-green':$i18n.locale == 'en'}">EN </a> | <a
                            @click="changeLocale(`th`)" class="cursor-pointer"
                            :class="{'text-green':$i18n.locale == 'th'}"> TH</a>
                    </div>

                    <!--                    show when not log in-->
                    <div v-if="!$store.state.isAuthenticated" class="block lg:hidden">
                        <div @click="goLogin"
                             class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">
                            Login
                        </div>
                        <div @click="goRegister"
                             class="py-3 px-10 text-xl font-l hover:bg-unHilight cursor-pointer">
                            Register
                        </div>
                        <div class="pb-3 pt-5 px-5 text-xl bg-gray_bg"></div>
                    </div>

                    <!--                    show when logged in-->
                    <div v-else class="block lg:hidden">
                        <div class="py-3 px-10 text-xl border-bottom hover:bg-unHilight">
                            <i @click="mobileDrawer =! mobileDrawer"
                               class="material-icons text-2xl cursor-pointer absolute"
                               style="top:61px;left: 0px;font-size: 2.5rem;">keyboard_arrow_left</i>
                            {{firstname_lastname}}
                        </div>
                        <div @click="goOrder"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Order
                            history
                        </div>
                        <div @click="goProfile"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Personal
                            Detail
                        </div>
                        <div @click="goAddress"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Address
                        </div>
                        <div class="py-3 px-10 text-xl font-l hover:bg-unHilight cursor-pointer">Payment</div>
                        <div class="pb-3 pt-5 px-5 text-xl bg-gray_bg"></div>
                    </div>

                    <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                        <span>Promotion</span>
                    </div>
                    <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                        <span>Recommend</span>
                    </div>
                    <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                        <span @click="goCategory({id:'new-product'})">New Product</span>
                    </div>

                    <div class="pb-3 pt-5 px-5 text-xl cursor-pointer bg-gray_bg">Product</div>
                    <div v-for="category in categorys" :key="category.id"
                         class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                        <span @click="goCategory(category)">{{category.type}}</span>
                    </div>
                    <div class="pb-3 pt-5 px-5 text-xl cursor-pointer bg-gray_bg"></div>
                    <div v-if="$store.state.isAuthenticated" @click="logout"
                         class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer block lg:hidden">
                        Log Out
                    </div>
                </div>
            </div>
        </transition>

        <!--cart screen-->
        <transition name="slide">
            <div v-if="cartDrawer" class="inset-y-0 right-0 bg-white fixed z-20 shadow-md z-105">
                <ul class="w-full py-6">L</ul>
                <div class="relative h-full w-70 overflow-auto">
                    <div class="w-70 p-3 text-xl border-bottom fixed justify-between flex bg-white">
<!--                        <img class="w-8" src="../assets/icon/supermarket.svg">-->
<!--                        <div class="text-white rounded-full h-5 w-5 flex items-center justify-center bg-green absolute count-position2">-->
<!--                            {{$store.state.inCart.cart_detail.length}}-->
<!--                        </div>-->
                        <el-badge :value="$store.state.inCart.cart_detail.length" class="item" type="primary">
                            <img class="w-8 mx-auto" src="../assets/icon/supermarket.svg">
                        </el-badge>
                        My Cart
                        <i @click="cartDrawer = !cartDrawer" class="material-icons text-3xl cursor-pointer">keyboard_arrow_right</i>
                    </div>
                    <div class="w-full">
                        <ul class="w-full" style="height: 3.5rem"></ul>
                        <InCartItem v-for="item in $store.state.inCart.cart_detail" :key="item.id" :data="item"/>
                        <div class="w-full" style="height: 249px"></div>
                    </div>
                </div>
                <div class="fixed w-70 bottom-0  border-top p-2 bg-white z-50">
                    <div class="flex justify-between font-l">
                        <div class="">Subtotal</div>
                        <div>{{subTotal}} €</div>
                    </div>
                    <div class="flex justify-between font-l">
                        <div class="">Shipping</div>
                        <div>{{shipping}} €</div>
                    </div>
                    <div class="flex justify-between font-l my-1">
                        <div class="">Coupon Code</div>
                        <div class="flex">
                            <input v-model="code"
                                   @input="checkCode"
                                   class="appearance-none border rounded-l-lg w-24 py-1 px-2 text-gray leading-tight focus:outline-none"
                                   id="username"
                                   type="text"/>
                            <div v-if="codeStatus == 'ok'" class="height1-85 bg-green rounded-r-lg"
                                 style="padding: 4px">
                                <i class="fas fa-check text-white"></i>
                            </div>

                            <div v-else-if="codeStatus == 'loading'" class="height1-85 bg-green rounded-r-lg opacity-50"
                                 style="padding: 4px">
                                <img src="../assets/icon/Rolling-1s-24px.svg">
                            </div>

                            <div v-else-if="codeStatus == 'none'" class="height1-85 bg-green rounded-r-lg opacity-50"
                                 style="padding: 4px">
                                <i class="fas fa-check text-white"></i>
                            </div>

                            <div v-else class="height1-85 bg-red rounded-r-lg text-center"
                                 style="padding: 3px">
                                <i class="fas fa-times text-white"></i>
                            </div>
                        </div>
                    </div>
                    <div class="flex justify-between">
                        <div class="">Total</div>
                        <div>{{total}} €</div>
                    </div>
                    <button v-if="subTotal > 0" @click="goCheckOut"
                            class="w-full h-10 bg-orange mt-3 text-white flex justify-center">
                        <img width="25px" class="mx-3" src="../assets/icon/supermarket_white.svg">
                        Process to checkout
                    </button>
                    <button v-else
                            class="w-full h-10 bg-orange mt-3 text-white flex justify-center opacity-50 cursor-not-allowed">
                        <img width="25px" class="mx-3" src="../assets/icon/supermarket_white.svg">
                        Process to checkout
                    </button>
                </div>
            </div>
        </transition>

        <!--right screen-->
        <transition name="slide">
            <div v-if="accountDrawer" class="inset-y-0 right-0 bg-gray_bg fixed z-20 shadow-md z-105">
                <ul class="w-full py-6">L</ul>
                <div class="relative h-100 w-70 bg-white">
                    <!--                    show when not log in-->
                    <div v-if="!$store.state.isAuthenticated">
                        <div @click="goLogin"
                             class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">
                            Login
                        </div>
                        <div @click="goRegister"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                            Register
                        </div>
                    </div>

                    <!--                    show when logged in-->
                    <div v-else>
                        <div class="py-3 px-10 text-xl border-bottom hover:bg-unHilight cursor-pointer">
                            <i @click="accountDrawer =! accountDrawer"
                               class="material-icons text-2xl cursor-pointer absolute"
                               style="top:7px;left: 0px;font-size: 2.5rem;">keyboard_arrow_left</i>
                            {{firstname_lastname}}
                        </div>
                        <div @click="goOrder"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                            Order history
                        </div>
                        <div @click="goProfile"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                            Personal Detail
                        </div>
                        <div @click="goAddress"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                            Address
                        </div>
                        <div class="py-3 px-10 text-xl font-l hover:bg-unHilight cursor-pointer">
                            Payment
                        </div>
                        <div class="pb-3 pt-5 px-5 text-xl cursor-pointer bg-gray_bg"></div>
                        <div v-if="$store.state.isAuthenticated" @click="logout"
                             class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">
                            Log Out
                        </div>
                    </div>
                </div>
            </div>
        </transition>

    </div>
</template>
<script>
    import i18n from "../plugins/i18n";
    import InCartItem from "./InCartItem";
    import axios from 'axios'

    export default {
        name: "Navbar",
        components: {
            InCartItem
        },
        data() {
            return {
                accountDrawer: false,
                cartDrawer: false,
                mobileDrawer: false,
                categorys: [
                    {id: 1, type: "Fruits and Vegetables", color: "green"},
                    {id: 2, type: "Dry goods and Seasonings", color: "blue"},
                    {id: 3, type: "Rice Flour and Noodles", color: "yellow"},
                    {id: 4, type: "Condiments and Sauces", color: "red"},
                    {id: 5, type: "Normal and Alcoholic Beverages", color: "black"},
                    {id: 6, type: "Snack", color: "orange"},
                    {id: 7, type: "Frozen Products", color: "purple"},
                    {id: 8, type: "Other", color: "pink"},
                ],
                itemIncart: [],
                code: '',
                codeStatus: 'none',
                percent: 0,

            }
        },
        created() {
            this.updateCart()
        },
        methods: {
            updateCart() {
                axios.get(`http://${window.location.hostname}:8000/api/products/cart/`, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                }).then(res => {
                    for (let i = 0; i < res.data.data.cart_detail.length; i++) {
                        // console.log(res.data.data.cart_detail[i])
                        if (res.data.data.cart_detail[i].quantity > res.data.data.cart_detail[i].product.quantity) {
                            res.data.data.cart_detail[i].overStatus = true
                            // res.data.data.cart_detail[i].price = 0
                            res.data.data.cart_detail[i].quantity = res.data.data.cart_detail[i].product.quantity
                            // axios.post(this.$store.state.endpoints.editInCart, {
                            //     quantity: res.data.data.cart_detail[i].quantity,
                            //     product_id: res.data.data.cart_detail[i].product.id
                            // }, {
                            //     headers: {
                            //         Authorization: `JWT ${this.$store.state.jwt}`,
                            //         'Content-Type': 'application/json'
                            //     },
                            // }).then((res) => {
                            //     console.log(res)
                            // }).catch()
                        }
                    }
                    this.$store.commit("setIncart", res.data.data);
                }).catch(() => {
                    this.$store.commit("setIncart", {
                        cart_detail: []
                    });
                })
            },
            goHome() {
                this.$router.push({
                    name: 'HomePage'
                })
                this.toggleOpacity()
            },
            goLogin() {
                this.$router.push({
                    name: "login"
                })
                this.toggleOpacity()
            },
            goRegister() {
                this.$router.push({
                    name: "register"
                })
                this.toggleOpacity()
            },
            goProfile() {
                this.$router.push({
                    name: 'ViewProfile'
                })
                this.toggleOpacity()
            },
            goOrder() {
                this.$router.push({
                    name: 'ViewOrderHistory'
                })
                this.toggleOpacity()
            },
            goAddress() {
                this.$router.push({
                    name: 'ViewAddress'
                })
                this.toggleOpacity()
            },
            goCategory(category) {
                this.$router.push({
                    name: 'Category',
                    params: {id: category.id}
                })
                this.toggleOpacity()
            },
            toggleOpacity() {
                this.accountDrawer = false
                this.cartDrawer = false
                this.mobileDrawer = false
            },
            changeLocale(locale) {
                i18n.locale = locale
                this.toggleOpacity()
            },
            checkCode() {
                clearTimeout(this.timeout)
                this.codeStatus = 'loading'

                this.timeout = setTimeout(() => {
                    axios.post(`http://${window.location.hostname}:8000/api/products/code/`, {
                        code_name: this.code
                    }, {
                        headers: {
                            Authorization: `JWT ${this.$store.state.jwt}`,
                            'Content-Type': 'application/json'
                        },
                    }).then(res => {
                        if (res.data.success == "code is delete") {
                            this.codeStatus = 'none'
                        } else {
                            this.codeStatus = 'ok'
                        }
                        console.log(res)
                        axios.get(`http://${window.location.hostname}:8000/api/products/cart/`, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(res => {
                            this.itemIncart = res.data.data
                            this.$store.commit("setIncart", this.itemIncart);
                            this.value = 0
                        }).catch()
                    }).catch(() => {
                        this.codeStatus = 'error'
                    })
                }, 1000)

            },
            goCheckOut() {
                this.$router.push({
                    name: "ConfirmOrder"
                })
                this.toggleOpacity()
            },
            logout() {
                this.$store.commit('removeToken');
                this.$router.push('/login');
                this.toggleOpacity()
            }
        },
        computed: {
            firstname_lastname() {
                let name = this.$store.state.authUser.user.first_name + ' ' + this.$store.state.authUser.user.last_name
                if (name.length > 20) {
                    return name.substring(0, 20) + '...'
                } else {
                    return name
                }
            },
            subTotal() {
                let sum = this.$store.state.inCart.cart_detail.reduce(function (accumulate, data) {
                    if (data.overStatus == true) {
                        console.log("kkkkk")
                    }
                    return accumulate + Number(data.price);
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
                    return 0
                } else {
                    return this.$store.state.inCart.code[0]
                }
            },
            total() {
                if (this.codeStatus == 'error') {
                    return this.totalShipping
                } else {
                    return (this.totalShipping - ((this.totalShipping / 100) * this.percent)).toFixed(2)
                }
            }
        },
        watch: {
            getCode: {
                deep: true,
                handler: function (code) {
                    if (code != 0) {
                        this.percent = Number(code.percent)
                        this.code = code.name
                    } else {
                        this.percent = 0
                        this.code = ''
                    }
                }
            },
            code: {
                deep: true,
                handler: function (newVal) {
                    if (this.codeStatus == 'loading') {
                        this.codeStatus = 'loading'
                    } else if (newVal.length > 0) {
                        this.codeStatus = 'ok'
                    } else {
                        this.codeStatus = 'none'
                    }
                }
            }
        }
    }
</script>

<style scoped>
    .z-105 {
        z-index: 105
    }

    .z-110 {
        z-index: 110
    }

    .w-70 {
        width: 20rem;
    }

    .container {
        height: 100%;
        width: 220px;
        position: relative;
    }

    .vertical-center {
        margin: 0;
        position: absolute;
        top: 50%;
        right: 0;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
    }

    .vertical-center-left {
        margin: 0;
        position: absolute;
        top: 50%;
        left: 0;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
    }

    .count-position {
        top: 9px;
        left: 47px;
        font-size: 13px;
        font-weight: 900;
    }

    .count-position2 {
        top: 9px;
        left: 35px;
        font-size: 13px;
        font-weight: 900;
    }

    .count-position3 {
        top: -4px;
        left: 21px;
        font-size: 13px;
        font-weight: 900;
    }

    .border-top {
        border-top: 1px solid #707070;
    }

    .height1-85 {
        height: 1.85rem;
        width: 1.85rem;
    }

    .bottom-73 {
        bottom: 73px;
    }

    .slide-enter-active, .slide-leave-active {
        transition: right .5s;
    }

    .slide-enter, .slide-leave-to {
        right: -325px;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity .5s;
    }

    .fade-enter, .fade-leave-to {
        opacity: 0;
    }

    .slide-left-enter-active, .slide-left-leave-active {
        transition: left .5s;
    }

    .slide-left-enter, .slide-left-leave-to {
        left: -325px;
    }
</style>