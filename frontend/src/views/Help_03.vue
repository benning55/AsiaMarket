<template>
    <div>
        <NavbarSpace/>
        <div class="w-full bg-white px-2 sm:px-5 md:px-10 lg:px-12 py-10">
            <h1 class="text-xl">How to Manage Address</h1>

            <p>กดปุ่ม "บัญชี" ด้านซ้ายของหน้าจอ (เส้นสามขีดมุมบนซ้ายในหน้าจอโทรศัพท์)</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md  w-2/5 md:w-1/5 lg:w-2/12"
                     src="../assets/help/payment/en_account.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md  w-2/5 md:w-1/5 lg:w-2/12"
                     src="../assets/help/payment/th_account.png">
            </div>

            <p>กด "<b>ที่อยู่</b>"</p>
            <p>ระบบจะแสดงที่อยู่ของผู้ใช้</p>
            <ul style="list-style:disc " class="ml-5 mb-5">
                <li>หากต้องการเพิ่มที่อยู่ ให้กด "เพิ่มที่อยู่ใหม่" <a href="#paypal" class="text-green underline">ดูเพิ่มเติม</a>
                </li>
                <li>หากต้องการแก้ไขที่อยู่ ให้กด "แก้ไข" ที่อยู่ที่ต้องการแก้ไข <a href="#credit"
                                                                                   class="text-green underline">ดูเพิ่มเติม</a>
                </li>
            </ul>
            <div class="mt-5 mb-24 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md "
                     src="../assets/help/address/en_address.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md"
                     src="../assets/help/address/th_address.png">
            </div>

            <h1 class="text-xl">เพิ่มที่อยู่ใหม่</h1>
            <p>กรอกข้อมูลชื่อผู้รับ และที่อยู่ตามที่กำหนด</p>
            <ul style="list-style:disc " class="ml-5 mb-5">
                <li>กด "เพิ่มที่อยู่ใหม่" เพื่อเพิ่มที่อยู่ใหม่</li>
            </ul>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md "
                     src="../assets/help/address/en_add_address.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md"
                     src="../assets/help/address/th_add_address.png">
            </div>

            <h1 class="text-xl">แก้ไขที่อยู่</h1>
            <p>แก้ไขข้อมูลชื่อผู้รับ และที่อยู่ตามที่กำหนด</p>
            <ul style="list-style:disc " class="ml-5 mb-5">
                <li>กด "บันทึก" เพื่อบันทึกข้อมูลใหม่ของที่อยู่</li>
                <li>กด "ลบที่อยู่" เพื่อลบที่อยู่</li>
                <ul style="list-style:disc " class="ml-5 mb-5">
                    <li class="text-red">ไม่สามารถลบที่อยู่ได้หากที่อยู่ของผู้ใช้มีเพียงที่อยู่เดียว</li>
                    <li class="text-red">ไม่สามารถลบที่อยู่ได้หากที่อยู่นั้นถูกเลือกในเป็นที่อยู่ที่ใช้ในการส่งสินค้าในตะกร้าปัจจุบัน</li>
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
        }
    }
</script>