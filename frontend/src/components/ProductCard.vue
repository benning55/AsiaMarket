<template>
    <div class="max-w-sm bg-white cs-border cursor-pointer" @click="goDetail(productData.id)">
        <img class="w-4/6 object-cover mx-auto my-3"
             src="https://charliesfruitonline.com.au/wp-content/uploads/2014/03/green-cabbage.jpg"
             alt="Sunset in the mountains">
        <div class="px-2 py-2">
            <div class="w-full text-left bg-white text-black py-2 h-24">
                {{productData.title}}
            </div>
            <div class="text-left text-md title text-green h-12" :style="`color:${productData.category_color}`">
                {{productData.category_name}}
            </div>
<!--            <a class="text-lightGray line-through ml-2">60</a>-->
            <a class="text-2xl ml-2">{{productData.price}} €</a>
            <a class="text-lightGray ml-2"> /piece</a>
            <div @mouseover="hover = true"
                 @mouseleave="hover = false"
                 v-if="hover"
                 class="button-area mx-auto flex justify-between mb-2">
                <div class="button-increase  bg-green">
                    <i class="material-icons">remove</i>
                </div>
                <div class="text-2xl">2</div>
                <div class="button-decrease bg-green">
                    <i class="material-icons">add</i>
                </div>
            </div>
            <div @mouseover="hover = true"
                 @mouseleave="hover = false"
                 v-if="!hover"
                 class="button-area mx-auto flex justify-between mb-2" style="border: 1.5px solid #707070">
                <div class="text-xl" style="margin: auto">Add</div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        props: [
            "productData"
        ],
        data() {
            return {
                hover: false
            }
        },
        methods:{
            goDetail(id){
                this.$router.push({
                    name:'Detail',
                    params:{id:id}
                })
            }
        }
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