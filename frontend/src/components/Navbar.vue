<template>
    <div>
        <!--        navbar desktop version-->
        <nav class="hidden sm:hidden md:hidden lg:block shadow-lg flex items-center justify-between flex-wrap bg-white py-6 fixed w-full z-50">
            <ul class="w-full">
                <li @click="goHome" class="hidden sm:hidden md:hidden lg:inline-block px-5">LOGO</li>
                <li class="float-right px-5 flex-grow"><a @click="changeLocale(`en`)">EN </a> | <a
                        @click="changeLocale(`th`)"> TH</a>
                </li>
            </ul>
        </nav>


        <!--        navbar mobile version-->
        <nav class="block sm:block md:block lg:hidden shadow-lg flex items-center justify-between flex-wrap bg-white py-5 fixed w-full z-50"
             style="height: 72px">
            <ul class="w-full flex justify-between">
                <li @click="mobileDrawer = !mobileDrawer,cartDrawer = false"
                    class="inline-block sm:inline-block md:inline-block lg:hidden px-5 "><i
                        class="material-icons text-3xl">menu</i>
                </li>
                <li class="inline-block">Logo</li>
                <li class="float-right px-5">
                    <div @click="cartDrawer = !cartDrawer, mobileDrawer =false" class="relative">
                        <img class="w-8 mx-auto" src="../assets/icon/supermarket.svg">
                        <div class="absolute text-white rounded-full h-5 w-5 flex items-center justify-center bg-green count-position3">
                            2
                        </div>
                    </div>
                </li>
            </ul>
        </nav>

        <!--        left menu on screen-->
        <div class="inset-y-0 left-0 fixed hidden sm:hidden md:hidden lg:block">
            <div class="container px-5">
                <ul class="mt-24">
                    <li class="mb-4">Home</li>
                    <li class="mb-1">Promotion</li>
                    <li class="mb-1">Recomment</li>
                    <li class="mb-4">New Product</li>
                    <li v-for="category in categorys" :key="category.id" class="mb-1">{{category.type}}</li>
                </ul>
            </div>
        </div>

        <!--        mini button left screen-->
        <div class="inset-y-0 right-0 fixed hidden sm:hidden md:hidden lg:block">
            <div class="container">
                <div class="vertical-center">
                    <div class="shadow-md">
                        <div @click="cartDrawer = !cartDrawer"
                             class="w-20 bg-white hover:bg-unHilight py-3 rounded-tl-lg border-bottom cursor-pointer">
                            <img class="w-8 mx-auto" src="../assets/icon/supermarket.svg">
                            <h1 class="text-lg text-center text-green">229 $</h1>
                            <div class=" text-white rounded-full h-5 w-5 flex items-center justify-center bg-green absolute count-position">
                                2
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

        <!--        opacity background -->
        <transition name="fade">
            <div v-if="accountDrawer || mobileDrawer || cartDrawer" @click="toggleOpacity"
                 class="w-full h-screen fixed z-10 bg-black opacity-50"></div>
        </transition>

        <!--left screen mobile version-->
        <transition name="slide-left">
            <div v-if="mobileDrawer"
                 class="inset-y-0 left-0 fixed bg-white fixed z-20 shadow-md w-70  overflow-auto h-screen">
                <ul class="w-full py-6">L</ul>
                <div class="relative h-100 w-70">
                    <div class="py-3 px-10 text-xl text-center border-bottom font-l bg-gray_bg cursor-pointer">
                        <a @click="changeLocale(`en`)">EN </a> | <a
                            @click="changeLocale(`th`)"> TH</a>
                    </div>
                    <div class="py-3 px-10 text-xl border-bottom hover:bg-unHilight cursor-pointer">
                        <i @click="mobileDrawer =! mobileDrawer" class="material-icons text-2xl cursor-pointer absolute"
                           style="top:61px;left: 0px;font-size: 2.5rem;">keyboard_arrow_left</i>
                        Firstname Lastname
                    </div>
                    <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Order history
                    </div>
                    <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Personal
                        Detail
                    </div>
                    <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Address</div>
                    <div class="py-3 px-10 text-xl font-l hover:bg-unHilight cursor-pointer">Payment</div>
                    <div class="pb-3 pt-5 px-5 text-xl cursor-pointer bg-gray_bg">Product</div>
                    <div v-for="category in categorys" :key="category.id" class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">{{category.type}}
                    </div>
                    <div class="pb-3 pt-5 px-5 text-xl cursor-pointer bg-gray_bg"></div>
                    <div class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">
                        Log Out
                    </div>
                </div>
            </div>
        </transition>

        <!--cart screen-->
        <transition name="slide">
            <div v-if="cartDrawer" class="inset-y-0 right-0 bg-white fixed z-20 shadow-md">
                <ul class="w-full py-6">L</ul>
                <div class="relative h-full w-70 overflow-auto">
                    <div class="w-70 p-3 text-xl border-bottom fixed justify-between flex bg-white cursor-pointer">
                        <img class="w-8" src="../assets/icon/supermarket.svg">
                        <div class="text-white rounded-full h-5 w-5 flex items-center justify-center bg-green absolute count-position2">
                            2
                        </div>
                        My Cart
                        <i @click="cartDrawer = !cartDrawer" class="material-icons text-3xl cursor-pointer">keyboard_arrow_right</i>
                    </div>
                    <div class=" w-full">
                        <ul class="w-full" style="height: 3.5rem">L</ul>
                        <InCartItem/>
                        <InCartItem/>
                        <InCartItem/>
                        <InCartItem/>
                        <InCartItem/>
                        <InCartItem/>
                        <div class="w-full" style="height: 249px"></div>
                    </div>
                </div>
                <div class="fixed w-70 bottom-0  border-top p-2 bg-white z-50">
                    <div class="flex justify-between font-l">
                        <div class="">Subtotal</div>
                        <div>254 $</div>
                    </div>
                    <div class="flex justify-between font-l">
                        <div class="">Shipping</div>
                        <div>254 $</div>
                    </div>
                    <div class="flex justify-between font-l my-1">
                        <div class="">Coupon Code</div>
                        <div class="flex">
                            <input class="appearance-none border rounded-l-lg w-24 py-1 px-2 text-gray leading-tight focus:outline-none"
                                   id="username"
                                   type="text"/>
                            <div class="height1-85 bg-green rounded-r-lg" style="padding: 4px">
                                <i class="fas fa-check text-white"></i>
                            </div>
                        </div>
                    </div>
                    <div class="flex justify-between">
                        <div class="">Total</div>
                        <div>254 $</div>
                    </div>
                    <button class="w-full h-10 bg-orange mt-3 text-white flex justify-center">
                        <img width="25px" class="mx-3" src="../assets/icon/supermarket_white.svg">
                        Process to checkout
                    </button>
                </div>
            </div>
        </transition>

        <!--right screen-->
        <transition name="slide">
            <div v-if="accountDrawer" class="inset-y-0 right-0 bg-white fixed z-20 shadow-md">
                <ul class="w-full py-6">L</ul>
                <div class="relative h-100 w-70">
                    <div class="p-3 text-xl border-bottom justify-between flex hover:bg-unHilight cursor-pointer">
                        Firstname
                        Lastname
                        <i @click="accountDrawer = !accountDrawer" class="material-icons text-3xl cursor-pointer">keyboard_arrow_right</i>
                    </div>
                    <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Order history
                    </div>
                    <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Personal
                        Detail
                    </div>
                    <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Address</div>
                    <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Payment</div>
                    <div class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">
                        Log
                        Out
                    </div>
                </div>
            </div>
        </transition>

    </div>
</template>
<script>
    import i18n from "../plugins/i18n";
    import InCartItem from "./InCartItem";

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
                        {id: 0, type: "Fruits and Vegetables", color: "green"},
                        {id: 1, type: "Dry goods and Seasonings", color: "blue"},
                        {id: 2, type: "Rice Flour and Noodles", color: "yellow"},
                        {id: 3, type: "Condiments and Sauces", color: "red"},
                        {id: 4, type: "Normal and Alcoholic Beverages", color: "black"},
                        {id: 5, type: "Snack", color: "orange"},
                        {id: 6, type: "Frozen Products", color: "purple"},
                        {id: 7, type: "Other", color: "pink"},
                    ]
            }
        },
        methods: {
            goHome(){
              this.$router.push({
                  name:'HomePage'
              })
            },
            toggleOpacity() {
                this.accountDrawer = false
                this.cartDrawer = false
                this.mobileDrawer = false
            },
            changeLocale(locale) {
                i18n.locale = locale
            }
        }
    }
</script>

<style>

</style>
<style scoped>
    .border-bottom {
        border-bottom: 1px solid #707070
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