<template>
  <Shopdata :shopdata="shopData" />
</template>
<script>
export default {
  data: () => {
    return {
      shopData: [],
    }
  },
  mounted() {
    this.$api
      .get(`/api/shops/${this.$route.params.shopId}`)
      .then((res) => {
        this.shopData = res.data
      })
      .catch((e) => {
        console.error(e)
      })
  },
}
</script>
