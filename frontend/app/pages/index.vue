<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="py-1 col col-md-9">
        <community-list :user-id="userId" />
        <Post style="z-index: 100; position: sticky; top: 85vh; left: 85%" />
        <div v-for="(post, idx) in posts" :key="idx" style="z-index: -1">
          <user-post :post="post" />
          <hr class="my-1" />
        </div>
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
