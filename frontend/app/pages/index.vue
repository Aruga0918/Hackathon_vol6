<template>
  <div>
    <community-list :user-id="userId" />
    <hr class="m-0 p-0" />
    <div class="container">
      <div class="row justify-content-center">
        <div class="py-1 col col-md-9">
          <Post
            style="z-index: 100; position: sticky; top: 85vh; left: 65vh"
            :user-id="userId"
          />
          <p class="text-center">
            <strong class="bland-color">{{ community.name }}</strong
            >の投稿一覧
          </p>
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
      communityId: (state) => state.community.id,
      community: (state) => state.community,
    }),
  },
  watch: {
    communityId() {
      this.posts = []
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
