<template>
    <div>
        <Loader v-if="isLoading"/>
        <ul class="w-full py-6">
            <li class="inline-block px-5">|</li>
        </ul>
<!--        <VueSlickCarousel v-bind="setting1">-->
<!--            <img v-for="image in mockup.showCarousel" :key="image.id" class="object-cover w-full h-56"-->
<!--                 :src="image.image"-->
<!--                 alt="Promotion">-->
<!--        </VueSlickCarousel>-->

        <Carousel/>

        <section class="mt-3 w-full">
            <h1 class="my-3 text-xl">{{titleCategory.category_name}}</h1>
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

    export default {
        name: 'CategoryView',
        components: {
            VueSlickCarousel,
            ProductCard,
            Loader,
            Carousel
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
                mockup: {
                    showCarousel: [
                        {
                            image: 'https://images.unsplash.com/photo-1565564331571-c3a69a159944?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80'
                        },
                        {
                            image: 'https://images.unsplash.com/photo-1565564331571-c3a69a159944?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80'
                        },
                        {
                            image: 'https://images.unsplash.com/photo-1565564331571-c3a69a159944?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80'
                        },
                        {
                            image: 'https://images.unsplash.com/photo-1565564331571-c3a69a159944?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80'
                        }
                    ]
                },
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
            loadCategory() {
                this.isLoading = true
                this.items = []
                if (this.$route.params.id == "new-product") {
                    axios.get(this.$store.state.endpoints.newestProduct).then(res => {
                        this.items = res.data.data
                        this.titleCategory = "New Product"
                        this.isLoading = false
                    }).catch(e => {
                        this.isLoading = false
                        this.$message.error('Oops, Something is Error. code ' + e.status + ', at load new product');
                    })
                } else if (this.$route.params.id == "recommend") {
                    axios.get(this.$store.state.endpoints.recommendProduct).then(res => {
                        this.items = res.data.data
                        this.titleCategory = "Recommend Product"
                        this.isLoading = false
                    }).catch(e => {
                        this.isLoading = false
                        this.$message.error('Oops, Something is Error. code ' + e.status + ', at load recommend product');
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
                        this.$message.error('Oops, Something is Error. code ' + e.status + ', at load caategory ' + this.$route.params.id);
                    })
                }


            }
        },
        watch: {
            '$route.params.id'() {
                this.loadCategory()
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