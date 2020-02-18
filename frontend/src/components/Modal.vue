<template>
    <transition name="modal-fade">
        <div @click.self="close" class="modal-backdrop opacity-bg">
            <div class="modal w-11/12 max-w-3xl "
                 role="dialog">
                <div class="p-5 w-full h-16 flex justify-between bg-white">
                    <h1>Select Destination</h1>
                    <i @click="close" class="fas fa-times cursor-pointer"></i>
                </div>
                <hr>
                <section class="modal-body" id="modalDescription" style="max-height: 500px;height: 50%">
                    <div class="overflow-auto" style="max-height: 500px">
                        <div v-for="(address,index) in $store.state.userAddress" :key="address.id">
                            <div @click="swapIndex(index)" class="round px-2 flex cursor-pointer"
                                 :class="{ 'select': $store.state.indexUserAddress == index }">
                                <div class="w-6/12 text-left text-black px-1 py-2 h-full text-center">
                                    {{address.recipient}}
                                </div>
                                <div class="w-6/12 text-left text-black px-1 py-2 h-full">
                                    {{address.house_number}} {{address.street}} {{address.city}} {{address.post_code}}
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </transition>
</template>

<script>
    export default {
        name: 'modal',
        data() {
            return {
                index: 5
            }
        },
        methods: {
            close() {
                this.$emit('close');
            },
            swapIndex(index) {
                console.log("swap")
                this.$store.commit("setIndexUserAddress", index);
            }
        },
    };
</script>

<style>
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

    .opacity-bg{
        background-color: rgba(38, 50, 56,.5);
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
        transform: scale(1.1,1.1)
    }

    .modal-fade-enter-active,
    .modal-fade-leave-active {
        transition: opacity .5s ease,transform .5s ease;
        /*transition: top .5s ease*/
    }

    .select{
        background-color: rgba(97, 159, 33,.3);
    }
</style>