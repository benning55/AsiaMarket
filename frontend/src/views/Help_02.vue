<template>
    <div>
        <NavbarSpace/>
        <div class="w-full bg-white px-2 sm:px-5 md:px-10 lg:px-12 py-10">
            <h1 class="text-xl">How to Payment</h1>

            <p>กดปุ่ม "บัญชี" ด้านซ้ายของหน้าจอ (เส้นสามขีดมุมบนซ้ายในหน้าจอโทรศัพท์)</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md  w-2/5 md:w-1/5 lg:w-2/12"
                     src="../assets/help/payment/en_account.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md  w-2/5 md:w-1/5 lg:w-2/12"
                     src="../assets/help/payment/th_account.png">
            </div>

            <ul style="list-style:disc " class="ml-5 mb-5">
                <li>กด "<b>ประวัติการสั่งซื้อ</b>"</li>
                <li>ระบบจะแสดงประวัติการสั่งซื้อทั้งหมด</li>
                <li>เลือกรายการที่ต้องการจะชำระเงิน</li>
            </ul>
            <p id="paypal">เลื่อนลงด้านล่างจะพบตัวเลือกของการชำระเงิน</p>
            <ul style="list-style:disc " class="ml-5 mb-5">
                <li><a href="#paypal" class="text-green underline">Paypal</a></li>
                <li><a href="#credit" class="text-green underline">บัตรเครดิต หรือ บัตรเดบิต</a></li>
                <li><a href="#transfer" class="text-green underline">โอนเงินผ่านธนาคาร</a></li>
            </ul>


            <h1 class="text-xl">Paypal</h1>

            <p>กดปุ่มสีเหลืองที่มีสัญลักษณ์ Paypal</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/paypal.png">
            </div>

            <p>ระบบจะเปิดหน้าต่างใหม่ ลงชื่อเข้าใช้งาน Paypal</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  shadow-md" src="../assets/help/payment/loginpaypal.png">
            </div>

            <p>เลือกวิธีชำระเงินของ Paypal</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/choose.png">
            </div>

            <p>ตรวจสอบความถูกต้องและชำระเงิน</p>
            <div class="mt-5 mb-24 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/paypal_confirm.png">
                <hr id="credit" class="text-white">
            </div>


            <h1 class="text-xl">บัตรเครดิต หรือ บัตรเดบิต</h1>

            <p>กดปุ่มสีดำที่มีสัญลักษณ์บัตรเครติต</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/paypal.png">
            </div>

            <p>ใส่ข้อมูลบัตรของท่านลงในช่องที่กำหนด และกดชำระเงิน (Pay Now)</p>
            <div class="mt-5 mb-24 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/card.png">
                <hr id="transfer" class="text-white">
            </div>


            <h1 class="text-xl">โอนเงินผ่านธนาคาร</h1>

            <p>เลือกรูปภาพของหลักฐานการโอนเงิน</p>
            <ul style="list-style:disc " class="ml-5">
                <li>ใส่วันที่โอน</li>
                <li>เลือกเวลาที่โอน (โดยประมาณ)</li>
                <li>กด "ส่ง" เพื่อส่งหลักฐานการโอนเงินให้ผู้ดูแลระบบ</li>
            </ul>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/en_slip.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/th_slip.png">
            </div>
            <p>ผู้ดูแลระบบจะทำการตรวจสอบการโอนเงินภายและยืนยันผลใน 48 ชั่วโมง</p>
        </div>
    </div>
</template>

<script>
    import NavbarSpace from "../components/NavbarSpace";

    export default {
        components: {
            NavbarSpace
        },
        methods: {
            scrollToTop() {
                window.scrollTo(0, 0);
            }
        }
    }
</script>