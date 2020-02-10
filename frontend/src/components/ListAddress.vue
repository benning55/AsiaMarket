<template>
    <div class="round border px-32 py-5 flex">
        <div class="w-4/5 text-left text-black py-2 h-full">
            {{address.address}} {{address.addition}} {{address.city}} {{address.postalCode}}
        </div>
        <div>
        </div>
    </div>
</template>

<script>
    export default {
        props: [
            "address"
        ]
    }
</script>