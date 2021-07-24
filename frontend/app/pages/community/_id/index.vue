<template>
  <div>
    <div class="row justify-content-center mx-1 mt-3">
      <div class="py-1 col col-md-8">
        <div class="d-flex">
          <div style="width: 20%" class="mr-1">
            <b-img
              v-if="community.comm_icon_url"
              :src="community.comm_icon_url"
              style="object-fit: contain; border-radius: 50%; width: 100%"
            />
            <b-img
              v-else
              src="~/assets/community.png"
              style="object-fit: contain; border-radius: 50%; width: 100%"
            />
          </div>
          <div style="width: 80%">
            <big style="my-auto">{{ community.name }}</big>
          </div>
        </div>

        <p>{{ community.description }}</p>

        <b-tabs
          content-class="mt-3"
          nav-class="justify-content-center"
          active-nav-item-class="font-weight-bold text-uppercase text-danger"
        >
          <b-tab title="ユーザー" active>
            <b-container class="userlist">
              <Invite :commid="community.id" />
              <div v-for="(member, id) in community.members" :key="id">
                <user-data :member="member" style="border: none" />
                <hr class="my-1" />
              </div>
            </b-container>
          </b-tab>
          <b-tab title="投稿">
            <b-container class="postlist">
              <div v-for="(post, idx) in posts" :key="idx">
                <user-post :post="post" />
                <hr class="my-1" />
              </div>
            </b-container>
          </b-tab>
        </b-tabs>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      community: [],
      posts: [],
    }
  },
  async fetch() {
    // this.community = this.$axios
    //   .get(`/mock/communities/${this.$route.params.id}`)
    //   .then((res) => {
    //     this.community = res.data
    //     console.log(this.community)
    //   })
    const community = await this.$axios.get(
      `/mock/communities/${this.$route.params.id}`
    )
    this.community = community.data

    // this.posts = this.$axios
    //   .get(`/mock/posts/communities/${this.$route.params.id}`)
    //   .then((res) => {
    //     this.posts = res.data
    //   })
    const posts = await this.$axios.get(
      `/mock/posts/communities/${this.$route.params.id}`
    )
    this.posts = posts.data
  },
}
</script>
