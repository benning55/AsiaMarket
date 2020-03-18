<template>
    <div>
        <div class="flex justify-between" @click="goEachOrder(orderdata.id)">
            <img style="max-width: 130px;" class="my-3 w-1/3 sm:w-1/3 mx-auto object-contain"
                 :src="$store.state.endpoints.host +'/media/'+orderdata.pic1">
            <div class=" my-3 ml-2 w-2/3 self-center">
                <div class="flex justify-between">
                    <h1 class="text-key_column">{{$t('order_number')}}</h1>
                    <h1>{{orderdata.id}}</h1>
                </div>
                <div class="flex justify-between">
                    <h1 class="text-key_column">{{$t('total')}}</h1>
                    <h1>{{orderdata.total_price}}</h1>
                </div>
                <div class="flex justify-between">
                    <h1 class="text-key_column">{{$t('date_order')}}</h1>
                    <h1>{{timeOrder(orderdata.created)}}</h1>
                </div>

                <div class="flex justify-between">
                    <h1 class="text-key_column">{{$t('status')}}</h1>
                    <h1 v-if="orderdata.payment_status">
                        <span v-if="orderdata.delivery_status == 'Waiting'" class="text-gray">{{$t('waiting_for_delivery')}}</span>
                        <span v-if="orderdata.delivery_status == 'Shipping'"
                              class="text-orange">{{$t('shipping')}}</span>
                        <span v-if="orderdata.delivery_status == 'Delivered'"
                              class="text-green">{{$t('delivered')}}</span>
                    </h1>
                    <h1 class="text-red" v-else>{{$t('not_paid')}}</h1>
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
                moment.locale(this.$i18n.locale);
                return moment(time).format('LL')
            }
        },
        computed: {}
    }

</script>