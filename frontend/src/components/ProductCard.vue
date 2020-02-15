<template>
    <div class="max-w-sm bg-white cs-border cursor-pointer">
        <div v-if="productData.quantity == 0" class="absolute bg-white w-full h-full opacity-50"></div>
        <div v-if="productData.quantity == 0" class="shadow-lg text-center text-red center absolute opacity-100 bg-white px-1 py-1">Out of Stock</div>
         <img @click="goDetail(productData.id)" v-if="productData.pic1 == null" class="w-4/6 object-cover mx-auto my-3"
             src="https://charliesfruitonline.com.au/wp-content/uploads/2014/03/green-cabbage.jpg"
             alt="Sunset in the mountains">
        <img @click="goDetail(productData.id)" v-else class="w-4/6 object-cover mx-auto my-3"
             :src="this.$store.state.endpoints.host+productData.pic1"
             alt="Sunset in the mountains">

        <div class="px-2 py-2">
            <div @click="goDetail(productData.id)" class="w-full text-left bg-white text-black py-2 h-24">
                {{productData.title}}
            </div>
            <div @click="goDetail(productData.id)" class="text-left text-md title text-green h-12"
                 :style="`color:${productData.category_color}`">
                {{productData.category_name}}
            </div>
            <a class="text-2xl ml-2">{{productData.price}} €</a>
            <a class="text-lightGray ml-2"> /piece</a>

            <!--            loading when start from 0-->
            <div v-if="countLoading == true"
                 class="button-area mx-auto flex justify-between mb-2 bg-green">
                <div class="text-xl" style="margin: auto">
                    <img src="../assets/icon/Rolling-1s-24px.svg">
                </div>
            </div>

            <!--            add and remove button show when item exist in cart-->
            <div @mouseover="hover = true"
                 @mouseleave="hover = false"
                 v-else-if="hover || count() > 0 || isInCart > -1"
                 class="button-area mx-auto flex justify-between mb-2">
                <div v-if="count() > 0" @click="decrease" class="button-increase  bg-green" style="user-select: none">
                    <i class="material-icons">remove</i>
                </div>
                <div v-else class="button-increase  bg-green" style="user-select: none;opacity: .5">
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
                 v-else-if="!hover && count() == 0"
                 class="button-area mx-auto flex justify-between mb-2" style="border: 1.5px solid #707070">
                <div class="text-xl" style="margin: auto">Add</div>
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
                countLoading: false
            }
        },
        created() {
            this.count()
            // console.log(this.$store.state.inCart[0])
            // this.isInCart = this.$store.state.inCart.findIndex(item => item.product.id == this.productData.id)
            // if (this.isInCart != -1) {
            //     this.value = this.$store.state.inCart[this.isInCart].quantity
            // }
        },
        methods: {
            goDetail(id) {
                this.$router.push({
                    name: 'Detail',
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
                            product_id: this.productData.id
                        }, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(() => {
                            axios.get(`http://${window.location.hostname}:8000/api/products/cart/`, {
                                headers: {
                                    Authorization: `JWT ${this.$store.state.jwt}`,
                                    'Content-Type': 'application/json'
                                },
                            }).then(res => {
                                this.itemIncart = res.data.data.cart_detail
                                this.$store.commit("setIncart", this.itemIncart);
                                this.countLoading = false
                            }).catch()
                        }).catch()
                    }, 2000)
                } else if (this.count() != this.quantity && this.$store.state.isAuthenticated == true) {
                    clearTimeout(this.timeout)
                    this.$store.state.inCart[this.isInCart].quantity++
                    this.timeout = setTimeout(() => {
                        axios.post(this.$store.state.endpoints.editInCart, {
                            quantity: this.$store.state.inCart[this.isInCart].quantity,
                            product_id: this.productData.id
                        }, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(res => {
                            this.$store.state.inCart[this.isInCart].quantity = res.data.data.quantity
                            this.$store.state.inCart[this.isInCart].price = res.data.data.price
                        }).catch()
                    }, 2000)
                } else if (this.$store.state.isAuthenticated == false) {
                    console.log("please login")
                }
            },
            decrease() {
                if (this.count() != 1) {
                    clearTimeout(this.timeout)
                    this.$store.state.inCart[this.isInCart].quantity--
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
                            this.$store.state.inCart[this.isInCart].quantity = res.data.data.quantity
                            this.$store.state.inCart[this.isInCart].price = res.data.data.price
                        }).catch()
                    }, 2000)
                } else if (this.count() == 1) {
                    clearTimeout(this.timeout)
                    axios.delete(this.$store.state.endpoints.editInCart + this.productData.id + "/", {
                        headers: {
                            Authorization: `JWT ${this.$store.state.jwt}`,
                            'Content-Type': 'application/json'
                        },
                    }).then(() => {
                        axios.get(`http://${window.location.hostname}:8000/api/products/cart/`, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(res => {
                            this.itemIncart = res.data.data.cart_detail
                            this.$store.commit("setIncart", this.itemIncart);
                            this.value = 0
                        }).catch()
                    }).catch()
                }
            },
            count() {
                this.isInCart = this.$store.state.inCart.findIndex(item => item.product.id == this.productData.id)
                if (this.isInCart != -1) {
                    this.oldQuantity = this.$store.getters.getCount[this.isInCart].quantity
                    return this.$store.getters.getCount[this.isInCart].quantity
                } else {
                    this.oldQuantity = 0
                    return 0
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

    .center {
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }
</style>