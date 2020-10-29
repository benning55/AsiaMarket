<template>
    <div class="max-w-sm bg-white cs-border cursor-pointer">
        <div v-if="productData.quantity === 0 || productData.is_active === false" class="cursor-not-allowed">
            <div class="absolute bg-white w-full h-full opacity-50 "></div>
            <div class="shadow-lg text-center text-red center absolute opacity-100 bg-white px-1 py-1">
                {{$t('out_of_stock')}}
            </div>
        </div>

        <div @click="goDetail(productData.id)" v-if="(productData.pic1 == null) || imageError" class="w-4/6 mx-auto my-3"
             style="height: 155px">
            <svg style="width: 100%;height: 100%" xmlns="http://www.w3.org/2000/svg"
                 height="300px" width="300px"
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
        <img @click="goDetail(productData.id)" v-else class="w-4/6 object-contain mx-auto my-3" style="height: 155px"
             :src="this.$store.state.endpoints.host+productData.pic1"
             @error="printerror()"
             :alt="productData.title">

        <div class="px-2 py-2">
            <div @click="goDetail(productData.id)" class="w-full text-center bg-white text-black py-2 h-24">
                {{reduceLetter(nameTranslate(productData.title))}}
            </div>
            <div v-if="!(overStatee() === true && productData.quantity > 0)" @click="goDetail(productData.id)"
                 class="text-center text-md title text-green h-12"
                 :style="`color:${productData.category_color}`">
                {{nameTranslate(productData.category_name)}}
            </div>

            <div v-else @click="goDetail(productData.id)" class="text-center text-xl title text-red h-12">
                {{$t('not_enough')}}
            </div>

            <div v-if="overStatee() == true && productData.quantity > 0" class="flex">
                <a class="text-2xl ml-2 text-red">*</a>
                <a class="text-red ml-2 self-center">{{$t('left')}} : {{productData.quantity}}</a>
            </div>

            <!--            show this when not over-->

            <div v-else class="w-full text-center bg-white text-black py-2 text-2xl">
                {{productData.price}} €
            </div>

<!--            <div v-else class="">-->
<!--                <a class="text-2xl text-center">{{productData.price}} €</a>-->
<!--                &lt;!&ndash;                <a class="text-lightGray ml-2 self-center absolute" style="right: 8px"> /{{$t('')}}piece</a>&ndash;&gt;-->
<!--            </div>-->

            <!--            show this when over-->
            <div v-if="overStatee() == true && productData.quantity > 0"
                 class="button-option mx-auto flex justify-between mb-2">
                <div class="button-delete  bg-red" style="user-select: none;margin-right: 5px">
                    <i class='fas fa-trash-alt text-white text-sm'></i>
                </div>
                <div @click="changeOverState()" class="text-3xl bg-lightGray button-change" style="margin: auto">
                    <h1 style="margin-top: 8px">{{$t('change')}}</h1>
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
                 v-else-if="(hover || count() > 0 || isInCart > -1) && productData.quantity != 0"
                 class="button-area mx-auto flex justify-between mb-2">
                <div v-if="count() > 0" @click="decrease" class="button-increase  bg-green" style="user-select: none">
                    <i class="material-icons">remove</i>
                </div>
                <div v-else class="button-increase bg-green cursor-not-allowed" style="user-select: none;opacity: .5">
                    <i class="material-icons">remove</i>
                </div>
                <div class="text-2xl">{{count()}}</div>
                <!--                <input v-model="tmp" style="width: 50px;font-size: 10px">-->
                <div v-if="count() < this.quantity" @click="increase" class="button-decrease bg-green" style="user-select: none">
                    <i class="material-icons">add</i>
                </div>

                <div v-else class="button-decrease bg-green cursor-not-allowed" style="user-select: none;opacity: .5">
                    <i class="material-icons">add</i>
                </div>
            </div>

            <!--            show add when item not in cart-->
            <div @mouseover="hover = true"
                 @mouseleave="hover = false"
                 v-else-if="!hover && count() == 0 || productData.quantity == 0"
                 class="button-area mx-auto flex justify-between mb-2" style="border: 1.5px solid #707070">
                <div class="text-xl" style="margin: auto">{{$t('add')}}</div>
            </div>
        </div>
    </div>
</template>
<script>
    import axios from "axios";

    export default {
        props: [
            "productData"
        ],
        data() {
            return {
                hover: false,
                value: 0,
                timeout: null,
                quantity: this.productData.quantity,
                isInCart: false,
                oldQuantity: 0,
                countLoading: false,
                tmp: 0,
                overState: false,
                imageError:false
            }
        },
        created() {
            this.count()
        },
        methods: {
            printerror(){
                this.imageError = true
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
            reduceLetter(title) {
                if (title.length > 40) {
                    return title.substring(0, 40) + '...'
                } else {
                    return title
                }
            },
            changeOverState() {
                this.$store.state.inCart.cart_detail[this.isInCart].overStatus = false
                this.$store.state.inCart.cart_detail[this.isInCart].quantity = 1
                axios.post(this.$store.state.endpoints.editInCart, {
                    quantity: this.$store.state.inCart.cart_detail[this.isInCart].quantity,
                    product_id: this.productData.id
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
                        this.$message.error(this.$t('error_Oops_') + e.response.status);
                    }
                )
                this.overState = false
            },
            goDetail(id) {
                if (this.$route.name == 'Detail') {
                    this.$router.push({
                        name: 'Detail',
                        params: {id: id}
                    })
                    location.reload();
                } else {
                    this.$router.push({
                        name: 'Detail',
                        params: {id: id}
                    })
                }
            },
            increase() {
                if (this.oldQuantity == 0 && this.$store.state.isAuthenticated == true) {               // if start from 0 it not have any list in cart
                    this.countLoading = true
                    clearTimeout(this.timeout)
                    this.value++                          // value is mockup number
                    this.timeout = setTimeout(() => {
                        axios.post(this.$store.state.endpoints.editInCart, {
                            quantity: this.value,
                            product_id: this.productData.id
                        }, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(() => {
                            axios.get(this.$store.state.endpoints.cartAPI, {
                                headers: {
                                    Authorization: `JWT ${this.$store.state.jwt}`,
                                    'Content-Type': 'application/json'
                                },
                            }).then(res => {
                                this.itemIncart = res.data.data
                                this.$store.commit("setIncart", this.itemIncart);
                                this.countLoading = false
                            }).catch(e => {
                                    this.$message.error(this.$t('error_Oops_') + e.response.status + ', at increase product c1');
                                }
                            )
                        }).catch(
                            e => {
                                this.$message.error(this.$t('error_Oops_') + e.response.status + ', at increase product c1');
                            }
                        )
                    }, 2000)
                } else if (this.count() != this.quantity && this.$store.state.isAuthenticated == true) {
                    clearTimeout(this.timeout)
                    this.$store.state.inCart.cart_detail[this.isInCart].quantity++
                    this.timeout = setTimeout(() => {
                        axios.post(this.$store.state.endpoints.editInCart, {
                            quantity: this.$store.state.inCart.cart_detail[this.isInCart].quantity,
                            product_id: this.productData.id
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
                                this.$message.error(this.$t('error_Oops_') + e.response.status + ', at increase product c2');
                            }
                        )
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
                            product_id: this.productData.id
                        }, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(res => {
                            this.$store.state.inCart.cart_detail[this.isInCart].quantity = res.data.data.quantity
                            this.$store.state.inCart.cart_detail[this.isInCart].price = res.data.data.price
                        }).catch(e => {
                            this.$message.error(this.$t('error_Oops_') + e.response.status + ', at decrease product c1');
                        })

                    }, 2000)
                } else if (this.count() == 1) {
                    clearTimeout(this.timeout)
                    axios.delete(this.$store.state.endpoints.editInCart + this.productData.id + "/", {
                        headers: {
                            Authorization: `JWT ${this.$store.state.jwt}`,
                            'Content-Type': 'application/json'
                        },
                    }).then(() => {
                        axios.get(this.$store.state.endpoints.cartAPI, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(res => {
                            this.itemIncart = res.data.data
                            this.$store.commit("setIncart", this.itemIncart);
                            this.value = 0
                        }).catch(e => {
                            this.$message.error(this.$t('error_Oops_') + e.response.status + ', at increase product c2');
                        })
                    }).catch(e => {
                        this.$message.error(this.$t('error_Oops_') + e.response.status + ', at increase delete product c2');
                    })
                }
            },

            count() {
                this.isInCart = this.$store.state.inCart.cart_detail.findIndex(item => item.product.id == this.productData.id)
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
                this.isInCart = this.$store.state.inCart.cart_detail.findIndex(item => item.product.id == this.productData.id)
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

    .title {
        line-height: 1.5em;
        overflow: hidden;
    }

    .h-30 {
        height: 10rem;
    }

    .cs-border {
        border: 1px solid #e3e4e3;
        /*border-style: none solid none none*/
    }

    .button-area {
        border: 1.5px solid #619F21;
        width: 90%;
        height: 40px;
    }

    .button-option {
        width: 90%;
        height: 40px;
    }

    .button-change {
        font-size: 18px;
        text-align: center;
        width: 100%;
        height: 40px;
        /*padding-top: 5px;*/
    }

    .button-delete {
        color: white;
        font-size: 23px;
        text-align: center;
        width: 50px;
        height: 40px;
        /*padding-top: 5px;*/
    }

    .button-increase {
        color: white;
        font-size: 23px;
        text-align: center;
        width: 36px;
        padding-top: 5px;
    }

    .button-decrease {
        color: white;
        font-size: 23px;
        text-align: center;
        width: 36px;
        padding-top: 5px;
    }

    .center {
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }
</style>