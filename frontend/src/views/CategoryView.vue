<template>
    <div>
        <Loader v-if="isLoading"/>
        <NavbarSpace/>

        <Carousel/>

        <section class="mt-3 w-full">
            <h1 class="my-3 text-xl">{{nameTranslate(titleCategory.category_name)}}</h1>
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

    export default {
        name: 'CategoryView',
        components: {
            VueSlickCarousel,
            ProductCard,
            Loader,
            Carousel,
            NavbarSpace
        },
        data() {
            return {
                items: [],
                titleCategory: '',
                isLoading: false
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
                if (this.$route.params.id == "new-product") {
                    axios.get(this.$store.state.endpoints.newestProduct).then(res => {
                        this.items = res.data.data
                        this.titleCategory = {category_name:"New Product(สินค้าใหม่)"}
                        this.isLoading = false
                    }).catch(e => {
                        this.isLoading = false
                        this.$message.error(this.$t('error_Oops_') + e.status + ', at load new product');
                    })
                } else if (this.$route.params.id == "recommend") {
                    axios.get(this.$store.state.endpoints.recommendProduct).then(res => {
                        this.items = res.data.data
                        this.titleCategory = {category_name:"Recommend Product(สินค้าแนะนำ)"}
                        this.isLoading = false
                    }).catch(e => {
                        this.isLoading = false
                        this.$message.error(this.$t('error_Oops_') + e.status + ', at load recommend product');
                    })
                } else {
                    axios.post(this.$store.state.endpoints.productUrL, {
                        "category_id": this.$route.params.id
                    }).then(res => {
                        this.items = res.data.data
                        this.titleCategory = res.data.data[0]
                        this.isLoading = false
                    }).catch(e => {
                        this.isLoading = false
                        this.$message.error(this.$t('error_Oops_') + e.response.status + ', at load caategory ' + this.$route.params.id);
                    })
                }
            }
        },
        watch: {
            '$route.params.id'() {
                this.loadCategory()
                window.scrollTo(0, 0);
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