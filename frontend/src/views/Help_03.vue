<template>
    <div>
        <NavbarSpace/>
        <div class="w-full bg-white px-2 sm:px-5 md:px-10 lg:px-12 py-10">
            <h1 class="text-xl">{{nameTranslate(`How to Manage Address|การจัดการที่อยู่`)}}</h1>

            <p>{{nameTranslate(`Click "Account" in right screen.(Three line in left on mobile screen)|กดปุ่ม "บัญชี" ด้านซ้ายของหน้าจอ (เส้นสามขีดมุมบนซ้ายในหน้าจอโทรศัพท์)`)}}</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md  w-2/5 md:w-1/5 lg:w-2/12"
                     src="../assets/help/payment/en_account.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md  w-2/5 md:w-1/5 lg:w-2/12"
                     src="../assets/help/payment/th_account.png">
            </div>

            <p>{{nameTranslate(`Click "Address"|กด "ที่อยู่"`)}}</p>
            <p>{{nameTranslate(`Website will show Address of account | ระบบจะแสดงที่อยู่ของผู้ใช้`)}}</p>
            <ul style="list-style:disc " class="ml-5 mb-5">
                <li>{{nameTranslate(`Click "Add new Address" for add new address|หากต้องการเพิ่มที่อยู่ ให้กด "เพิ่มที่อยู่ใหม่" `)}} <a
                        href="#add" class="text-green underline">{{nameTranslate(`see more|ดูเพิ่มเติม`)}}</a>
                </li>
                <li>{{nameTranslate(`Click "edit" for edit address|หากต้องการแก้ไขที่อยู่ ให้กด "แก้ไข" ที่อยู่ที่ต้องการแก้ไข `)}} <a
                        href="#edit" class="text-green underline">{{nameTranslate(`see more|ดูเพิ่มเติม`)}}</a>
                </li>
            </ul>
            <div class="mt-5 mb-32 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md "
                     src="../assets/help/address/en_address.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md"
                     src="../assets/help/address/th_address.png">
                <hr id="add" class="text-white">
            </div>

            <h1 class="text-xl">{{nameTranslate(`Add new Address|เพิ่มที่อยู่ใหม่`)}}</h1>
            <p>{{nameTranslate(`Fill recipient and recipient's address|กรอกข้อมูลชื่อผู้รับ และที่อยู่ตามที่กำหนด`)}}</p>
            <ul style="list-style:disc " class="ml-5 mb-5">
                <li>{{nameTranslate(`Click "Add new Address"|กด "เพิ่มที่อยู่ใหม่" เพื่อเพิ่มที่อยู่ใหม`)}}่</li>
            </ul>
            <div class="mt-5 mb-32 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md "
                     src="../assets/help/address/en_add_address.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md"
                     src="../assets/help/address/th_add_address.png">
                <hr id="edit" class="text-white">
            </div>

            <h1 class="text-xl">{{nameTranslate(`Edit Address|แก้ไขที่อย`)}}</h1>
            <p>{{nameTranslate(`Edit recipient's name and recipient's address|แก้ไขข้อมูลชื่อผู้รับ และที่อยู่ตามที่กำหนด`)}}</p>
            <ul style="list-style:disc " class="ml-5 mb-5">
                <li>{{nameTranslate(`Click "Save" for save new information of address|กด "บันทึก" เพื่อบันทึกข้อมูลใหม่ของที่อยู่`)}}</li>
                <li>{{nameTranslate(`Click "Delete" for delete a address|กด "ลบที่อยู่" เพื่อลบที่อยู่`)}}</li>
                <ul style="list-style:disc " class="ml-5 mb-5">
                    <li class="text-red">{{nameTranslate(`The address cannot be deleted if the user's address has only one address.|ไม่สามารถลบที่อยู่ได้หากที่อยู่ของผู้ใช้มีเพียงที่อยู่เดียว`)}}
                    </li>
                    <li class="text-red">{{nameTranslate(`The address cannot be deleted if the address is selected in as the current shipping address in the cart.|ไม่สามารถลบที่อยู่ได้หากที่อยู่นั้นถูกเลือกในเป็นที่อยู่ที่ใช้ในการส่งสินค้าในตะกร้าปัจจุบัน`)}}
                    </li>
                </ul>
            </ul>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md "
                     src="../assets/help/address/en_edit_address.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md"
                     src="../assets/help/address/th_edit_address.png">
            </div>
        </div>
    </div>
</template>

<script>
    import NavbarSpace from "../components/NavbarSpace";

    export default {
        components: {
            NavbarSpace
        },
        methods:{
            nameTranslate(text) {
            let list = text.split('|')
            if (list.length == 1) {
                return text
            } else {
                if (this.$i18n.locale == 'th') {
                    return list[1]
                } else {
                    return list[0]
                }
            }
        },
        }
    }
</script>