<template>
    <div>
<!--        <section v-if="type == 'address'" class="modal-body" id="modalDescription"-->
<!--                 style="max-height: 500px;height: 50%">-->
<!--            {{chooseNewAddress}}-->
<!--            <div class="overflow-auto" style="max-height: 500px">-->
<!--                <div v-for="(address,index) in $store.state.userAddress" :key="address.id">-->
<!--                    <div @click="swapIndex(index)" class="round px-2 flex cursor-pointer"-->
<!--                         :class="{ 'select': $store.state.indexUserAddress == index && chooseNewAddress == false }">-->
<!--                        <div class="w-6/12 text-left text-black px-1 py-2 h-full text-center">-->
<!--                            {{address.recipient}}-->
<!--                        </div>-->
<!--                        <div class="w-6/12 text-left text-black px-1 py-2 h-full">-->
<!--                            {{address.house_number}} {{address.street}} {{address.city}} {{address.post_code}}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->

<!--            </div>-->
<!--        </section>-->

        <!--                show check user is comfirm-->
<!--        <section v-if="type == 'check_confirm'" class="modal-body">-->
<!--            <div class="px-4 pb-4 sm:px-5 sm:py-5 h-full">-->

<!--                &lt;!&ndash;                        show when complete&ndash;&gt;-->
<!--                <div v-if="isOrderComplete" class="h-full flex flex-wrap content-between">-->
<!--                    <div class="w-full text-center text-green" style="font-size: 3.2rem">-->
<!--                        <i class="far fa-check-circle"></i></div>-->
<!--                    <p class="pb-5">{{$t('you_order_complete')}}</p>-->
<!--                    <div class="flex justify-between w-full">-->
<!--                        <div @click="goHome" class="bg-red py-2  px-4 text-white cursor-pointer">-->
<!--                            {{$t('back_to_homepage')}}-->
<!--                        </div>-->
<!--                        <div @click="goEachOrder" class="bg-green py-2 px-4 text-white cursor-pointer">-->
<!--                            {{$t('go_payment')}}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->

<!--                &lt;!&ndash;                        show before select&ndash;&gt;-->
<!--                <div v-else class=" flex flex-wrap content-between">-->
<!--                    <p class="pb-5">{{$t('are_you_sure_to_confirm')}}</p>-->
<!--                    <div class="flex justify-between w-full">-->
<!--                        <div @click="$emit('close')" class="bg-red py-2  px-4 text-white cursor-pointer">-->
<!--                            {{$t('cancel')}}-->
<!--                        </div>-->
<!--                        <div @click="confirmOrder" class="bg-green py-2 px-4 text-white cursor-pointer">-->
<!--                            {{$t('confirm')}}-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->
<!--            </div>-->
<!--        </section>-->
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'modal',
        props: ["type", "total"],
        data() {
            return {
                index: 5,
                id: 0,
                chooseNewAddress:this.total[4],
                isOrderComplete: false,
                dialogTableVisible: false
            }
        },
        methods: {
            close() {
                if (this.isOrderComplete) {
                    location.reload()
                } else {
                    this.$emit('close');
                }

            },
            swapIndex(index) {
                this.$store.commit("setIndexUserAddress", index);
                this.$emit('chooseExist')
                this.$emit('close')
            },
            confirmOrder() {
                axios.post(`${this.$store.state.endpoints.host}/api/orders/order/`, {
                    address: this.$store.state.userAddress[this.$store.state.indexUserAddress].recipient + ' ' + this.$store.state.userAddress[this.$store.state.indexUserAddress].house_number + ', ' + this.$store.state.userAddress[this.$store.state.indexUserAddress].street + ', ' + this.$store.state.userAddress[this.$store.state.indexUserAddress].city + ' ' + this.$store.state.userAddress[this.$store.state.indexUserAddress].post_code,
                    total_price: this.total[0],
                    payment_type: "",
                    payment_status: false,
                    shipping_fee: this.total[1],
                    price: this.total[3]

                }, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    }
                }).then(res => {
                    this.isOrderComplete = true
                    this.id = res.data.data.id
                    this.$store.commit("setIncart", {
                        cart_detail: []
                    });
                    $(".el-dialog").css({"max-width": "350px", "height": "300px"});
                }).catch(e => {
                    this.$message.error(this.$t('error_Oops_') + e.response.status + ', at confirm order');
                })
            },
            goEachOrder() {
                this.$router.push({
                    name: 'ViewEachOrder',
                    params: {id: this.id}
                })
            },
            goHome() {
                this.$router.push("/")
                location.reload();
            }
        },
    };
</script>

<style scoped>

    .el-alert .el-alert__description {
        margin: 0 0 0 0 !important;
    }

    .modal-backdrop {
        position: fixed;
        top: 72px;
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        justify-content: center;
        align-items: center;

    }

    .opacity-bg {
        background-color: rgba(38, 50, 56, .5);
        z-index: 5;
    }

    .modal {
        background: #FFFFFF;
        /*box-shadow: 2px 2px 20px 1px;*/
        overflow-x: auto;
        display: flex;
        flex-direction: column;
    }

    .modal-header,
    .modal-footer {
        padding: 5px;
        display: flex;
    }

    .modal-header {
        border-bottom: 1px solid #eeeeee;
        color: #4AAE9B;
        justify-content: space-between;
    }

    .modal-footer {
        border-top: 1px solid #eeeeee;
        justify-content: flex-end;
    }

    .modal-body {
        height: 200px;
        position: relative;
        padding: 0px 0px;
    }

    .btn-close {
        border: none;
        font-size: 20px;
        padding: 20px;
        cursor: pointer;
        font-weight: bold;
        color: #4AAE9B;
        background: transparent;
    }

    .btn-green {
        color: white;
        background: #4AAE9B;
        border: 1px solid #4AAE9B;
        border-radius: 2px;
    }

    .modal-fade-enter,
    .modal-fade-leave-active {
        opacity: 0;
        transform: scale(1.1, 1.1)
    }

    .modal-fade-enter-active,
    .modal-fade-leave-active {
        transition: opacity .3s ease, transform .3s ease;
        /*transition: top .5s ease*/
    }

    .select {
        background-color: rgba(97, 159, 33, .3);
    }
</style>