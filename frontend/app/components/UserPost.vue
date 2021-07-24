<template>
  <div class="d-flex">
    <div style="width: 15%" class="mr-1">
      <b-img
        v-if="post.user_icon_url"
        :src="post.user_icon_url"
        style="object-fit: contain; border-radius: 50%; width: 100%"
      />
      <b-img
        v-else
        src="@/assets/person.png"
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
        <ul v-for="menu in post.menu" :key="menu.menu_id" class="m-0">
          <li>{{ menu.name }}&nbsp;&nbsp;¥{{ menu.price }}</li>
        </ul>
        <p>{{ post.message }}</p>
      </div>
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
}
</script>
