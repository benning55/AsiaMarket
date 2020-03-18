<template>
    <div class="md:mx-24 sm:mx-0 lg:mx-0 xl:mx-0">
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <div class="bg-white w-full border-green-top px-4 sm:h-full lg:px-16 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
            <div class="text-center text-2xl mb-10 mt-5 font-l">{{$t('page_not_found')}}</div>
            <div class="mb-6 pl-2 w-1/2 mx-auto mt-8">
                <button @click="goHome"
                        class="w-full bg-green text-white text-center py-2 focus:outline-none "
                        type="button">{{$t('go_back_to_homepage')}}
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return{

            }
        },
        methods:{
            goHome(){
                this.$router.push({
                    name:'HomePage'
                })
            }
        }
    }
</script>

<style scoped>

</style>