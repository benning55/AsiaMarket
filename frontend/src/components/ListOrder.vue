<template>
    <div>
        <div class="flex justify-between cursor-pointer hover:bg-unHilight" @click="goEachOrder(orderdata.id)">
            <div v-if="imageError" style="max-width: 130px;" class="my-3 w-1/3 sm:w-1/3 mx-auto object-contain">
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
            <img v-else style="max-width: 130px;" class="my-3 w-1/3 sm:w-1/3 mx-auto object-contain"
                 @error="printerror()"
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
                    <h1 class="text-key_column">{{$t('tracking_no')}}</h1>
                    <h1 v-if="orderdata.tracking_no != null" class="text-orange">{{orderdata.tracking_no}}</h1>
                    <h1 v-else class="text-orange">{{$t('dont_shipping')}}</h1>
                </div>

                <div class="flex justify-between">
                    <h1 class="text-key_column">{{$t('status')}}</h1>
                    <h1 v-if="orderdata.payment_status">
                        <span v-if="orderdata.delivery_status == 'Waiting'" class="text-gray">{{nameTranslate('Wait for Shipping(รอนำส่ง)')}}</span>
                        <span v-if="orderdata.delivery_status == 'Shipping'"
                              class="text-orange">{{nameTranslate('(กำลังส่ง)')}}</span>
                        <span v-if="orderdata.delivery_status == 'Delivered'"
                              class="text-green">{{nameTranslate('Delivered(ส่งสำเร็จ)')}}</span>
                    </h1>
                    <h1 class="text-red" v-else>
                        <span v-if="orderData.payment_type == 'BankTransfer'"
                              class="text-orange">{{$t('wait_admin')}}</span>
                        <span v-else class="text-red">{{$t('not_paid')}}</span>
                    </h1>
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
                orderData: this.orderdata,
                imageError: false
            }
        },
        methods: {
            printerror() {
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