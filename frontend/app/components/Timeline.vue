<template>
  <b-container class="commlist">
    <div
      v-for="post in posts"
      :key="post.user_id"
      class="d-flex"
      style="
        align-items: center;
        justify-content: center;
        border-bottom-style: ridge;
        height: 100px;
      "
    >
      <div class="d-flex" style="align-items: center; width: 90%">
        <img
          :src="post.user_icon_url"
          class="d-inline-block"
          style="border-radius: 50%; height: 60px; width: 60px; float: left"
        />
        <div class="d-inline-block ml-auto mr-auto" style="width: 260px">
          <div class="d-inline ml-auto">
            <p style="font-weight: bold; margin-bottom: 0">
              {{ post.user_name }}
            </p>
            {{ menus }}
            <p style="font-size: 6px; margin-bottom: 0; text-align: right">
              を食べました
            </p>
          </div>
          <p style="color: gray; margin-bottom: 0">
            -場所- {{ post.shop_name }}
          </p>
        </div>
      </div>
    </div>
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      // users: [
      //   {
      //     name: 'コラショ',
      //     latestpost: {
      //       shop: 'なか卯',
      //       foods: 'カツ丼',
      //     },
      //   },
      //   {
      //     name: 'トリッピー',
      //     latestpost: {
      //       shop: '串鳥',
      //       foods: 'コロッケ定食',
      //     },
      //   },
      //   {
      //     name: 'しゃちょう',
      //     latestpost: {
      //       shop: 'マクドナルド',
      //       foods: 'ビッグマック',
      //     },
      //   },
      // ],
      posts: [],
      menus: [],
    }
  },
  mounted() {
    this.rankings = this.$axios
      .get(`/posts/communities/0`)
      .then((res) => (this.posts = res.data))

    for (const post of this.posts) {
      for (const list of post.menu) {
        this.menus.push(list.name)
      }
    }
  },
}
</script>
