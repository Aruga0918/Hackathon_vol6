<template>
  <div class="d-flex">
    <div style="width: 15%" class="mr-1" @click="goProfPage">
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
    <div style="width: 85%">
      <div
        class="d-flex m-0 p-0"
        style="line-height: 0.5em"
        @click="goProfPage"
      >
        <h6 class="m-0">
          {{ post.user_name }}
        </h6>
        <small class="text-muted p-0 m-1">@{{ post.uid }}</small>
      </div>
      <div style="line-height: 1em" class="mb-1">
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
        <div @click="goPostDetailPage">
          <p class="m-0">メニュー</p>
          <ul v-for="(menu, idx) in post.menu" :key="idx" class="m-0">
            <li>{{ menu.name }}&nbsp;&nbsp;¥{{ menu.price }}</li>
          </ul>
          <p>{{ post.message }}</p>
        </div>
      </div>
      <p class="text-muted text-right">
        <small>{{ post.created_at }}</small>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  methods: {
    goPostDetailPage() {
      this.$router.push(`/post/${this.post.post_id}`)
    },
    goProfPage() {
      this.$router.push(`/user/${this.post.user_id}`)
    },
  },
}
</script>
