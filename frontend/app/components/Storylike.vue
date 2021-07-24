<template>
  <ul class="horizontal-list">
    <li v-for="comm in communities" :key="comm.id" class="item">
      <img
        v-if="comm.icon_url"
        style="object-fit: contain; border-radius: 50%; width: 100%"
        :src="comm.icon_url"
      />
      <img
        v-else
        style="object-fit: contain; border-radius: 50%; width: 100%"
        src="@/assets/community.png"
      />
    </li>
  </ul>
</template>
<style>
.horizontal-list {
  overflow-x: auto;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
  margin-bottom: 0%;
  padding-left: 0;
}

.item {
  /* 横スクロール用 */
  display: inline-block;

  /* 見た目調整 */
  height: 40px;
  margin: 5px;
  width: 40px;
}

.li img {
  height: 100%;
  width: 100%;
}
</style>
<script>
export default {
  // props: {
  //   userId:{
  //     type:Number,
  //     required: true
  //   },
  // },
  data() {
    return {
      communities: [],
    }
  },
  mounted() {
    this.communities = this.$axios
      .get(`/mock/users/1/community`)
      .then((res) => {
        this.communities = res.data
      })
  },
}
</script>
