<template>
    <div class="flex justify-between">
                <img style="max-width: 130px;" class="my-3 w-1/3 sm:w-1/3"
                     src="https://charliesfruitonline.com.au/wp-content/uploads/2014/03/green-cabbage.jpg">
                <div class=" my-3 ml-2 w-2/3 self-center">
                    <div class="flex justify-between">
                        <h1>Order Number</h1>
                        <h1>{{orderdata.id}}</h1>
                    </div>
                    <div class="flex justify-between">
                        <h1>Total</h1>
                        <h1>{{orderdata.total_price}}</h1>
                    </div>
                    <div class="flex justify-between">
                        <h1>Date Order</h1>
                        <h1>{{orderdata.created}}</h1>
                    </div>
                    <div class="flex justify-between">
                        <h1>Status</h1>
                        <h1>{{orderdata.delivery_status}}</h1>
                    </div>
                </div>
            </div>
</template>

<script>
    export default {
        props:["orderdata"],
        data(){
            return{
                orderData:this.orderdata
            }
        }
    }

</script>