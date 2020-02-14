<template>
    <div class="max-w-sm bg-white cs-border cursor-pointer">
        {{count()}}
        <img class="w-4/6 object-cover mx-auto my-3"
             src="https://charliesfruitonline.com.au/wp-content/uploads/2014/03/green-cabbage.jpg"
             alt="Sunset in the mountains">
        <div class="px-2 py-2">
            <div @click="goDetail(productData.id)" class="w-full text-left bg-white text-black py-2 h-24">
                {{productData.title}}
            </div>
            <div class="text-left text-md title text-green h-12" :style="`color:${productData.category_color}`">
                {{productData.category_name}}
            </div>
            <a class="text-2xl ml-2">{{productData.price}} €</a>
            <a class="text-lightGray ml-2"> /piece</a>
            <div @mouseover="hover = true"
                 @mouseleave="hover = false"
                 v-if="hover || count() > 0 || isInCart > -1"
                 class="button-area mx-auto flex justify-between mb-2">
                <div @click="decrease" class="button-increase  bg-green">
                    <i class="material-icons">remove</i>
                </div>
                <div class="text-2xl">{{count()}}</div>
                <div @click="increase" class="button-decrease bg-green" style="user-select: none">
                    <i class="material-icons">add</i>
                </div>
            </div>
            <div @mouseover="hover = true"
                 @mouseleave="hover = false"
                 v-if="!hover && count() == 0"
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
                oldQuantity: 0
            }
        },
        created() {
            this.isInCart = this.$store.state.inCart.findIndex(item => item.product.id == this.productData.id)
            if (this.isInCart != -1) {
                this.value = this.$store.state.inCart[this.isInCart].quantity
            }
        },
        methods: {
            goDetail(id) {
                this.$router.push({
                    name: 'Detail',
                    params: {id: id}
                })
            },
            increase() {
                if (this.oldQuantity == 0) {
                    clearTimeout(this.timeout)
                    this.value++
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
                            }).catch()
                        }).catch()
                    }, 2000)
                } else if (this.count() != this.quantity) {
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
                        // console.log(res.status)
                        // let index = this.$store.state.inCart.findIndex(item => item.id == this.productData.id)
                        // this.$store.state.inCart.splice(index, 1)
                        axios.get(`http://${window.location.hostname}:8000/api/products/cart/`, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(res => {
                            this.itemIncart = res.data.data.cart_detail
                            this.$store.commit("setIncart", this.itemIncart);
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
</style>