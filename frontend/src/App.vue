<template>
    <div id="app">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Movies Review!</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
                    aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <router-link to="/movie"><a class="nav-item nav-link">Movies</a></router-link>
                    <router-link to="/login" v-if="this.$store.state.isAuthenticated === false"><a class="nav-item nav-link">Login</a></router-link>
                    <router-link to="/register" v-if="this.$store.state.isAuthenticated === false"><a class="nav-item nav-link">Register</a></router-link>
                    <a class="nav-item nav-link" v-if="this.$store.state.isAuthenticated === true" @click="logOut">Logout</a>
                    <a @click="lookOut">State</a>
                </div>
            </div>
        </nav>
        <br>
        <div class="align-items-center mt-5">
          <router-view/>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
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
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
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
</style>