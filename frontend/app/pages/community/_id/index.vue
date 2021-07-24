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
    this.$api
      .get(`/mock/users/communities`)
      .then((res) => {
        this.belongings = res.data
      })
      .catch((e) => {
        console.error(e)
      })
  },
}
</script>
