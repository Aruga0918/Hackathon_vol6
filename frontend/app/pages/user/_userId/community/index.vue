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
      .get(`/api/users/communities`)
      .then((res) => {
        console.log('api', res.data)
        this.belongings = res.data
      })
      .catch((e) => {
        console.error(e)
      })
  },
}
</script>
