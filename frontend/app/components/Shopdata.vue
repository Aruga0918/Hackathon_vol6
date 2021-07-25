<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="py-1 col col-md-9">
        <div class="primary_shopdata d-flex" style="height: 20vh">
          <img :src="shopdata.icon_url" style="object-fit: scale-down" />
          <div class="d-inline-block ml-auto mr-auto" style="margin-top: 16px">
            <div class="primarydata mr-auto">
              <big style="height: 20%; font-weight: bold">{{
                shopdata.name
              }}</big>
              <!-- <p style="height:20% color:gray">ジャンル: {{ ShopCategory }}</p> -->
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="ShopDetails">
      <p>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-door-open"
          viewBox="0 0 16 16"
        >
          <path
            d="M8.5 10c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z"
          />
          <path
            d="M10.828.122A.5.5 0 0 1 11 .5V1h.5A1.5 1.5 0 0 1 13 2.5V15h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V1.5a.5.5 0 0 1 .43-.495l7-1a.5.5 0 0 1 .398.117zM11.5 2H11v13h1V2.5a.5.5 0 0 0-.5-.5zM4 1.934V15h6V1.077l-6 .857z"
          />
        </svg>
        {{ shopdata.description }}
      </p>
      <p>
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
          />
        </svg>
        {{ shopdata.address }}
      </p>
    </div>
    <div>
      <b-tabs
        content-class="mt-3"
        nav-class="justify-content-center"
        active-nav-item-class="font-weight-bold text-uppercase text-danger"
      >
        <b-tab title="ランキング" active>
          <b-container class="commlist">
            <div
              v-for="(ranking, index) in rankings"
              :key="index"
              class="d-flex"
              style="
                align-items: center;
                justify-content: center;
                border-bottom-style: ridge;
                height: 100px;
              "
            >
              <div class="d-flex" style="align-items: center; width: 70%">
                <img
                  :src="require(`~/assets/${rankIcon[index]}`)"
                  class="d-inline-block"
                  style="height: 40px; float: left"
                />
                <div
                  class="d-inline-block ml-auto mr-auto"
                  style="width: 260px"
                >
                  <p class="d-inline ml-auto">
                    {{ ranking.name }}
                  </p>
                  <p class="small mb-1">
                    価格: {{ ranking.price }} 投稿数:{{ ranking.posted_cnt }}
                  </p>
                </div>
              </div>
            </div>
          </b-container>
        </b-tab>
        <b-tab title="メニュー">
          <b-container class="menulist">
            <div
              v-for="menu in shopdata.menu"
              :key="menu.id"
              class="d-flex"
              style="
                align-items: center;
                justify-content: center;
                border-bottom-style: ridge;
                height: 50px;
              "
            >
              <div class="d-flex" style="align-items: center; width: 100%">
                <div class="d-flex ml-auto mr-auto" style="width: 90%">
                  <p class="d-inline-block mr-auto my-auto">
                    <a>{{ menu.name }}</a>
                  </p>
                  <p class="d-inline-block ml-auto my-auto">
                    <a>{{ menu.price }}</a>
                  </p>
                  <!-- <p style="font-size: 6px">価格: {{ menu.price }}</p> -->
                </div>
              </div>
            </div>
          </b-container>
        </b-tab>
        <b-tab title="投稿一覧">
          <div v-for="(post, idx) in posts" :key="idx">
            <user-post :post="post" />
            <hr class="my-1" />
          </div>
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  props: {
    shopdata: {
      type: Object,
      required: true,
    },
  },
  data: () => {
    return {
      rankings: [],
      rankIcon: ['f3-1.png', 'f3-2.png', 'f3-3.png'],
      posts: [],
    }
  },
  computed: {
    ...mapState({
      communityId: (state) => state.community.id,
    }),
  },
  mounted() {
    const params = {
      n_cnt: this.rankIcon.length,
      community_id: this.communityId,
    }
    this.$api
      .get(`/api/rankings/shops/${this.$route.params.shopId}`, { params })
      .then((res) => {
        const data = res.data
        this.rankings = data.slice(
          0,
          Math.min(data.length, this.rankIcon.length)
        )
      })
      .catch((e) => {
        console.error(e)
      })
    this.$api
      .get(`/api/posts/shops/${this.$route.params.shopId}`)
      .then((res) => {
        this.posts = res.data
        console.log(this.posts)
      })
      .catch((e) => {
        console.error(e)
      })
  },
}
</script>

<style scoped>
.primary_shopdata {
  margin-bottom: 1%;
}

.ShopDetails p {
  margin-bottom: 1%;
}
</style>
