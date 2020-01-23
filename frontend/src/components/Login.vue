<template lang="html">
    <div class="auth container">
        <form>
            <h1>Log In</h1>
            <div class="form-group">
                <label for="exampleInputEmail1">Username</label>
                <input type="text" v-model="username" class="form-control" id="exampleInputEmail1"
                       aria-describedby="emailHelp"
                       placeholder="Enter Username">
                <small id="emailHelp" class="form-text text-muted">We'll never share your Username with anyone
                    else.</small>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">Password</label>
                <input type="password" v-model="password" class="form-control" id="exampleInputPassword1"
                       placeholder="Password">
            </div>
            <router-link to="/register"><small>Don't have an account?</small></router-link>
            <br><br>
            <button type="submit" class="btn btn-primary" @click.prevent="authenticate">Submit</button>
        </form>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "Login",
        data() {
            return {
                username: '',
                password: ''
            }
        },
        methods: {
            authenticate() {
                const payload = {
                    username: this.username,
                    password: this.password
                };
                axios.post(this.$store.state.endpoints.obtainJWT, payload)
                    .then((response) => {
                        this.$store.commit('updateToken', response.data.token);
                        //get and set auth user
                        const base = {
                            baseURL: this.$store.state.endpoints.baseUrL,
                            headers: {
                                // Set your Authorization to 'JWT', not Bearer!!!
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                            xhrFields: {
                                withCredentials: true
                            }
                        };
                        //Even though the authentication returned a user object that can be
                        //decoded, we fetch it again. This way we aren't super dependant on
                        //JWT and can plug in something else.
                        const axiosInstance = axios.create(base);
                        axiosInstance({
                            url: "/user/",
                            method: "get",
                            params: {}
                        }).then((response) => {
                                this.$store.commit("setAuthUser",
                                    {authUser: response.data, isAuthenticated: true}
                                );
                                console.log(this.$store.state.authUser);
                                console.log(this.$store.state.authUser['profile']);
                                this.$router.push("/movies")
                            }).catch((error) => {
                            console.log(error);
                            alert(this.$store.state.jwt)
                        })
                    })
                    .catch((error) => {

                        console.log(error);
                        console.debug(error);
                        console.dir(error);
                        alert('Fuck You')
                    })
            }
        }
    }
</script>

<style lang="css">
</style>