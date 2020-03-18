<template>
    <div class="h-24 p-2 border-bottom"
         @focusout="handleFocusOut"
         tabindex="0">

        <div v-if="!isWillDelete && this.data.overStatus && quantity > 0" class="parent" style="height: 80px">
            <div class="div1 self-center">
                <div class="relative" style="width: 90%">
                    <img :src="$store.state.endpoints.host+data.product.pic1" alt=""
                         style="max-height: 80px;margin: auto;opacity: .2">
                    <a class="center text-red text-center absolute">{{$t('not_enough')}}</a>
                </div>
            </div>
            <div class="div2">
                <div class="w-full" style="line-height: 20px;">{{reduceTitle(data.product.title)}}</div>
            </div>
            <div class="div3" style="align-self: flex-start;text-align: right;">
                <i @click="isWillDelete=true" class='fas fa-trash-alt m-2 text-lightGray cursor-pointer'></i>
            </div>
            <div class="div4">
                <div @click="changeOverState()" class="button-change cursor-pointer bg-lightGray text-center">
                    {{$t('change')}}
                </div>
            </div>
            <div class="div5" style="align-self: end">
                <div class="text-green" style="text-align: end;margin-right: 8px;">
                    --
                </div>
            </div>
        </div>

        <div v-else-if="!isWillDelete && quantity > 0" class="parent" style="height: 80px">
            <div class="div1 self-center">
                <div class="" style="width: 90%">
                    <img :src="$store.state.endpoints.host+data.product.pic1" alt=""
                         style="max-height: 80px;margin: auto">
                </div>
            </div>
            <div class="div2">
                <div class="w-full" style="line-height: 20px;">{{reduceTitle(data.product.title)}}</div>
            </div>
            <div class="div3" style="align-self: flex-start;text-align: right;">
                <i @click="isWillDelete=true" class='fas fa-trash-alt m-2 text-lightGray cursor-pointer'></i>
            </div>
            <div class="div4">
                <div class="button-area flex justify-between cursor-pointer">
                    <div @click="decrease" class="button-increase  bg-green" style="user-select: none">
                        <i class="material-icons">remove</i>
                    </div>
                    <div class="text-lg">{{value}}</div>
                    <div @click="increase" class="button-decrease bg-green" style="user-select: none">
                        <i class="material-icons">add</i>
                    </div>
                </div>
            </div>
            <div class="div5" style="align-self: end">
                <div class="text-green" style="text-align: end;margin-right: 8px;">
                    {{data.price}} €
                </div>
            </div>
        </div>

        <div v-else-if="!isWillDelete && quantity == 0" class="parent" style="height: 80px">
            <div class="div1 self-center">
                <div class="" style="width: 90%">
                    <img :src="$store.state.endpoints.host+data.product.pic1" alt=""
                         style="max-height: 80px;margin: auto">
                </div>
            </div>
            <div class="div2">
                <div class="w-full" style="line-height: 20px;">{{reduceTitle(data.product.title)}}</div>
            </div>
            <div class="div3" style="align-self: flex-start;text-align: right;">
                <i @click="isWillDelete=true" class='fas fa-trash-alt m-2 text-lightGray cursor-pointer'></i>
            </div>
            <div class="div4">
                <div class="text-lg text-red">{{$t('out_of_stock')}}</div>
            </div>
            <div class="div5" style="align-self: end">
                <div class="text-green" style="text-align: end;margin-right: 8px;">
                    --
                </div>
            </div>
        </div>


        <div v-else class="parent2" style="height: fit-content">
            <div @click="deleteItem" class="div22 bg-red text-white text-center w-full h-20 cursor-pointer">
                <p>{{$t('delete')}}</p>
            </div>
            <div @click="isWillDelete=false"
                 class="div12 text-black text-center w-full h-20 cursor-pointer hover:bg-unHilight">
                <p>{{$t('cancel')}}</p>
            </div>

        </div>
    </div>
</template>
<script>
    import axios from "axios";

    export default {
        name: 'InCartItem',
        props: ["data"],
        data() {
            return {
                value: this.data.quantity,
                quantity: this.data.product.quantity,
                isWillDelete: false,
                itemStatus: 'ok'
            }
        },
        methods: {
            reduceTitle(title) {
                if (title.length > 30) {
                    return title.substring(0, 30) + "...."
                } else {
                    return title
                }
            },
            handleFocusOut() {
                this.isWillDelete = false
            },
            increase() {
                if (this.value < this.quantity) {
                    clearTimeout(this.timeout)
                    this.value++
                    this.timeout = setTimeout(() => {
                        axios.post(this.$store.state.endpoints.editInCart, {
                            quantity: this.value,
                            product_id: this.data.product.id
                        }, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(res => {
                            this.quantity = res.data.data.product.quantity
                            let index = this.$store.state.inCart.cart_detail.findIndex(item => item.id == res.data.data.id)
                            this.$store.state.inCart.cart_detail[index].quantity = res.data.data.quantity
                            this.$store.state.inCart.cart_detail[index].price = res.data.data.price
                        }).catch(e => {
                            this.$message.error(this.$t('error_Oops_') + e.status);
                        })
                    }, 2000)
                } else {
                    this.value = this.quantity
                }
            },
            decrease() {
                if (this.value > 1) {
                    clearTimeout(this.timeout)
                    this.value--
                    this.timeout = setTimeout(() => {
                        axios.post(this.$store.state.endpoints.editInCart, {
                            quantity: this.value,
                            product_id: this.data.product.id
                        }, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(res => {
                            let index = this.$store.state.inCart.cart_detail.findIndex(item => item.id == res.data.data.id)
                            this.$store.state.inCart.cart_detail[index].quantity = res.data.data.quantity
                            this.$store.state.inCart.cart_detail[index].price = res.data.data.price
                        }).catch(e => {
                            this.$message.error(this.$t('error_Oops_') + e.status + 'at decrease product');
                        })
                    }, 2000)
                }
            },
            changeOverState() {
                let isInCart = this.$store.state.inCart.cart_detail.findIndex(item => item.product.id == this.data.product.id)
                this.$store.state.inCart.cart_detail[isInCart].overStatus = false
                this.$store.state.inCart.cart_detail[isInCart].quantity = 1
                this.value = 1
                axios.post(this.$store.state.endpoints.editInCart, {
                    quantity: this.$store.state.inCart.cart_detail[isInCart].quantity,
                    product_id: this.data.product.id
                }, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                }).then(res => {
                    this.$store.state.inCart.cart_detail[isInCart].quantity = res.data.data.quantity
                    this.$store.state.inCart.cart_detail[isInCart].price = res.data.data.price
                }).catch(
                    e => {
                            this.$message.error('Oops, Something is Error. code ' + e.status + 'at change state');
                        }
                )
                this.overState = false
            },
            deleteItem() {
                axios.delete(this.$store.state.endpoints.editInCart + this.data.product.id + "/", {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                }).then(() => {
                    // console.log(res.status)
                    let index = this.$store.state.inCart.cart_detail.findIndex(item => item.id == this.data.id)
                    this.$store.state.inCart.cart_detail.splice(index, 1)
                }).catch(e => {
                            this.$message.error('Oops, Something is Error. code ' + e.status + 'at delete product');
                        })
            }
        },
        computed: {
            // isOver(){
            //     if(this.data.quantity > this.data.product.quantity){}
            // }
        }
    }
</script>

<style scoped>
    .center {
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }

    .border-bottom {
        border-bottom: 1px solid #707070
    }

    .button-change {
        font-size: 18px;
        text-align: center;
        width: 100%;
        height: 40px;
        padding-top: 5px;
    }

    .button-area {
        margin-top: 6px;
        border: 1.5px solid #619F21;
        width: 90%;
        height: 28px;
    }

    .button-increase {
        color: white;
        font-size: 20px;
        text-align: center;
        width: 26px;
        height: 25px;
        /*padding-top: 5px;*/
    }

    .button-decrease {
        color: white;
        font-size: 20px;
        text-align: center;
        width: 26px;
        height: 25px;
        /*padding-top: 5px;*/
    }

    .parent {
        display: grid;
        grid-template-columns: 2fr repeat(5, 1fr);
        grid-template-rows: repeat(2, 1fr);
        grid-column-gap: 0px;
        grid-row-gap: 0px;
    }

    .div1 {
        grid-area: 1 / 1 / 3 / 2;
    }

    .div2 {
        grid-area: 1 / 2 / 2 / 6;
    }

    .div3 {
        grid-area: 1 / 6 / 2 / 7;
    }

    .div4 {
        grid-area: 2 / 2 / 3 / 5;
    }

    .div5 {
        grid-area: 2 / 5 / 3 / 7;
    }

    .parent2 {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        grid-template-rows: repeat(2, 1fr);
        grid-column-gap: 0px;
        grid-row-gap: 0px;
    }

    .div12 {
        padding: 28px 0px 28px 0px;
        grid-area: 1 / 3 / 3 / 8;

    }

    .div22 {
        padding: 28px 0px 28px 0px;
        grid-area: 1 / 1 / 3 / 3;
    }
</style>