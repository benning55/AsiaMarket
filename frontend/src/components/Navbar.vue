<template>
    <div>
        <nav class="shadow-lg flex items-center justify-between flex-wrap bg-white py-6 fixed w-full z-50">
            <ul class="w-full">
                <li class="inline-block px-5">LOGO</li>
                <li class="float-right px-5 flex-grow"><a @click="changeLocale(`en`)">EN </a> | <a
                        @click="changeLocale(`th`)"> TH</a>
                </li>
            </ul>
        </nav>
        <div class="inset-y-0 left-0 bg-gray fixed">
            <div class="container px-5">
                <ul class="mt-24">
                    <li class="mb-4">ddd</li>
                    <li class="mb-1">ddd</li>
                    <li class="mb-1">ddd</li>
                    <li class="mb-4">ddd</li>
                    <li class="mb-1">ddd</li>
                    <li class="mb-1">ddd</li>
                    <li class="mb-1">ddd</li>
                </ul>
            </div>
        </div>
        <div class="inset-y-0 right-0 fixed">
            <div class="container">
                <div class="vertical-center">
                    <div class="shadow-md">
                        <div class="w-20 bg-white hover:bg-unHilight py-3 rounded-tl-lg border-bottom cursor-pointer">
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
        <div v-if="accountDrawer || mobileDrawer" @click="toggleOpacity"
             class="w-full h-screen fixed z-10 bg-black opacity-50"></div>

        <!--left screen-->
        <div v-if="mobileDrawer" class="inset-y-0 left-0 fixed bg-white fixed z-20 shadow-md w-70  overflow-auto h-screen">
            <ul class="w-full py-6">L</ul>
            <div class="relative h-100 w-70">
                <div class="py-3 px-10 text-xl border-bottom hover:bg-unHilight cursor-pointer">
                    <i @click="mobileDrawer =! mobileDrawer" class="material-icons text-2xl cursor-pointer absolute"
                       style="top:7px;left: 0px;font-size: 2.5rem;">keyboard_arrow_left</i>
                    Firstname Lastname
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Order history
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Personal Detail
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Address</div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Payment</div>
                <div class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">Log
                    Out
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Order history
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Personal Detail
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Address</div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Payment</div>
                <div class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">Log
                    Out
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Order history
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Personal Detail
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Address</div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Payment</div>
                <div class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">Log
                    Out
                </div>
            </div>
        </div>

        <!--right screen-->
        <div v-if="accountDrawer" class="inset-y-0 right-0 bg-white fixed z-20 shadow-md">
            <ul class="w-full py-6">L</ul>
            <div class="relative h-100 w-70">
                <div class="p-3 text-xl border-bottom justify-between flex hover:bg-unHilight cursor-pointer">Firstname
                    Lastname
                    <i @click="accountDrawer = !accountDrawer" class="material-icons text-3xl cursor-pointer">keyboard_arrow_right</i>
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Order history
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Personal Detail
                </div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Address</div>
                <div class="py-3 px-10 text-xl border-bottom font-l hover:bg-unHilight cursor-pointer">Payment</div>
                <div class="py-3 px-10 text-xl border-bottom font-l text-orange hover:bg-unHilight cursor-pointer">Log
                    Out
                </div>
            </div>
        </div>

    </div>
</template>
<script>
    import i18n from "../plugins/i18n";

    export default {
        name: "Navbar",
        data() {
            return {
                accountDrawer: false,
                cartDrawer: false,
                mobileDrawer: true
            }
        },
        methods: {
            toggleOpacity(){
                this.accountDrawer= false,
                this.cartDrawer= false,
                this.mobileDrawer= false
            },
            changeLocale(locale) {
                i18n.locale = locale
            }
        }
    }
</script>

<style scoped>
    .font-l {
        font-family: kanit light;
    }

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
</style>