<template>
  <div class="sm:mx-0 md:mx-24 lg:mx-0 xl:mx-0">
    <Loader v-if="isLoading"/>
    <NavbarSpace/>
    <div v-if="$store.state.isAuthenticated" class="px-3 pt-4 md:px-0">
      <a href="#payment">
        <el-alert v-if="!order.payment_status && !order.receipt"
                  type="warning"
                  show-icon
                  :closable="false">
          <h1 class="text-lg">{{ $t('not_paid') }}</h1>
        </el-alert>
        <el-alert v-if="!order.payment_status && order.receipt"
                  type="warning"
                  show-icon
                  :closable="false">
          <h1 class="text-lg">{{ $t('sent_slip') }}</h1>
        </el-alert>
      </a>

    </div>

    <h1 v-if="$store.state.isAuthenticated" class="py-1 text-xl font-l px-3 md:px-0">{{ $t('product') }}</h1>

    <div v-if="!$store.state.isAuthenticated"
         class="bg-white w-full px-1 h-64 lg:px-10 xl:px-24 pb-10 mx-auto relative mt-10">
      <NoLoginText/>
    </div>

    <!--        show when have item in cart-->
    <div v-else>
      <div class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 pb-10 mx-auto ">
        <table id="orderTable" class="table-auto w-full">
          <thead class="border-bottom">
          <tr class="">
            <th class="px-2 py-2 w-2/12 sm:1/12"></th>
            <th class="px-2 py-2 w-3/12 text-left" style="font-weight: normal">{{ $t('product_name') }}</th>
            <th class="p-0 sm:p-2 w-1/12" style="font-weight: normal">{{ $t('product_price') }}</th>
            <th class="p-0 sm:p-2 w-1/12 hidden sm:table-cell" style="font-weight: normal">
              {{ $t('product_quantity') }}
            </th>
            <th class="p-0 sm:p-2 w-1/12 table-cell sm:hidden" style="font-weight: normal">
              {{ $t('product_q') }}
            </th>
            <th class="p-0 sm:p-2 w-1/12" style="font-weight: normal">{{ $t('total') }}</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="item in orderDetail" :key="item.id" class="border-bottom">
            <td class="px-2 py-2">
              <div v-if="imageError" class="w-full mx-auto"
                   style="max-width: 120px;height: 120px; object-fit: contain">
                <svg style="width: 100%;height: 100%" xmlns="http://www.w3.org/2000/svg"
                     height="300px" width="300px"
                     version="1.1"
                     viewBox="-300 -300 600 600"
                     font-family="Kanit"
                     font-size="72"
                     text-anchor="middle">

                  <circle stroke="#AAA" stroke-width="10" r="280" fill="#FFF"/>
                  <text style="fill:#444;">
                    <tspan x="0" y="-8">{{ $t('NO_IMAGE') }}</tspan>
                    <tspan x="0" y="80">{{ $t('AVAILABLE') }}</tspan>
                  </text>
                </svg>
              </div>
              <img v-else class="w-full mx-auto"
                   style="max-width: 120px;height: 120px; object-fit: contain"
                   :src="$store.state.endpoints.host + item.product.pic1"
                   @error="printerror()"
                   alt="">
            </td>
            <td class="px-2 py-2">
              <div>{{ nameTranslate(item.product.title) }}</div>
              <div v-if="!item.product.is_active" class="text-red">{{ $t('product_not_active') }}</div>
            </td>
            <td class="px-2 py-2 text-center text-green">{{ item.product.price }}</td>
            <td class="px-2 py-2 text-center">{{ item.quantity }}</td>
            <td class="px-2 py-2 text-center text-green">{{ (item.product.price * item.quantity).toFixed(2) }}
            </td>
          </tr>
          </tbody>
        </table>
        <div class="px-5 md:px-10 font-l mt-5 text-xl">
          <div class="flex justify-between">
            <h1 class="">{{ $t('subTotal') }}</h1>
            <h1 class="text-green">{{ order.total_price }} €</h1>
          </div>
          <div class="flex justify-between">
            <h1 class="">{{ $t('shipping') }}</h1>
            <h1 class="">{{ order.shipping_fee }} €</h1>
          </div>
          <div class="flex justify-between">
            <h1 class="">{{ $t('coupon_code') }}</h1>
            <h1 v-if="order.code != null" class="">{{ order.code }}</h1>
            <h1 v-else>{{ $t('no_code') }}</h1>
          </div>
          <div class="flex justify-between">
            <h1 class="">{{ $t('total') }}</h1>
            <h1 class="text-green">{{ order.price }} €</h1>
          </div>

          <div class="flex justify-between mt-5">
            <h1 class="">{{ $t('tracking_no') }}</h1>
            <h1 v-if="order.tracking_no != null" class="text-orange">{{ order.tracking_no }}</h1>
            <h1 v-else class="text-orange">{{ $t('dont_shipping') }}</h1>
          </div>
        </div>
      </div>

      <div class="flex justify-between px-1 sm:px-0">
        <h1 class="mt-5 py-1 text-xl font-l">{{ $t('shipping_information') }}</h1>
      </div>
      <div class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 mx-auto py-5">
        <div class="px-5 md:px-10 font-l text-lg">
          <div class="flex justify-between">
            <h1 class="">{{ $t('recipient') }}</h1>
            <h1 class="text-right">
              {{ order.address }}
            </h1>
          </div>
        </div>
      </div>

      <div id="payment" class="flex justify-between px-1 sm:px-0">
        <h1 class="mt-5 py-1 text-xl font-l">{{ $t('payment') }}</h1>
      </div>
      <SelectPayment v-if="!order.payment_status && !order.receipt" :id="$route.params.id" :order="order"
                     :orderDetail="orderDetail" @updatePayment="loadData"/>
      <div v-else-if="!order.payment_status && order.receipt"
           class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 mx-auto py-5">
        <div class="px-5 md:px-10 font-l text-lg">
          {{ $t('sent_slip') }}
        </div>
      </div>
      <div v-else class="bg-white w-full px-1 sm:h-full lg:px-10 xl:px-24 mx-auto py-5">
        <div class="px-5 md:px-10 font-l text-lg">
          {{ $t('payment_success') }}
        </div>
      </div>


      <div class="flex justify-between pt-10">
        <button class="w-32 text-black_p py-2 focus:outline-none flex justify-start"
                type="button">
          <p @click="$router.go(-1)" class="inline-flex ml-0">
            <i class="material-icons">keyboard_arrow_left</i><span>{{ $t('previous') }}</span>
          </p>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import {Validator} from "../main";
// import moment from 'moment'
import SelectPayment from "./SelectPayment";
import NoLoginText from "../components/NoLoginText";
import Loader from "../components/Loader";
import NavbarSpace from "../components/NavbarSpace";

export default {
  components: {
    SelectPayment,
    NoLoginText,
    Loader,
    NavbarSpace
  },
  data() {
    return {
      orderData: {},
      order: {
        total_price: ''
      },
      orderDetail: null,
      isLoading: false,
      imageError: false
    }
  },
  created() {
    this.isLoading = true
    this.loadData()
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
    loadData() {
      axios.get(`${this.$store.state.endpoints.host}/api/orders/order/` + this.$route.params.id + '/', {
        headers: {
          Authorization: `JWT ${this.$store.state.jwt}`,
          'Content-Type': 'application/json'
        }
      }).then(res => {
        this.isLoading = false
        this.order = res.data.data.order[0]
        this.orderDetail = res.data.data.order_detail
      }).catch(e => {
        this.isLoading = false
        this.$message.error(this.$t('error_Oops_') + e.status + ', at Load this Order');
      })
    },
    printerror() {
      this.imageError = true
    }
  }
}
</script>

<style scoped>
.el-alert__description {
  margin-top: 0;
}
</style>