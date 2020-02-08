<template>
    <div id="app">
        <Navbar/>
        <div class=" mx-auto px-0 sm:px-0 md:px-0 lg:px-56 xl:px-64">
            <router-view/>
        </div>
    </div>
</template>

<script>
    import Navbar from "./components/Navbar";

    export default {
        components: {
            Navbar
        },
        data() {
            return{

            }
        },
        methods: {
            logOut() {
                this.$store.commit('removeToken');
                this.$router.push("/auth");
            },
            lookOut() {
                console.log(this.$store.state.isAuthenticated)
            }
        }
    }
</script>

<style lang="scss">
    #app {
        font-family: 'Kanit', sans-serif;
    }

    #nav {
        padding: 30px;

        a {
            font-weight: bold;
            color: #2c3e50;

            &.router-link-exact-active {
                color: #42b983;
            }
        }
    }

    body {
        background-color: #e3e4e3;
    }

</style>