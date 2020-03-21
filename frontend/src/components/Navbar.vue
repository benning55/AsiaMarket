<template>
    <div>
        <!--        navbar desktop version-->
        <div class="fixed w-full z-110  bg-white shadow-lg">
            <div class="hidden sm:hidden md:hidden lg:block h-6 w-full bg-orange text-center text-white">
                {{this.banner}}
            </div>
            <nav class="hidden sm:hidden md:hidden lg:block  flex items-center  ">
                <ul class="w-full flex justify-between">
                    <li class="flex-1 hidden sm:hidden md:hidden lg:inline-block px-5 pt-4">
                        <a @click="goHome" class="cursor-pointer" style="font-size: 24px;margin-top: 16px">ThaiMarket
                            Express</a>
                        <!--                    <img src="../assets/Logo/logo.jpg">-->
                    </li>
                    <li class="flex-1">
                        <div class="pt-4 relative mx-auto text-black">
                            <input v-model="searchText"
                                   v-on:keyup.enter="goSearch(searchText)"
                                   class="bg-unHilight h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none w-full"
                                   type="search" name="search"
                                   :placeholder="nameTranslate('Find Product(ค้นหาสินค้า)')">
                            <button @click="goSearch(searchText)" type="submit" class="absolute right-0 mt-5 mr-4"
                                    style="top:8px">
                                <svg class="text-gray-600 h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg"
                                     xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px"
                                     y="0px"
                                     viewBox="0 0 56.966 56.966" style="enable-background:new 0 0 56.966 56.966;"
                                     xml:space="preserve"
                                     width="512px" height="512px">
                                    <path d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z"/>
                                </svg>
                            </button>
                        </div>
                    </li>
                    <li class="flex-1 px-5 text-right  py-6">
                        <a @click="changeLocale(`en`)" class="cursor-pointer"
                           :class="{'text-green':$i18n.locale == 'en'}">EN </a>
                        |
                        <a @click="changeLocale(`th`)" class="cursor-pointer"
                           :class="{'text-green':$i18n.locale == 'th'}">
                            TH</a>
                    </li>
                </ul>
            </nav>

        </div>

        <!--        navbar mobile version-->
        <div class="fixed w-full z-110 bg-white">
            <div class="block sm:block md:block lg:hidden h-6 w-full bg-orange text-center text-white">
                {{this.banner}}
            </div>
            <nav class="block sm:block md:block lg:hidden  flex items-center justify-between flex-wrap  py-5 shadow-lg"
                 style="height: 72px;">
                <ul class="w-full flex justify-between">
                    <li @click="mobileDrawer = !mobileDrawer,cartDrawer = false"
                        class="inline-block sm:inline-block md:inline-block lg:hidden px-5 "><i
                            class="material-icons text-3xl">menu</i>
                    </li>
                    <li class="inline-block cursor-pointer flex">
                        <h1 @click="goHome" style="font-size: 19px;">ThaiMarket Express</h1>
                    </li>
                    <li class="float-right px-5">
                        <div @click="cartDrawer = !cartDrawer, mobileDrawer =false" class="relative">
                            <el-badge :value="$store.state.inCart.cart_detail.length" class="item" type="primary">
                                <img class="w-8 mx-auto" src="../assets/icon/supermarket.svg">
                            </el-badge>
                        </div>
                    </li>
                </ul>
            </nav>

        </div>

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
                            <h1 class="text-md text-center">{{$t('account')}}</h1>
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
                            <h1 class="text-md text-center">{{$t('category')}}</h1>
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
                <NavbarSpace/>
                <div class="relative h-100 w-70 bg-white">
                    <div class="py-3 px-10 text-xl text-center border-bottom font-l bg-gray_bg cursor-pointer block lg:hidden">
                        <a @click="changeLocale(`en`)" class="cursor-pointer"
                           :class="{'text-green':$i18n.locale == 'en'}">EN </a> | <a
                            @click="changeLocale(`th`)" class="cursor-pointer"
                            :class="{'text-green':$i18n.locale == 'th'}"> TH</a>
                    </div>

                    <div class="block lg:hidden py-3 px-3 text-xl border-bottom font-l text-orange cursor-pointer">
                        <div class="relative mx-auto text-black">
                            <input v-model="searchText" v-on:keyup.enter="goSearch(searchText)"
                                   class="border-2 border-lightGray bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none w-full"
                                   type="search" name="search" placeholder="Search">
                            <button @click="goSearch(searchText)" type="submit" class="absolute right-0 mt-3 mr-4"
                                    style="top:0px">
                                <svg class="text-gray-600 h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg"
                                     xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px"
                                     y="0px"
                                     viewBox="0 0 56.966 56.966" style="enable-background:new 0 0 56.966 56.966;"
                                     xml:space="preserve"
                                     width="512px" height="512px">
                                    <path d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z"/>
                                </svg>
                            </button>
                        </div>
                    </div>

                    <!--                    show when not log in-->
                    <div v-if="!$store.state.isAuthenticated" class="block lg:hidden">
                        <div @click="goLogin"
                             class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">
                            {{$t('login')}}
                        </div>
                        <div @click="goRegister"
                             class="py-3 px-10 text-xl font-l hover:bg-unHilight cursor-pointer">
                            {{$t('register')}}
                        </div>
                        <div class="pb-3 pt-5 px-5 text-xl bg-gray_bg"></div>
                    </div>

                    <!--                    show when logged in-->
                    <div v-else class="block lg:hidden">
                        <div class="py-3 px-10 text-xl border-bottom hover:bg-unHilight">
                            <i @click="mobileDrawer =! mobileDrawer"
                               class="material-icons text-2xl cursor-pointer absolute"
                               style="top:128px;left: 0px;font-size: 2.5rem;">keyboard_arrow_left</i>
                            {{firstname_lastname}}
                        </div>
                        <div @click="goOrder"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                            {{$t('order_history')}}
                        </div>
                        <div @click="goProfile"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                            {{$t('personal_detail')}}
                        </div>
                        <div @click="goAddress"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                            {{$t('address')}}
                        </div>
                        <div class="pb-3 pt-5 px-5 text-xl bg-gray_bg"></div>
                    </div>

                    <div @click="goCategory({id:'recommend'})"
                         class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                        <span>{{$t('recommend')}}</span>
                    </div>
                    <div @click="goCategory({id:'new-product'})"
                         class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                        <span>{{$t('new_product')}}</span>
                    </div>

                    <div class="pb-3 pt-5 px-5 text-xl cursor-pointer bg-gray_bg">{{$t('product')}}</div>
                    <div v-for="category in categorys" :key="category.id" @click="goCategory(category)"
                         class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                        <span>{{nameTranslate(category.type)}}</span>
                    </div>
                    <div class="pb-3 pt-5 px-5 text-xl cursor-pointer bg-gray_bg"></div>
                    <div v-if="$store.state.isAuthenticated" @click="logout"
                         class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer block lg:hidden">
                        {{$t('logout')}}
                    </div>
                </div>
            </div>
        </transition>

        <!--cart screen-->
        <!--        <transition name="slide">-->
        <div v-if="cartDrawer" class="inset-y-0 right-0 bg-white fixed z-20 shadow-md z-105">
            <NavbarSpace/>
            <div class="relative h-full w-70 overflow-auto">
                <div class="w-70 p-3 text-xl border-bottom fixed justify-between flex bg-white">
                    <el-badge :value="$store.state.inCart.cart_detail.length" class="item" type="primary">
                        <img class="w-8 mx-auto" src="../assets/icon/supermarket.svg">
                    </el-badge>
                    {{$t('my_cart')}}
                    <i @click="cartDrawer = !cartDrawer" class="material-icons text-3xl cursor-pointer">keyboard_arrow_right</i>
                </div>
                <div class="w-full">
                    <ul class="w-full" style="height: 3.5rem"></ul>
                    <InCartItem v-for="item in $store.state.inCart.cart_detail" :key="item.id" :data="item"/>
                    <div class="w-full" style="height: 273px"></div>
                </div>
            </div>
            <div class="fixed-b w-70 bottom-0  border-top p-2 bg-white z-50 appearance-none">
                <div class="flex justify-between font-l">
                    <div class="">{{$t('subTotal')}}</div>
                    <div>{{subTotal}} €</div>
                </div>
                <div class="flex justify-between font-l">
                    <div class="">{{$t('shipping')}}</div>
                    <div>{{shipping}} €</div>
                </div>
                <div class="flex justify-between font-l my-1">
                    <div class="">{{$t('coupon_code')}}</div>
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
                    <div class="">{{$t('total')}}</div>
                    <div>{{total}} €</div>
                </div>

                <el-popover
                        v-if="checkPass.length > 0"
                        placement="top"
                        :title="nameTranslate('Product Incorrect(สินค้าไม่ถูกต้อง)')"
                        width="300"
                        trigger="click"
                        :content="nameTranslate('Some Product maybe out of stock or not enough please edit and try again(สินค้าบางชื้นหมดแล้วหรือมีไม่เพียงพอ กรุณาแก้ไขสินค้าชิ้นนั้น)')">
                    <button
                            slot="reference"
                            class="w-full h-10 bg-orange mt-3 text-white flex justify-center opacity-50 cursor-not-allowed">
                        <img width="25px" class="mx-3" src="../assets/icon/supermarket_white.svg">
                        {{$t('process_to_checkout')}}
                    </button>
                </el-popover>
                <button v-else-if="subTotal == 0"
                        class="w-full h-10 bg-orange mt-3 text-white flex justify-center opacity-50 cursor-not-allowed">
                    <img width="25px" class="mx-3" src="../assets/icon/supermarket_white.svg">
                    {{$t('process_to_checkout')}}
                </button>
                <button v-else @click="goCheckOut"
                        class="w-full h-10 bg-orange mt-3 text-white flex justify-center">
                    <img width="25px" class="mx-3" src="../assets/icon/supermarket_white.svg">
                    {{$t('process_to_checkout')}}
                </button>
            </div>
        </div>
        <!--        </transition>-->

        <!--right screen-->
        <transition name="slide">
            <div v-if="accountDrawer" class="inset-y-0 right-0 bg-gray_bg fixed z-20 shadow-md z-105">
                <NavbarSpace/>
                <div class="relative h-100 w-70 bg-white">
                    <!--                    show when not log in-->
                    <div v-if="!$store.state.isAuthenticated">
                        <div @click="goLogin"
                             class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">
                            {{$t('login')}}
                        </div>
                        <div @click="goRegister"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                            {{$t('register')}}
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
                            {{$t('order_history')}}
                        </div>
                        <div @click="goProfile"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                            {{$t('personal_detail')}}
                        </div>
                        <div @click="goAddress"
                             class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">
                            {{$t('address')}}
                        </div>
                        <div class="pb-3 pt-5 px-5 text-xl cursor-pointer bg-gray_bg"></div>
                        <div v-if="$store.state.isAuthenticated" @click="logout"
                             class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">
                            {{$t('logout')}}
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
    import NavbarSpace from "./NavbarSpace";

    export default {
        name: "Navbar",
        components: {
            InCartItem,
            NavbarSpace
        },
        data() {
            return {
                accountDrawer: false,
                cartDrawer: false,
                mobileDrawer: false,
                categorys: [
                    {id: 1, type: "Fruits and Vegetables(ผักและผลไม้)", color: "green"},
                    {id: 2, type: "Dry goods and Seasonings(ของแห้งและเครื่องปรุงรส)", color: "blue"},
                    {id: 3, type: "Rice Flour and Noodles( แป้งและเส้น)", color: "yellow"},
                    {id: 4, type: "Condiments and Sauces(เครื่องปรุงรสและซอส)", color: "red"},
                    {id: 5, type: "Normal and Alcoholic Beverages(เครื่องดื่มและแอลกอฮอล์)", color: "black"},
                    {id: 6, type: "Snack(ขนมขบเคี้ยว)", color: "orange"},
                    {id: 7, type: "Frozen Products(อาหารแช่แข็ง)", color: "purple"},
                    {id: 8, type: "Other(อื่น ๆ)", color: "pink"},
                ],
                itemIncart: [],
                code: '',
                codeStatus: 'none',
                percent: 0,
                shipping_fee: 0,
                searchText: '',
                banner: []
            }
        },
        created() {
            this.updateCart()
            this.updateShipping()
            this.getBannerData()
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
            goSearch(text) {
                if (text.length > 0) {
                    this.toggleOpacity()
                    this.$router.push({
                        name: 'SearchView',
                        params: {id: text}
                    })
                }
            },

            getBannerData() {
                axios.get(`${this.$store.state.endpoints.host}/api/banner/`).then(res => {
                    this.banner = res.data.data[0].description
                    this.isLoading = false
                }).catch(e => {
                    this.$message.error(this.$t('error_Oops_') + e.status + ', at load recommend');
                })
            },

            updateCart() {
                axios.get(`${this.$store.state.endpoints.host}/api/products/cart/`, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                }).then(res => {
                    for (let i = 0; i < res.data.data.cart_detail.length; i++) {
                        if (res.data.data.cart_detail[i].quantity == 0) {
                            res.data.data.cart_detail[i].overStatus = false
                            res.data.data.cart_detail[i].quantity = 1
                        } else if (res.data.data.cart_detail[i].quantity > res.data.data.cart_detail[i].product.quantity) {
                            res.data.data.cart_detail[i].overStatus = true
                            res.data.data.cart_detail[i].quantity = 0
                        } else {
                            res.data.data.cart_detail[i].overStatus = false
                        }
                    }
                    this.$store.commit("setIncart", res.data.data);
                }).catch(() => {
                    this.$store.commit("setIncart", {
                        cart_detail: []
                    });
                })
            },
            updateShipping() {
                axios.get(`${this.$store.state.endpoints.host}/api/orders/shipping-fee/`, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                }).then(res => {
                        this.shipping_fee = Number(res.data.price)
                        this.$store.commit("setShippingFee", this.shipping_fee)
                    }
                ).catch()
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
                localStorage.setItem("setLocalLanguage", locale)
                this.toggleOpacity()
            },
            checkCode() {
                clearTimeout(this.timeout)
                this.codeStatus = 'loading'
                this.timeout = setTimeout(() => {
                    axios.post(`${this.$store.state.endpoints.host}/api/products/code/`, {
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
                        this.updateCart()
                    }).catch(() => {
                        this.codeStatus = 'error'
                        this.$store.state.inCart.code = null
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
            }
            ,
            checkPass() {
                let p = []
                this.$store.state.inCart.cart_detail.reduce(function (accumulate, data) {
                    if (data.overStatus == true || data.product.quantity == 0) {
                        return p.push('4')
                    }
                }, 0);
                return p
            }
            ,
            subTotal() {
                let sum = this.$store.state.inCart.cart_detail.reduce(function (accumulate, data) {
                    if (data.overStatus == true || data.product.quantity == 0) {
                        return accumulate + 0;
                    } else {
                        return accumulate + Number(data.price);
                    }
                }, 0);
                return (sum).toFixed(2);
            }
            ,
            shipping() {
                if (this.subTotal == 0) {
                    return 0
                } else {
                    return this.$store.state.shippingFee
                }
                return 0
            }
            ,
            totalShipping() {
                return Number(this.subTotal) + Number(this.shipping)
            }
            ,
            getCode() {
                if (this.$store.state.inCart.code == null) {
                    return 0
                } else {
                    return this.$store.state.inCart.code[0]
                }
            }
            ,
            total() {
                if (this.codeStatus == 'error') {
                    return this.totalShipping.toFixed(2)
                } else {
                    return (this.totalShipping - ((this.totalShipping / 100) * this.percent)).toFixed(2)
                }
            }
        }
        ,
        watch: {
            '$route.name'() {
                this.updateCart()
                this.updateShipping()
            },
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
            }
            ,
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
    .fixed-b {
        position: absolute;
    }

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
        /*width: 220px;*/
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