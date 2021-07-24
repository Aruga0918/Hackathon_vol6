<template>
  <div iclass="container">
    <div class="row justify-content-center mx-1 mt-3">
      <div class="py-1 col col-md-8">
        <div class="d-flex mb-2" @click="goProfPage">
          <div style="width: 20%" class="mr-1">
            <b-img
              v-if="post.user_icon_url"
              :src="post.user_icon_url"
              class="icon-circle"
              style="object-fit: contain; border-radius: 50%; width: 100%"
            />
            <b-img
              v-else
              src="@/assets/person.png"
              class="icon-circle"
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
          <nuxt-link
            :to="{
              name: 'category-categoryId-shop-shopId',
              params: { categoryId: 0, shopId: post.shop_id },
            }"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-geo-alt"
              viewBox="0 0 16 16"
            >
              <path
                d="M12.166 8.94c-.524 1.062-1.234 2.12-1.96 3.07A31.493 31.493 0 0 1 8 14.58a31.481 31.481 0 0 1-2.206-2.57c-.726-.95-1.436-2.008-1.96-3.07C3.304 7.867 3 6.862 3 6a5 5 0 0 1 10 0c0 .862-.305 1.867-.834 2.94zM8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10z"
              />
              <path
                d="M8 8a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"
              /></svg
            >&nbsp;&nbsp;{{ post.shop_name }}</nuxt-link
          >
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
  fetch() {
    this.$axios
      .get(`/api/posts/${this.$route.params.postId}`)
      .then((res) => {
        this.post = res.data
      })
      .catch((e) => {
        console.error(e)
      })
  },
  methods: {
    goProfPage() {
      this.$router.push(`/user/${this.post.user_id}`)
    },
  },
}
</script>
