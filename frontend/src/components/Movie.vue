<template>
    <div class="movies">
        <h1>This is Movies Pages</h1>
        <button @click="logout">Log out</button>
    </div>
</template>

<script>
    // import router from "../router";
    export default {
        name: "Movie",
        mounted() {
            this.checkLogIn();
        },
        methods: {
            checkLogIn(){
                if(this.$store.state.jwt === null){
                    this.$router.push('/auth');
                }
            },
            logout(){
                this.$store.commit('removeToken');
                this.$router.push('/auth');
            }
        }
    }
</script>

<style scoped>
</style>