<template>
  <div iclass="container">
    <div class="row justify-content-center mx-1 mt-3">
      <div class="py-1 col col-md-8">
        <div class="d-flex">
          <div style="width: 20%" class="mr-1">
            <b-img
              v-if="user.icon_url"
              :src="user.icon_url"
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
          <div style="width: 80%">
            <big>{{ user.name }}</big>
            <p>@ {{ user.uid }}</p>
          </div>
        </div>

        <p class="text-break">{{ user.profile }}</p>

        <h5 class="text-center text-white bg-bland-color">投稿</h5>
        <div>
          <div v-for="(post, idx) in posts" :key="idx">
            <user-post :post="post" />
            <hr class="my-1" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => {
    return {
      posts: [],
      user: {},
    }
  },
  fetch() {
    this.$api
      .get(`/api/posts/users/${this.$route.params.userId}`)
      .then((res) => {
        this.posts = res.data
      })
      .catch((e) => {
        console.error(e)
      })
    this.$api
      .get(`/api/users/${this.$route.params.userId}`)
      .then((res) => {
        this.user = res.data
      })
      .catch((e) => {
        console.error(e)
      })
  },
}
</script>
