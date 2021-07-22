<template>
  <Shopdata :shopdata="shopData" />
</template>
<script>
export default {
  data() {
    return {
      shopData: [],
    }
  },
  mounted() {
    this.shopData = this.$axios
      .get(`/mock/shops/${this.$route.params.shopId}`)
      .then((res) => (this.shopData = res.data))
    console.log(this.shopData)
  },
}
</script>
