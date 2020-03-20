<template>
    <swiper v-if="carousel.length>0" class="swiper" :options="swiperCarousel">
        <swiper-slide v-for="image in carousel" :key="image.id">
            <img class="object-cover w-full h-80"
                 :src="image.picture"
                 alt="Promotion">
        </swiper-slide>
        <div class="swiper-pagination2" slot="pagination"></div>
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
</template>

<script>
    import axios from "axios";

    export default {
        data() {
            return {
                swiperCarousel: {
                    slidesPerView: 1,
                    loop: true,
                    autoplay: {
                        delay: 5000,
                    },
                    pagination: {
                        el: '.swiper-pagination2',
                        clickable: true,
                        renderBullet(index, className) {
                            return `<span class="${className} swiper-pagination-bullet-custom"></span>`
                        }
                    },

                    navigation: {
                        nextEl: '.swiper-button-next',
                        prevEl: '.swiper-button-prev'
                    }
                },
                carousel: []
            }
        },
        created() {
            this.loadCarousel()
        },
        methods: {
            loadCarousel() {
                axios.get(`${this.$store.state.endpoints.host}/api/products/carousel/`).then(res => {
                    this.carousel = res.data.data
                }).catch(e => {
                    this.$message.error(this.$t('error_Oops_') + e.response.status + ', at load new Product');
                })
            }
        }
    }
</script>

<style>
    .h-80 {
        height: 20rem;
    }

    .swiper-pagination2 {
        text-align: center;
        -webkit-transition: 300ms opacity;
        -o-transition: 300ms opacity;
        transition: 300ms opacity;
        -webkit-transform: translate3d(0, 0, 0);
        transform: translate3d(0, 0, 0);
        z-index: 10;
        padding-top: 10px;
    }

    .swiper-pagination-bullet-custom {
        width: 10px;
        height: 10px;
        text-align: center;
        line-height: 20px;
        font-size: 12px;
        color: #000;
        opacity: 1;
        background: rgba(0, 0, 0, 0.2);
    }

    .swiper-pagination-bullet-custom.swiper-pagination-bullet-active {
        color: #fff;
        background: #fff;
    }

    .swiper-button-prev, .swiper-container-rtl {
        background-image: url("data:image/svg+xml;charset=utf-8,<svg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%2027%2044'><path%20d%3D'M0%2C22L22%2C0l2.1%2C2.1L4.2%2C22l19.9%2C19.9L22%2C44L0%2C22L0%2C22L0%2C22z'%20fill%3D'%23FFFFFF'%2F><%2Fsvg>");
        right: auto;
        left: 10px;
    }

    .swiper-button-next, .swiper-container-rtl {
        background-image: url("data:image/svg+xml;charset=utf-8,<svg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%2027%2044'><path%20d%3D'M27%2C22L27%2C22L5%2C44l-2.1-2.1L22.8%2C22L2.9%2C2.1L5%2C0L27%2C22L27%2C22z'%20fill%3D'%23FFFFFF'%2F><%2Fsvg>");
        right: 10px;
        left: auto;
    }

    .swiper-button-next {
        position: absolute;
        width: 27px;
        height: 44px;
        margin-top: -22px;
        z-index: 10;
        cursor: pointer;
        background-size: 17px 44px;
        background-position: center;
        background-repeat: no-repeat;
    }

    .swiper-button-prev {
        position: absolute;
        width: 27px;
        height: 44px;
        margin-top: -22px;
        z-index: 10;
        cursor: pointer;
        background-size: 17px 44px;
        background-position: center;
        background-repeat: no-repeat;
    }
</style>