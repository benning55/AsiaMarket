<template>
    <div class="register container">
        <form>
            <div class="form-row">
                <div class="form-group col-md-12">
                    <label for="inputEmail">Username</label>
                    <input type="text" v-model="username" class="form-control" id="inputEmail" placeholder="Email">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-12">
                    <label for="inputEmail4">Email</label>
                    <input type="email" v-model="email" class="form-control" id="inputEmail4" placeholder="Email">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-12">
                    <label for="inputPassword4">Password</label>
                    <input type="password" v-model="password" class="form-control" id="inputPassword4"
                           placeholder="Password">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-12">
                    <label for="inputPassword">Re-type Password</label>
                    <input type="password" v-model="password2" class="form-control" id="inputPassword"
                           placeholder="Password">
                </div>
            </div>
            <div class="form-group">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="gridCheck">
                    <label class="form-check-label" for="gridCheck">
                        Check me out
                    </label>
                </div>
            </div>
            <button type="submit" class="btn btn-primary" @click.prevent="registered">Sign Up</button>
            <br><br>
        </form>
    </div>
</template>

<script>
    export default {
        name: 'Register',
        data() {
            return {
                "email": null,
                "username": null,
                "password": null,
                "password2": null
            }
        },
        methods: {
            registered (){
            }
        },
    }
</script>