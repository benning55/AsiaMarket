<template>
    <div class="h-24 p-2 border-bottom">
        <div class="parent">
            <div class="div1">
                <div class="" style="width: 90%">
                    <img src="https://charliesfruitonline.com.au/wp-content/uploads/2014/03/green-cabbage.jpg" alt="">
                </div>
            </div>
            <div class="div2">
                <div class="w-full" style="line-height: 20px;">{{reduceTitle(data.product.title)}}</div>
            </div>
            <div class="div3">
                <i class='fas fa-trash-alt m-2 text-lightGray'></i>
            </div>
            <div class="div4" style="padding-top: 9px">
                <div class="button-area flex justify-between cursor-pointer">
                    <div @click="decrease" class="button-increase  bg-green">
                        <i class="material-icons">remove</i>
                    </div>
                    <div class="text-lg">{{value}}</div>
                    <div @click="increase" class="button-decrease bg-green">
                        <i class="material-icons">add</i>
                    </div>
                </div>
            </div>
            <div class="div5" style="align-self: end">
                <div class="text-green">
                    123 $
                </div>
            </div>

        </div>
    </div>
</template>
<script>
    export default {
        name: 'InCartItem',
        props: ["data"],
        data() {
            return {
                value: 0,
                quantity: this.data.product.quantity
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
            increase() {
                if (this.value != this.quantity) {
                    clearTimeout(this.timeout)
                    this.value++
                    this.timeout = setTimeout(() => {
                        console.log(this.value)
                    }, 2000)
                }
            },
            decrease() {
                if (this.value != 0) {
                    clearTimeout(this.timeout)
                    this.value--
                    this.timeout = setTimeout(() => {
                        console.log(this.value)
                    }, 2000)
                }
            }
        }
    }
</script>

<style scoped>
    .border-bottom {
        border-bottom: 1px solid #707070
    }

    .button-area {
        border: 1.5px solid #619F21;
        width: 70%;
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
        grid-area: 2 / 2 / 3 / 6;
    }

    .div5 {
        grid-area: 2 / 6 / 3 / 7;
    }
</style>