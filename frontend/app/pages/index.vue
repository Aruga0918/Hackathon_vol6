<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="py-1 col col-md-9">
        <community-list :user-id="userId" />
        <div v-for="(post, idx) in posts" :key="idx">
          <user-post :post="post" />
          <hr class="my-1" />
        </div>
        <Post style="z-index: 100; position: sticky; top: 85vh; left: 65vh" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data: () => {
    return {
      posts: [],
    }
  },

  fetch() {
    this.$api
      .get(`/api/posts/communities/${this.communityId}`)
      .then((res) => {
        this.posts = res.data
      })
      .catch(() => {
        console.error(`/api/posts/communities/${this.communityId}`)
      })
  },
  computed: {
    ...mapState({
      userId: (state) => state.user.id,
      communityId: (state) => state.communityId,
    }),
  },
  watch: {
    communityId() {
      this.$api
        .get(`/api/posts/communities/${this.communityId}`)
        .then((res) => {
          this.posts = res.data
        })
        .catch(() => {
          console.error(`/api/posts/communities/${this.communityId}`)
        })
    },
  },
}
</script>
