<template>
    <div class="h-24 p-2 border-bottom">
        <div class="flex mb-4">
            <div class="w-32">
                <img src="https://charliesfruitonline.com.au/wp-content/uploads/2014/03/green-cabbage.jpg" alt="">
            </div>
            <div class=" ml-2">
                <div class="h-12 flex">
                    <div class="w-full" style="line-height: 18px;">Name eeeeeee eeeeee eeee eee eee eeeeeexx</div>
                    <i class='fas fa-trash-alt m-2 text-lightGray'></i>
                </div>
                <div class="flex justify-between">
                    <div class="button-area flex justify-between">
                        <div class="button-increase  bg-green">
                            <i class="material-icons">remove</i>
                        </div>
                        <div class="text-lg">2</div>
                        <div class="button-decrease bg-green">
                            <i class="material-icons">add</i>
                        </div>
                    </div>
                    <div class="text-green">
                        123 $
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'InCartItem'
    }
</script>

<style scoped>
    .border-bottom {
        border-bottom: 1px solid #707070
    }

    .button-area {
        border: 1.5px solid #619F21;
        width: 50%;
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
</style>