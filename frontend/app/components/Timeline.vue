<template>
  <div>
    <div
      v-for="(post, idx) in posts"
      :key="idx"
      class="d-flex"
      style="border-bottom: ridge"
    >
      <div style="width: 15%" class="mr-1">
        <b-img
          :src="post.user_icon_url"
          style="object-fit: contain; border-radius: 50%; width: 100%"
        />
      </div>
      <div style="width: 85%">
        <div class="d-flex m-0 p-0" style="line-height: 0.5em">
          <h6 class="m-0">
            {{ post.user_name }}
          </h6>
          <small class="text-muted p-0 m-1">@{{ post.uid }}</small>
        </div>
        <div style="line-height: 1em" class="mb-1">
          <p class="m-0">店&nbsp;&nbsp;{{ post.shop_name }}</p>
          <p class="m-0">メニュー</p>
          <ul v-for="(menu, idx) in post.menu" :key="idx" class="m-0">
            <li>{{ menu.name }}&nbsp;&nbsp;¥{{ menu.price }}</li>
          </ul>
          <p>{{ post.message }}</p>
        </div>
      </div>
    </div>
  </div>
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
      // menus: [],
    }
  },
  mounted() {
    this.posts = this.$axios
      .get(`/mock/posts/communities/0`)
      .then((res) => (this.posts = res.data))

    // for (const post of this.posts) {
    //   for (const list of post.menu) {
    //     this.menus.push(list.name)
    //   }
    // }
  },
}
</script>
