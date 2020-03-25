<template>
    <div>
        <NavbarSpace/>
        <div class="w-full bg-white px-2 sm:px-5 md:px-10 lg:px-12 py-10">
            <h1 class="text-xl">{{nameTranslate(`How to Payment|วิธีชำระเงิน`)}}</h1>

            <p>{{nameTranslate(`Click "Account" in right screen.(Three line in left on mobile screen)|กดปุ่ม "บัญชี" ด้านซ้ายของหน้าจอ (เส้นสามขีดมุมบนซ้ายในหน้าจอโทรศัพท์)`)}}</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto shadow-md  w-2/5 md:w-1/5 lg:w-2/12"
                     src="../assets/help/payment/en_account.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto shadow-md  w-2/5 md:w-1/5 lg:w-2/12"
                     src="../assets/help/payment/th_account.png">
            </div>

            <ul style="list-style:disc " class="ml-5 mb-5">
                <li>{{nameTranslate(`Click "Order history".|กด "ประวัติการสั่งซื้อ"`)}}</li>
                <li>{{nameTranslate(`Website will show all order.|ระบบจะแสดงประวัติการสั่งซื้อทั้งหมด`)}}</li>
                <li>{{nameTranslate(`Choose the item that you want to pay.|เลือกรายการที่ต้องการจะชำระเงิน`)}}</li>
            </ul>
            <p id="paypal">{{nameTranslate(`Scroll down to choose payment method|เลื่อนลงด้านล่างจะพบตัวเลือกของการชำระเงิน`)}}</p>
            <ul style="list-style:disc " class="ml-5 mb-5">
                <li><a href="#paypal" class="text-green underline">Paypal</a></li>
                <li><a href="#credit" class="text-green underline">{{nameTranslate(`Credit or Debit Card|บัตรเครดิต หรือ บัตรเดบิต`)}}</a></li>
                <li><a href="#transfer" class="text-green underline">{{nameTranslate(`Bank Transfer|โอนเงินผ่านธนาคาร`)}}</a></li>
            </ul>


            <h1 class="text-xl">Paypal</h1>

            <p>{{nameTranslate(`Click yellow button with Paypal symbol|กดปุ่มสีเหลืองที่มีสัญลักษณ์ Paypal`)}}</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/paypal.png">
            </div>

            <p>{{nameTranslate(`In new window. Login by Paypal account|ระบบจะเปิดหน้าต่างใหม่ ลงชื่อเข้าใช้งาน Paypal`)}}</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  shadow-md" src="../assets/help/payment/loginpaypal.png">
            </div>

            <p>{{nameTranslate(`Choose Paypal payment methods|เลือกวิธีชำระเงินของ Paypal`)}}</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/choose.png">
            </div>

            <p>{{nameTranslate(`Verify and make payment.|ตรวจสอบความถูกต้องและชำระเงิน`)}}</p>
            <div class="mt-5 mb-24 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/paypal_confirm.png">
                <hr id="credit" class="text-white">
            </div>


            <h1 class="text-xl">{{nameTranslate(`Credit or Debit Card|บัตรเครดิต หรือ บัตรเดบิต`)}}</h1>

            <p>{{nameTranslate(`Click black button with card symbol|กดปุ่มสีดำที่มีสัญลักษณ์บัตรเครติต`)}}</p>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/paypal.png">
            </div>

            <p>{{nameTranslate(`Input your card information in require field.|ใส่ข้อมูลบัตรของท่านลงในช่องที่กำหนด และกดชำระเงิน (Pay Now)`)}}</p>
            <div class="mt-5 mb-24 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/card.png">
                <hr id="transfer" class="text-white">
            </div>


            <h1 class="text-xl">{{nameTranslate(`Bank Transfer|โอนเงินผ่านธนาคาร`)}}</h1>

            <p>{{nameTranslate(`Choose pictures of proof of payment.| เลือกรูปภาพของหลักฐานการโอนเงิน`)}}</p>
            <ul style="list-style:disc " class="ml-5">
                <li>{{nameTranslate(`Input transfer date.|ใส่วันที่โอน`)}}</li>
                <li>{{nameTranslate(`Choose transfer time.|เลือกเวลาที่โอน (โดยประมาณ)`)}}</li>
                <li>{{nameTranslate(`Click "Send" to send pictures of proof of payment.|กด "ส่ง" เพื่อส่งหลักฐานการโอนเงินให้ผู้ดูแลระบบ`)}}</li>
            </ul>
            <div class="mt-5 mb-20 px-3 md:px-5 lg:px-8 xl:px-12 ">
                <img v-if="$i18n.locale == 'en'" class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/en_slip.png">
                <img v-if="$i18n.locale == 'th'" class="mx-auto  w-4/5 md:w-1/2 lg:w-1/3 shadow-md" src="../assets/help/payment/th_slip.png">
            </div>
            <p>{{nameTranslate(`The administrator will check the internal transfer and confirm the results in 48 hour.|ผู้ดูแลระบบจะทำการตรวจสอบการโอนเงินภายและยืนยันผลใน 48 ชั่วโมง`)}}</p>
        </div>
    </div>
</template>

<script>
    import NavbarSpace from "../components/NavbarSpace";

    export default {
        components: {
            NavbarSpace
        },
        created() {
            window.scrollTo(0, 0);
        },
        methods: {
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