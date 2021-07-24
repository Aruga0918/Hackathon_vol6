<template>
  <div class="Container" style="vertical-align: center">
    <div class="primary_shopdata d-flex" style="height: 20vh">
      <img :src="shopdata.icon_url" style="object-fit: scale-down" />
      <div class="d-inline-block ml-auto mr-auto" style="margin-top: 16px">
        <div class="primarydata mr-auto">
          <big style="height: 20%; font-weight: bold">{{ shopdata.name }}</big>
          <!-- <p style="height:20% color:gray">ジャンル: {{ ShopCategory }}</p> -->
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
          class="bi bi-cash-coin"
          viewBox="0 0 16 16"
        >
          <path
            fill-rule="evenodd"
            d="M11 15a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm5-4a5 5 0 1 1-10 0 5 5 0 0 1 10 0z"
          />
          <path
            d="M9.438 11.944c.047.596.518 1.06 1.363 1.116v.44h.375v-.443c.875-.061 1.386-.529 1.386-1.207 0-.618-.39-.936-1.09-1.1l-.296-.07v-1.2c.376.043.614.248.671.532h.658c-.047-.575-.54-1.024-1.329-1.073V8.5h-.375v.45c-.747.073-1.255.522-1.255 1.158 0 .562.378.92 1.007 1.066l.248.061v1.272c-.384-.058-.639-.27-.696-.563h-.668zm1.36-1.354c-.369-.085-.569-.26-.569-.522 0-.294.216-.514.572-.578v1.1h-.003zm.432.746c.449.104.655.272.655.569 0 .339-.257.571-.709.614v-1.195l.054.012z"
          />
          <path
            d="M1 0a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h4.083c.058-.344.145-.678.258-1H3a2 2 0 0 0-2-2V3a2 2 0 0 0 2-2h10a2 2 0 0 0 2 2v3.528c.38.34.717.728 1 1.154V1a1 1 0 0 0-1-1H1z"
          />
          <path
            d="M9.998 5.083 10 5a2 2 0 1 0-3.132 1.65 5.982 5.982 0 0 1 3.13-1.567z"
          />
        </svg>
        {{ shopdata.budget }}
      </p>
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
                  style="height: 100px; width: 100px; float: left"
                />
                <div
                  class="d-inline-block ml-auto mr-auto"
                  style="width: 260px"
                >
                  <p class="d-inline ml-auto">
                    <a>{{ ranking.name }}</a>
                  </p>
                  <p style="font-size: 6px">
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
              v-for="(menu, idx) in shopdata.menu"
              :key="idx"
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
