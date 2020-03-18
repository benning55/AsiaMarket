<template>
    <div class="center-y w-full">
        <h1 class="text-2xl text-center">{{$t('you_dont_have_login')}}</h1>
        <h1 @click="goLogin" class="text-center text-orange cursor-pointer">{{$t('go_to_login_page')}}</h1>
    </div>
</template>

<script>
    export default {
        methods:{
            goLogin(){
                this.$router.push({
                    name:'login'
                })
            }
        }
    }
</script>