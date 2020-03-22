<template>
    <div>
        <NavbarSpace/>
        <div class="w-full bg-white px-2 sm:px-5 md:px-10 lg:px-12 py-10">
            <h1 class="text-xl mb-10">How to Order</h1>

            <p>กดปุ่ม "ใส่ตะกร้า" หรือ "Add" และเลือกจำนวนสินค้าที่ต้องการลงในตะกร้า</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto shadow-md" src="../assets/help/order/select.png">
            </div>

            <p>กดปุ่มสัญลักษณ์รถเข็นด้านซ้ายของหน้าจอ (มุมบนขวาในหน้าจอโทรศัพท์) เพื่อดูสิ่งของต่าง ๆ ในตะกร้า</p>
            <ul style="list-style:disc " class="ml-5">
                <li>สามารถเอาสินค้าออกได้โดยการกดเครื่องหมายรูปถังขยะ และกด "ลบ"</li>
                <li>หากท่ามีรหัสส่วนลด สามารถใส่ได้ในช่อง "รหัสส่วนลด"</li>
            </ul>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto  shadow-md" src="../assets/help/order/cartEN.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md" src="../assets/help/order/cartTH.png">
            </div>

            <p>กด "ตรวจสอบสินค้า" เพื่อทำการตรวจสอบสินค้า</p>
            <ul style="list-style:disc " class="ml-5">
                <li>ไม่สามารถกดได้หากสินค้าในตะกร้าอย่างน้อง 1 ชิ้น มีไม่เพียงพอ ให้เปลี่ยนจำนวนสินค้าใหม่หรือลบออก</li>
                <li>หากสินค้าหมด กรุณาลบออกจากตะกร้า</li>
            </ul>
            <div class="mt-5 mb-20 mx-auto px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md w-4/5 lg:w-1/3"
                     src="../assets/help/order/checkoutbuttonEN.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md w-4/5 lg:w-1/3"
                     src="../assets/help/order/checkoutbuttonTH.png">
            </div>

            <p>ตรวจสอบสินค้าและข้อมูลต่าง ๆ ของการสั่งซื้อ</p>
            <ul style="list-style:disc " class="ml-5">
                <li>สามารถแก้ไขสินค้าได้ในตระกร้าสินค้า</li>
            </ul>
            <div class="mt-5 mb-20 mx-auto px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md" src="../assets/help/order/confirmEN.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md" src="../assets/help/order/confirmEN.png">
            </div>

            <p>เลื่อนจอลงมาด้านล่าง จะพบกับข้อมูลของสถานที่สำหรับจัดส่ง หากต้องการเปลี่ยนที่อยู่จัดส่ง ให้กดปุ่ม
                "เปลี่ยน"</p>
            <div class="mt-5 mb-20 mx-auto px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md" src="../assets/help/order/confirm2EN.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md" src="../assets/help/order/confirm2TH.png">
            </div>

            <p>เลือกที่อยู่ที่ต้องการจัดส่ง</p>
            <div class="mt-5 mb-20 mx-auto px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md w-4/5 lg:w-1/3"
                     src="../assets/help/order/selectaddressEN.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md w-4/5 lg:w-1/3"
                     src="../assets/help/order/selectaddressTH.png">
            </div>

            <p>กดปุ่ม "ยืนยันการสั่งซื้อและไปยังหน้าชำระเงิน" เพื่อทำการสั่งซื้อ</p>
            <div class="mt-5 mb-20 mx-auto px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md w-4/5 lg:w-1/3"
                     src="../assets/help/order/confirm_btnTH.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md w-4/5 lg:w-1/3"
                     src="../assets/help/order/confirm_btnTH.png">
            </div>

            <p>กด "ยืนยัน" เพื่อสั่งซื้อ กด "ยกเลิก" เพื่อออก</p>
            <div class="mt-5 mb-20 mx-auto px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md w-4/5 lg:w-1/3"
                     src="../assets/help/order/confirmorderEN.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md w-4/5 lg:w-1/3"
                     src="../assets/help/order/confirmorderTH.png">
            </div>

            <p>เมื่อการสั่งซื้อสำเร็จ</p>
            <ul style="list-style:disc " class="ml-5">
                <li>เลือก "ชำระเงิน" เพื่อไปยังหน้าชำระเงิน</li>
                <li>เลือก "กลับไปหน้าหลัก" หากต้องการชำระเงินในภายหลัง</li>
            </ul>
            <div class="mt-5 mb-20 mx-auto px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md w-4/5 lg:w-1/3" src="../assets/help/order/completeEN.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md w-4/5 lg:w-1/3" src="../assets/help/order/completeTH.png">
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
        data() {
            return {
                text: [
                    'กดปุ่ม "ใส่ตะกร้า" และเลือกจำนวนสินค้าที่ต้องการลงในตะกร้า',
                    'กดปุ่มสัญลักษณ์รถเข็นด้านซ้ายของหน้าจอ (มุมบนซ้ายในหน้าจอโทรศัพท์) เพื่อดูสิ่งของต่าง ๆ ในตะกร้า',
                    '-สามารถเอาสินค้าออกได้โดยการกดเครื่องหมายรูปถังขยะ และกด "ลบ"',
                    '-หากท่ามีรหัสส่วนลด สามารถใส่ได้ในช่อง "รหัสส่วนลด"',
                    'กด "ตรวจสอบสินค้า" เพื่อทำการตรวจสอบสินค้า',
                    '-ไม่สามารถกดได้หากสินค้าในตะกร้าอย่างน้อง 1 ชิ้น มีไม่เพียงพอ ให้เปลี่ยนจำนวนสินค้าใหม่หรือลบออก',
                    '-หากสินค้าหมด กรุณาลบออกจากตะกร้า',
                    'สามารถแก้ไขสินค้าได้ในตระกร้าสินค้า',
                    '', '', '', '', '', '',

                ]
            }
        },
        methods: {
            nameTranslate(text) {
                let list = text.split(')').join('(').split('(')
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

<style scoped>
</style>