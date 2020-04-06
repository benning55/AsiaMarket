<template>
    <div>
        <Loader v-if="isLoading"/>
        <NavbarSpace/>

        <section class="mt-3 w-full">
            <h1 class="ml-2 lg:ml-0 my-3 text-xl">{{nameTranslate(titleCategory.category_name)}}
                "{{this.$route.params.id}}"</h1>
            <div v-if="isNotFound" class=" w-full px-0 sm:h-full pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
                <div class="text-center text-2xl mb-10 mt-5 font-l">{{nameTranslate('Product Not
                    Found(ไม่พบสินค้าที่คุณค้นหา)')}}
                </div>
                <div class="mb-6 pl-2 w-1/2 mx-auto mt-8">
                </div>
                <section class="mt-3">
                    <div class="flex justify-between">
                        <h1 class="ml-2 lg:ml-0 my-3 text-xl">{{nameTranslate('You maybe also like(ลองดูสินค้าชิ้นอื่น
                            ๆ)')}}</h1>
                        <router-link :to="{ name: 'Category', params: { id: 'recommend' }}">
                            <h1 class="mr-2 lg:mr-0 my-3 text-md self-center text-gray">{{$t('see_more')}} ></h1>
                        </router-link>
                    </div>
                    <SwiperItem :dataItem="recommendProduct"/>
                </section>
            </div>
            <!--            {{this.$route.params.id}}-->
            <div class="flex flex-wrap">
                <div v-for="item in items" :key="item.id" class="w-1/2 sm:w-1/4 sc-480:w-1/3 sc-1400:w-1/5 relative">
                    <ProductCard :productData="item"/>
                </div>
            </div>
        </section>
    </div>

</template>

<script>
    import VueSlickCarousel from 'vue-slick-carousel'
    import 'vue-slick-carousel/dist/vue-slick-carousel.css'
    import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
    import ProductCard from "../components/ProductCard";
    import axios from 'axios'
    import Loader from "../components/Loader";
    import Carousel from "../components/Carousel";
    import NavbarSpace from "../components/NavbarSpace";
    import SwiperItem from "../components/SwiperItem";

    export default {
        name: 'CategoryView',
        components: {
            VueSlickCarousel,
            ProductCard,
            Loader,
            Carousel,
            NavbarSpace,
            SwiperItem
        },
        data() {
            return {
                setting1: {
                    "dots": true,
                    "dotsClass": "slick-dots custom-dot-class",
                    "edgeFriction": 0.35,
                    "infinite": false,
                    "speed": 500,
                    "slidesToShow": 1,
                    "slidesToScroll": 1,
                    "autoplay": true,
                    "autoplaySpeed": 3000,
                    "pauseOnDotsHover": true,
                    "pauseOnFocus": true,
                    "pauseOnHover": true
                },
                items: [],
                titleCategory: {
                    category_name: "Search result for (ผลการค้นหาสำหรับ)"
                },
                isLoading: false,
                isNotFound: false,
                recommendProduct: []
            }
        },
        created() {
            this.isLoading = true
            this.loadCategory()
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
            loadCategory() {
                this.isLoading = true
                this.items = []
                axios.post(`${this.$store.state.endpoints.host}/api/products/search/`,
                    {
                        name: this.$route.params.id
                    }
                ).then(res => {
                    this.items = res.data.data
                    this.titleCategory = {category_name: "Search result for (ผลการค้นหาสำหรับ)"}
                    this.isNotFound = false
                    this.isLoading = false
                }).catch(e => {
                    if (e.response.status >= 500) {
                        this.isNotFound = true
                        this.$message.error(this.$t('error_Oops_') + e.response.status + ', at search product');
                    } else if (e.response.status >= 400) {
                        this.isNotFound = true
                    } else {
                        this.$message.error(this.$t('error_Oops_') + e.response.status + ', at search product');
                    }
                    this.isLoading = false

                })


            },
        },
        watch: {
            '$route.params.id'() {
                this.loadCategory()
                window.scrollTo(0, 0);
            },
            isNotFound() {
                if (this.isNotFound) {
                    axios.get(this.$store.state.endpoints.recommendProduct).then(res => {
                        this.recommendProduct = res.data.data.slice(0, 8)
                        this.isLoading = false
                        window.scrollTo(0, 0);
                    }).catch(e => {
                        this.$message.error(this.$t('error_Oops_') + e.response.status + ', at load recommend');
                    })
                }
            }
        }
    }
</script>

<style scoped>
    .grid-cols-2 {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    }

    .grid-cols-3 {
        grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
    }

    .grid-cols-4 {
        grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
    }

    .grid-cols-5 {
        grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
    }

    .grid {
        display: grid !important;
    }
</style>