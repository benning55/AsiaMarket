<template>
    <swiper :options="swiperOption">
        <swiper-slide v-for="product in dataItem" :key="product.key">
            <ProductCard :productData="product"/>
        </swiper-slide>
    </swiper>
</template>

<script>
    import ProductCard from "./ProductCard";
    export default {
        props: ["dataItem"],
        components:{
            ProductCard
        },
        data() {
            return {
                swiperOption: {
                    slidesPerView: 5,
                    pagination: {
                        el: '.swiper-pagination',
                        clickable: true
                    },
                    breakpoints: {
                        1400: {
                            slidesPerView: 4,
                        },
                        1024: {
                            slidesPerView: 4,
                        },
                        640: {
                            slidesPerView: 3,
                        },
                        480: {
                            slidesPerView: 2,
                        }
                    }
                }
            }
        }
    }
</script>