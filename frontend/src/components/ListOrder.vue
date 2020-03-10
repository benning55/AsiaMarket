<template>
    <div>
        <div class="flex justify-between" @click="goEachOrder(orderdata.id)">
            <img style="max-width: 130px;" class="my-3 w-1/3 sm:w-1/3 mx-auto object-contain"
                 :src="$store.state.endpoints.host +'/media/'+orderdata.pic1">

            <div class=" my-3 ml-2 w-2/3 self-center">
                <div class="flex justify-between">
                    <h1 class="text-key_column">Order Number</h1>
                    <h1>{{orderdata.id}}</h1>
                </div>
                <div class="flex justify-between">
                    <h1 class="text-key_column">Total</h1>
                    <h1>{{orderdata.total_price}}</h1>
                </div>
                <div class="flex justify-between">
                    <h1 class="text-key_column">Date Order</h1>
                    <h1>{{timeOrder(orderdata.created)}}</h1>
                </div>

                <div class="flex justify-between">
                    <h1 class="text-key_column">Status</h1>
                    <h1 v-if="orderdata.payment_status">
                        <span v-if="orderdata.delivery_status == 'Waiting'" class="text-gray">Waiting for Delivery</span>
                        <span v-if="orderdata.delivery_status == 'Shipping'" class="text-orange">{{orderdata.delivery_status}}</span>
                        <span v-if="orderdata.delivery_status == 'Delivered'" class="text-green">{{orderdata.delivery_status}}</span>
                    </h1>
                    <h1 class="text-red" v-else>Not paid</h1>
                </div>
            </div>
        </div>
        <hr>
    </div>

</template>

<script>
    import moment from 'moment'

    export default {
        props: ["orderdata"],
        data() {
            return {
                orderData: this.orderdata
            }
        },
        methods: {
            goEachOrder(id) {
                this.$router.push({
                    name: 'ViewEachOrder',
                    params: {id: id}
                })
            },
            timeOrder(time) {
                moment.locale('th');
                return moment(time).format('LL')
            }
        },
        computed: {}
    }

</script>