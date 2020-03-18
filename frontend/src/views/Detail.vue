<template>
    <div>
        <Loader v-if="isLoading"/>
        <ul class="w-full py-6">
            <li class="inline-block px-5">|</li>
        </ul>
        <section class="bg-white p-5 my-5">
            <a><span @click="goHome" class="hover:text-green cursor-pointer">{{$t('home')}}</span> / <span
                    @click="goCategory(dataProduct.category_id)" class="hover:text-green cursor-pointer">{{dataProduct.category_name}}</span>
                / {{nameTranslate(dataProduct.title)}}</a>
        </section>
        <section class="my-5 mb-10">
            <div class="flex-none sm:flex md:flex lg:flex xl:flex mb-4 bg-white">
                <div class="w-full sm:w-3/12 md:4/12 lg:4/12">
                    <VueSlickCarousel
                            ref="c1"
                            :asNavFor="$refs.c2"
                            :focusOnSelect="true"
                            :dots="false"
                            :arrows="false"
                            :infinite="false">

                        <div v-if="(dataProduct.pic1 == null) || imageError" class="w-full p-10 md:p-5">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                 height="100%" width="100%"
                                 version="1.1"
                                 viewBox="-300 -300 600 600"
                                 font-family="Kanit"
                                 font-size="72"
                                 text-anchor="middle">

                                <circle stroke="#AAA" stroke-width="10" r="280" fill="#FFF"/>
                                <text style="fill:#444;">
                                    <tspan x="0" y="-8">{{$t('NO_IMAGE')}}</tspan>
                                    <tspan x="0" y="80">{{$t('AVAILABLE')}}</tspan>
                                </text>
                            </svg>
                        </div>
                        <div v-else class="w-full p-10 md:p-5">
                            <img @error="imgError()" class="height220"
                                 :src="$store.state.endpoints.host+dataProduct.pic1" alt="saa">
                        </div>

                        <div v-if="dataProduct.pic2 != null" class="w-full p-10 md:p-5">
                            <img class="height220" :src="$store.state.endpoints.host+dataProduct.pic2" alt="s">
                        </div>
                        <div v-if="dataProduct.pic3 != null" class="w-full p-10 md:p-5">
                            <img class="height220" :src="$store.state.endpoints.host+dataProduct.pic3" alt="s">
                        </div>
                    </VueSlickCarousel>
                    <div class="px-5">
                        <VueSlickCarousel ref="c2"
                                          :asNavFor="$refs.c1"
                                          :focusOnSelect="true"
                                          :arrows="true"
                                          :slidesToShow="3"
                                          :infinite="false">
                            <div v-if="(dataProduct.pic1 == null) || imageError" class="w-full p-2 md:p-2">
                                <svg xmlns="http://www.w3.org/2000/svg"
                                     height="100%" width="100%"
                                     version="1.1"
                                     viewBox="-300 -300 600 600"
                                     font-family="Kanit"
                                     font-size="72"
                                     text-anchor="middle">

                                    <circle stroke="#AAA" stroke-width="10" r="280" fill="#FFF"/>
                                    <text style="fill:#444;">
                                        <tspan x="0" y="-8">{{$t('NO_IMAGE')}}</tspan>
                                        <tspan x="0" y="80">{{$t('AVAILABLE')}}</tspan>
                                    </text>
                                </svg>
                            </div>
                            <div v-else class="w-full p-2 md:p-2">
                                <img class="height80" :src="$store.state.endpoints.host+dataProduct.pic1" alt="s">
                            </div>
                            <div v-if="dataProduct.pic2 != null" class="w-full p-2 md:p-2">
                                <img class="height80"
                                     :src="$store.state.endpoints.host+dataProduct.pic2"
                                     alt="s">
                            </div>
                            <div v-if="dataProduct.pic3 != null" class="w-full p-2 md:p-2">
                                <img class="height80"
                                     :src="$store.state.endpoints.host+dataProduct.pic3"
                                     alt="s">
                            </div>
                        </VueSlickCarousel>
                    </div>
                </div>
                <div class="w-full sm:w-5/12 md:5/12 lg:md:5/12 px-10 pt-12">
                    <h1 class="text-3xl">{{nameTranslate(dataProduct.title)}}</h1>
                    <!--                    <h1 class="text-lightGray">unit</h1>-->
                    <p class="mt-10"> {{dataProduct.description}}</p>
                </div>
                <div class="w-full sm:w-4/12 px-10 pt-12">
                    <h1 class="text-4xl">{{dataProduct.price}} $</h1>

                    <!--            show this when over-->
                    <div v-if="overStatee() == true && dataProduct.quantity > 0"
                         class="button-option mx-auto flex justify-between mb-2">
                        <div class="button-delete  bg-red" style="user-select: none;margin-right: 5px">
                            <i class='fas fa-trash-alt text-white text-sm'></i>
                        </div>
                        <div @click="changeOverState()" class="text-3xl bg-lightGray button-change"
                             style="margin: auto">
                            {{$t('change')}}
                        </div>
                    </div>

                    <!--            loading when start from 0-->
                    <div v-else-if="countLoading == true"
                         class="button-area mx-auto flex justify-between mb-2 bg-green">
                        <div class="text-xl" style="margin: auto">
                            <img src="../assets/icon/Rolling-1s-24px.svg">
                        </div>
                    </div>

                    <!--            add and remove button show when item exist in cart-->
                    <div @mouseover="hover = true"
                         @mouseleave="hover = false"
                         v-else-if="(hover || count() > 0 || isInCart > -1) && dataProduct.quantity > 0"
                         class="button-area mx-auto flex justify-between mb-2">
                        <div @click="decrease" class="button-increase  bg-green" style="user-select: none">
                            <i class="material-icons">remove</i>
                        </div>
                        <div class="text-2xl">{{count()}}</div>
                        <div @click="increase" class="button-decrease bg-green" style="user-select: none">
                            <i class="material-icons">add</i>
                        </div>
                    </div>

                    <!--            show add when item not in cart-->
                    <div @mouseover="hover = true"
                         @mouseleave="hover = false"
                         v-else-if="!hover && count() == 0 && dataProduct.quantity > 0"
                         class="button-area mx-auto flex justify-between mb-2" style="border: 1.5px solid #707070">
                        <div class="text-xl" style="margin: auto">{{$t('add')}}</div>
                    </div>

                    <!--            show add when no item not in cart-->
                    <div v-else-if="!hover && dataProduct.quantity == 0"
                         class="button-area mx-auto flex justify-between mb-2" style="border: 1.5px solid #707070">
                        <div class="text-xl text-red" style="margin: auto">{{$t('out_of_stock')}}</div>
                    </div>

                    <h1 v-if="dataProduct.quantity > 0" class="text-lightGray my-5">{{$t('left')}} :
                        {{dataProduct.quantity}}</h1>
                    <h1 v-else class="text-red my-5">{{$t('left')}} : {{dataProduct.quantity}}</h1>
                </div>
            </div>
        </section>

        <section class="mt-3">
            <h1 class="mb-2 text-xl">{{$t('you_may_also_like')}}</h1>
            <SwiperItem :dataItem="recommendProduct"/>
        </section>
    </div>
</template>

<script>
    import VueSlickCarousel from 'vue-slick-carousel'
    import 'vue-slick-carousel/dist/vue-slick-carousel.css'
    import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
    import axios from "axios";
    import SwiperItem from "../components/SwiperItem";
    import Loader from "../components/Loader";

    export default {
        name: 'Detail',
        components: {
            VueSlickCarousel,
            Loader,
            SwiperItem
        },
        data() {
            return {
                setting3: {
                    "dots": false,
                    "infinite": false,
                    "initialSlide": 3,
                    "speed": 500,
                    "slidesToShow": 3,
                    "slidesToScroll": 1,
                    "arrows": false,
                    "swipeToSlide": true,
                    "responsive": [
                        {
                            "breakpoint": 1400,
                            "settings": {
                                "slidesToShow": 3,
                            }
                        },
                        {
                            "breakpoint": 1024,
                            "settings": {
                                "slidesToShow": 3,
                            }
                        },
                        {
                            "breakpoint": 600,
                            "settings": {
                                "slidesToShow": 3,
                            }
                        },
                        {
                            "breakpoint": 480,
                            "settings": {
                                "slidesToShow": 2,
                            }
                        }
                    ]
                },
                hover: false,
                recommendProduct: [],
                dataProduct: [],
                swiperOption: {
                    slidesPerView: 5,
                    pagination: {
                        el: '.swiper-pagination',
                        clickable: true
                    },
                    breakpoints: {
                        1400: {
                            slidesPerView: 4,
                        },
                        1024: {
                            slidesPerView: 4,
                        },
                        640: {
                            slidesPerView: 3,
                        },
                        480: {
                            slidesPerView: 2,
                        }
                    }
                },
                countLoading: false,
                isInCart: false,
                value: 0,
                overState: false,
                isLoading: false,
                imageError: false
            }
        },
         created() {
            this.isLoading = true
            // get detail of product
            axios.get(this.$store.state.endpoints.productUrL + this.$route.params.id + "/").then(res => {
                this.dataProduct = res.data.data
                this.isLoading = false
            }).catch(e => {
                this.isLoading = false
                this.$message.error(this.$t('error_Oops_') + e.status);
            })

            // get recommend product
            axios.get(this.$store.state.endpoints.recommendProduct).then(res => {
                this.recommendProduct = res.data.data.slice(0, 8)
                this.isLoading = false
            }).catch(e => {
                this.isLoading = false
                this.$message.error(this.$t('error_Oops_') + e.status);
            })

            this.isInCart = this.$store.state.inCart.cart_detail.findIndex(item => item.product.id == this.dataProduct.id)
            if (this.isInCart != -1) {
                this.value = this.$store.state.inCart.cart_detail[this.isInCart].quantity
            }
        },
        methods: {
            imgError() {
                this.imageError = true
            },
            nameTranslate(text) {
                let list = text.split(')').join('(').split('(')
                if (list.length == 1) {
                    document.title = text
                    return text
                } else {
                    if (this.$i18n.locale == 'th') {
                        document.title = list[1]
                        return list[1]
                    } else {
                        document.title = list[0]
                        return list[0]
                    }
                }
            },
            changeOverState() {
                this.$store.state.inCart.cart_detail[this.isInCart].overStatus = false
                this.$store.state.inCart.cart_detail[this.isInCart].quantity = 1
                axios.post(this.$store.state.endpoints.editInCart, {
                    quantity: this.$store.state.inCart.cart_detail[this.isInCart].quantity,
                    product_id: this.dataProduct.id
                }, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                }).then(res => {
                    this.$store.state.inCart.cart_detail[this.isInCart].quantity = res.data.data.quantity
                    this.$store.state.inCart.cart_detail[this.isInCart].price = res.data.data.price
                }).catch(
                    e => {
                        this.$message.error(this.$t('error_Oops_') + e.status);
                    }
                )
                this.overState = false
            },
            goHome() {
                this.$router.push({
                    name: 'HomePage'
                })
            },
            goCategory(id) {
                this.$router.push({
                    name: 'Category',
                    params: {id: id}
                })
            },
            increase() {
                if (this.oldQuantity == 0 && this.$store.state.isAuthenticated == true) {               // if start from 0 it not have any list in cart
                    this.countLoading = true
                    clearTimeout(this.timeout)
                    this.value++                          // value is mockup number
                    this.timeout = setTimeout(() => {
                        axios.post(this.$store.state.endpoints.editInCart, {
                            quantity: this.value,
                            product_id: this.dataProduct.id
                        }, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(() => {
                            axios.get(`${this.$store.state.endpoints.host}/api/products/cart/`, {
                                headers: {
                                    Authorization: `JWT ${this.$store.state.jwt}`,
                                    'Content-Type': 'application/json'
                                },
                            }).then(res => {
                                this.itemIncart = res.data.data
                                this.$store.commit("setIncart", this.itemIncart);
                                this.countLoading = false
                            }).catch(e => {
                                this.$message.error(this.$t('error_Oops_') + e.status + ', at increase c1');
                            })
                        }).catch(e => {
                            this.$message.error(this.$t('error_Oops_') + e.status + ', at increase c1');
                        })
                    }, 2000)
                } else if (this.count() != this.dataProduct.quantity && this.$store.state.isAuthenticated == true) {
                    clearTimeout(this.timeout)
                    this.$store.state.inCart.cart_detail[this.isInCart].quantity++
                    this.timeout = setTimeout(() => {
                        axios.post(this.$store.state.endpoints.editInCart, {
                            quantity: this.$store.state.inCart.cart_detail[this.isInCart].quantity,
                            product_id: this.dataProduct.id
                        }, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(res => {
                            this.$store.state.inCart.cart_detail[this.isInCart].quantity = res.data.data.quantity
                            this.$store.state.inCart.cart_detail[this.isInCart].product.quantity = res.data.data.product.quantity
                            this.$store.state.inCart.cart_detail[this.isInCart].price = res.data.data.price
                        }).catch(e => {
                            this.$message.error(this.$t('error_Oops_') + e.status + ', at increase c2');
                        })
                    }, 2000)
                } else if (this.$store.state.isAuthenticated == false) {
                    this.$alert(this.$t('please_login_message'),this.$t('please_login'), {
                        confirmButtonText: this.$t('login'),
                        callback: action => {
                            if (action == 'confirm') {
                                this.$router.push({
                                    name: 'login'
                                })
                            }
                        }
                    });
                }
            },
            decrease() {
                if (this.count() != 1) {
                    clearTimeout(this.timeout)
                    this.$store.state.inCart.cart_detail[this.isInCart].quantity--
                    this.timeout = setTimeout(() => {
                        axios.post(this.$store.state.endpoints.editInCart, {
                            quantity: this.count(),
                            product_id: this.dataProduct.id
                        }, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(res => {
                            this.$store.state.inCart.cart_detail[this.isInCart].quantity = res.data.data.quantity
                            this.$store.state.inCart.cart_detail[this.isInCart].price = res.data.data.price
                        }).catch(e => {
                            this.$message.error(this.$t('error_Oops_') + e.status + ', at decrease c1');
                        })
                    }, 2000)
                } else if (this.count() == 1) {
                    clearTimeout(this.timeout)
                    axios.delete(this.$store.state.endpoints.editInCart + this.dataProduct.id + "/", {
                        headers: {
                            Authorization: `JWT ${this.$store.state.jwt}`,
                            'Content-Type': 'application/json'
                        },
                    }).then(() => {
                        axios.get(`${this.$store.state.endpoints.host}/api/products/cart/`, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(res => {
                            this.itemIncart = res.data.data
                            this.$store.commit("setIncart", this.itemIncart);
                            this.value = 0
                        }).catch(e => {
                            this.$message.error(this.$t('error_Oops_') + e.status + ', at decrease c2');
                        })
                    }).catch(e => {
                            this.$message.error(this.$t('error_Oops_') + e.status + ', at decrease c2');
                        }
                    )
                }
            },
            count() {
                this.isInCart = this.$store.state.inCart.cart_detail.findIndex(item => item.product.id == this.dataProduct.id)
                if (this.isInCart != -1) {
                    if (this.$store.state.inCart.cart_detail[this.isInCart].overStatus) {
                        this.overState = true
                        return 1
                    } else {
                        this.overState = false
                        this.oldQuantity = this.$store.getters.getCount[this.isInCart].quantity
                        this.tmp = this.$store.getters.getCount[this.isInCart].quantity
                        return this.$store.getters.getCount[this.isInCart].quantity
                    }
                } else {
                    this.oldQuantity = 0
                    this.value = 0
                    return 0
                }
            },

            overStatee() {
                this.isInCart = this.$store.state.inCart.cart_detail.findIndex(item => item.product.id == this.dataProduct.id)
                if (this.isInCart != -1) {
                    if (this.$store.state.inCart.cart_detail[this.isInCart].overStatus) {
                        this.overState = true
                        return this.$store.state.inCart.cart_detail[this.isInCart].overStatus
                    } else {
                        this.overState = false
                        return false
                    }
                } else {
                    return false
                }
            }
        },
    }
</script>

<style scoped>
    .slick-slide.slick-active.slick-cloned {
        display: none;
    }

    .height220 {
        height: 220px;
        margin: auto;
        object-fit: contain;
    }

    .height80 {
        height: 80px;
        margin: auto;
        object-fit: contain;
    }

    .button-area {
        border: 1.5px solid #619F21;
        width: 100%;
        height: 40px;
    }

    .button-increase {
        color: white;
        font-size: 23px;
        text-align: center;
        width: 36px;
        height: 37px;
        padding-top: 5px;
    }

    .button-decrease {
        color: white;
        font-size: 23px;
        text-align: center;
        width: 36px;
        height: 37px;
        padding-top: 5px;
    }

    .button-change {
        font-size: 18px;
        text-align: center;
        width: 100%;
        height: 40px;
        padding-top: 5px;
    }

    .button-delete {
        color: white;
        font-size: 23px;
        text-align: center;
        width: 50px;
        height: 40px;
        padding-top: 5px;
    }

    /*.slick-slider[data-v-6bed67a2] {*/
    /*    max-height: 330px;*/
    /*}*/

</style>