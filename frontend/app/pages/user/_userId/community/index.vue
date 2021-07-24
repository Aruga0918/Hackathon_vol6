<template>
  <div>
    <Comunities class="d-inline ml-auto mr-auto" :belongings="belongings" />
    <Commodal />
  </div>
</template>

<script>
export default {
  data() {
    return {
      belongings: [],
    }
  },
  mounted() {
    this.belongings = this.$axios
      .get(`/mock/users/${this.$route.params.userId}/communities`)
      .then((res) => {
        this.belongings = res.data
      })
  },
}
</script>
