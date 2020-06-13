<template>
    <div class="round px-2 sm:px-2 md:px-10 lg:20 xl:px-32 py-5 flex">
        <div class="w-5/12 text-left text-black px-1 py-2 h-full">
            {{address.recipient}}
        </div>
        <div class="w-6/12 text-left text-black px-1 py-2 h-full">
            {{address.address}} {{address.city}} {{address.state}} {{address.post_code}}
        </div>
        <div @click="goEditAddress(address.id)" class="w-1/12 text-right text-orange px-1 py-2 h-full cursor-pointer">
            {{$t('edit')}}
        </div>
    </div>
</template>

<script>
    export default {
        props: [
            "address"
        ],
        methods: {
            goEditAddress(id) {
                this.$router.push({
                    name: 'EditAddress',
                    params: {id: id}
                })
            }
        }
    }
</script>

<style scoped>

</style>