<template>
    <div class="center-y w-full">
        <h1 class="text-2xl text-center">You don't have Login</h1>
        <h1 @click="goLogin" class="text-center text-orange cursor-pointer">Go to Login Page</h1>
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