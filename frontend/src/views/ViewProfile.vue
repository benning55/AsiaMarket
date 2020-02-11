<template>
    <div class="md:mx-24 sm:mx-0 lg:mx-0 xl:mx-0">
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <div class="bg-white w-full border-green-top px-4 sm:h-full lg:px-32 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
            <div class="text-center text-2xl mb-10 mt-5 font-l">Profile</div>
            <div class="flex justify-between mb-5">
                <h1 class="text-xl font-l text-gray">Firstname</h1>
                <div v-if="!isEditFirstname" class="md:flex lg:flex xl:flex">
                    <h1 class="text-xl text-right">{{userData.firstname}}</h1>
                    <h1 @click="isEditFirstname = !isEditFirstname"
                        class="text-sm text-right text-orange self-center ml-2">Edit</h1>
                </div>
                <div v-else class="flex">
                    <input v-model="newFirstname"
                           v-bind:class="{ 'border-red': validation.firstError('newFirstname') }"
                           class="appearance-none border rounded-l-lg w-40 py-1 px-2 text-gray leading-tight focus:outline-none"
                           id="newFirstname"
                           type="text"/>
                    <div v-if="!validation.firstError('newFirstname')" @click="editFirstname(newFirstname)"
                         class="w-8 bg-green rounded-r-lg" style="padding-left: 7px;padding-top: 7px">
                        <i class="fas fa-check text-white text-center absolute"></i>
                    </div>
                    <div v-else @click="isEditFirstname = !isEditFirstname" class="w-8 bg-red rounded-r-lg"
                         style="padding-left: 3px ;padding-top: 3px;">
                        <i class="material-icons text-white text-center absolute">
                            clear
                        </i>
                    </div>
                </div>
            </div>
            <div class="flex justify-between mb-5">
                <h1 class="text-xl font-l text-gray">Lastname</h1>
                <div v-if="!isEditLastname" class="md:flex lg:flex xl:flex">
                    <h1 class="text-xl text-right">{{userData.lastname}}</h1>
                    <h1 @click="isEditLastname = !isEditLastname"
                        class="text-sm text-right text-orange self-center ml-2">Edit</h1>
                </div>
                <div v-else class="flex">
                    <input v-model="newLastname"
                           v-bind:class="{ 'border-red': validation.firstError('newLastname') }"
                           class="appearance-none border rounded-l-lg w-40 py-1 px-2 text-gray leading-tight focus:outline-none"
                           id="newLastname"
                           type="text"/>
                    <div v-if="!validation.firstError('newLastname')" @click="editLastname(newLastname)"
                         class="w-8 bg-green rounded-r-lg" style="padding-left: 7px;padding-top: 7px">
                        <i class="fas fa-check text-white text-center absolute"></i>
                    </div>
                    <div v-else @click="isEditLastname = !isEditLastname" class="w-8 bg-red rounded-r-lg"
                         style="padding-left: 3px ;padding-top: 3px;">
                        <i class="material-icons text-white text-center absolute">
                            clear
                        </i>
                    </div>
                </div>
            </div>

            <div class="flex justify-between mb-5">
                <h1 class="text-xl font-l text-gray">Email</h1>
                <h1 class="text-xl">{{userData.email}}</h1>
            </div>
            <div class="flex justify-between mb-5">
                <h1 class="text-xl font-l text-gray">Phone Number</h1>
                <div v-if="!isEditPhone" class="md:flex lg:flex xl:flex">
                    <h1 class="text-xl">{{userData.phone}}</h1>
                    <h1 @click="isEditPhone = !isEditPhone" class="text-sm text-right text-orange self-center ml-2">
                        Edit</h1>
                </div>
                <div v-else class="flex">
                    <input v-model="newPhone"
                           v-bind:class="{ 'border-red': validation.firstError('newPhone') }"
                           class="appearance-none border rounded-l-lg py-1 px-2 text-gray leading-tight focus:outline-none"
                           id="newPhone"
                           style="width:7rem"
                           type="number"/>
                    <div v-if="!validation.firstError('newPhone')" @click="editPhone(newPhone)"
                         class="w-8 bg-green rounded-r-lg" style="padding-left: 7px;padding-top: 7px">
                        <i class="fas fa-check text-white text-center absolute"></i>
                    </div>
                    <div v-else @click="isEditPhone = !isEditPhone" class="w-8 bg-red rounded-r-lg"
                         style="padding-left: 3px ;padding-top: 3px;">
                        <i class="material-icons text-white text-center absolute">
                            clear
                        </i>
                    </div>
                </div>
            </div>
            <div class="flex justify-between mb-5">
                <h1 class="text-xl font-l text-gray">Date of Birth</h1>
                <div v-if="!isEditDOB" class="md:flex lg:flex xl:flex">
                    <h1 class="text-xl">{{userData.dob}}</h1>
                    <h1 @click="isEditDOB = !isEditDOB" class="text-sm text-right text-orange self-center ml-2">
                        Edit</h1>
                </div>
                <div v-else class="flex">
                    <input v-model="newDOB"
                           v-bind:class="{ 'border-red': validation.firstError('newDOB') }"
                           class="appearance-none border rounded-l-lg w-32 py-1 px-2 text-gray leading-tight focus:outline-none"
                           id="newDOB"
                           type="text"/>
                    <div v-if="!validation.firstError('newDOB')" @click="editDOB(newDOB)"
                         class="w-8 bg-green rounded-r-lg" style="padding-left: 7px;padding-top: 7px">
                        <i class="fas fa-check text-white text-center absolute"></i>
                    </div>
                    <div v-else @click="isEditDOB = !isEditDOB" class="w-8 bg-red rounded-r-lg"
                         style="padding-left: 3px ;padding-top: 3px;">
                        <i class="material-icons text-white text-center absolute">
                            clear
                        </i>
                    </div>
                </div>
            </div>
        </div>
        {{$store.state.authUser}}
    </div>
</template>

<script>
    import {Validator} from "../main";

    export default {
        data() {
            return {
                newFirstname: '',
                newLastname: '',
                newPhone: '',
                newDOB: '',
                isEditFirstname: false,
                isEditLastname: false,
                isEditPhone: false,
                isEditDOB: false,
                userData: {}
            }
        },
        validators: {
            newFirstname(value) {
                return Validator.value(value)
                    .required("กรุณาใส่อีเมลล์");
            },
            newLastname(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่าน")
            },
            newPhone(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่าน")
            },
            newDOB(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่าน")
            },
            mockupData(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่าน")
            }
        },
        created() {
            this.loadUserData()
        },
        methods: {
            loadUserData() {
                this.userData = {
                    firstname: this.$store.state.authUser.user.firstname,
                    lastname: 'mennakred',
                    email: this.$store.state.authUser.user.email,
                    phone: '0501326252',
                    dob: '12-12-2012'
                }
                this.equal()
            },
            equal() {
                this.newFirstname = this.userData.firstname
                this.newLastname = this.userData.lastname
                this.newPhone = this.userData.phone
                this.newDOB = this.userData.dob
            },
            editFirstname(firstname) {
                this.userData.firstname = firstname
                this.equal()
                this.isEditFirstname = false
            },
            editLastname(lastname) {
                this.userData.lastname = lastname
                this.equal()
                this.isEditLastname = false
            },
            editPhone(phone) {
                this.userData.phone = phone
                this.equal()
                this.isEditPhone = false
            },
            editDOB(dob) {
                this.userData.dob = dob
                this.equal()
                this.isEditDOB = false
            }
        }
    }
</script>