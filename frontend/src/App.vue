<template>
    <div id="app">
        <!--        {{$router.currentRoute.name}}-->
        <Navbar/>
        <div class="mx-auto px-0 sm:px-0 md:px-0 lg:px-56 xl:px-64">
            <router-view/>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Navbar from "./components/Navbar";
    import Footer from "./components/Footer";

    export default {
        components: {
            Navbar,
            Footer
        },
        data() {
            return {}
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
    .font-l {
        font-weight: 300;
    }

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

    .border-green-top {
        border-top: 6px solid #619F21;
    }

    .border-bottom {
        border-bottom: 1px solid #707070
    }

    .center-y {
        margin: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }

</style>