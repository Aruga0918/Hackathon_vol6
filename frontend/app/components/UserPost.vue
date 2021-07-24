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
          >店&nbsp;&nbsp;{{ post.shop_name }}</nuxt-link
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
