<template>
  <div iclass="container">
    <div class="row justify-content-center mx-1 mt-3">
      <div class="py-1 col col-md-8">
        <div class="d-flex mb-2">
          <div style="width: 20%" class="mr-1">
            <b-img
              :src="post.user_icon_url"
              style="object-fit: contain; border-radius: 50%; width: 100%"
            />
          </div>
          <div style="width: 70%">
            <big>{{ post.user_name }}</big>
            <p class="text-muted">@{{ post.uid }}</p>
          </div>
          <div style="width: 10%">
            <b-dropdown
              right
              size="sm"
              variant="link"
              toggle-class="text-decoration-none"
              no-caret
            >
              <template #button-content>
                <p>•••</p>
              </template>
              <b-dropdown-item>編集</b-dropdown-item>
              <b-dropdown-item>削除</b-dropdown-item>
            </b-dropdown>
          </div>
        </div>
        <div>
          <p>店&nbsp;&nbsp;{{ post.shop_name }}</p>
          <p class="m-0">メニュー</p>
          <ul v-for="(menu, idx) in post.menu" :key="idx" class="m-0">
            <li>{{ menu.name }}&nbsp;&nbsp;¥{{ menu.price }}</li>
          </ul>
          <div class="mb-3" />
          <p>{{ post.message }}</p>
        </div>
        <p class="text-muted text-right">
          <small>{{ post.created_at }}</small>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => {
    return {
      post: [],
    }
  },
  async fetch() {
    const post = await this.$axios.get(
      `/mock/posts/${this.$route.params.postId}`
    )
    this.post = post.data
  },
}
</script>
