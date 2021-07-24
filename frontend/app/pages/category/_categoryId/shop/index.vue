<template>
  <b-container class="shoplist">
    <div
      v-for="shop in shops"
      :key="shop.name"
      class="d-flex"
      style="
        align-items: center;
        justify-content: center;
        border-bottom-style: ridge;
        height: 150px;
      "
    >
      <div class="d-flex" style="align-items: center; width: 100%">
        <img
          :src="shop.icon_url"
          class="d-inline-block"
          style="height: 100px; width: 100px; float: left"
        />
        <div class="d-inline-block ml-auto mr-auto" style="width: 260px">
          <p class="d-inline ml-auto">
            <NuxtLink
              :to="{
                name: 'category-categoryId-shop-shopId',
                params: {
                  categoryId: $route.params.categoryId,
                  shopId: shop.id,
                },
              }"
              >{{ shop.name }}</NuxtLink
            >
          </p>
          <p style="font-size: 6px">{{ shop.opentime }}</p>
        </div>
      </div>
    </div>
  </b-container>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data() {
    return {
      shops: [],
      // Shoplist: [],
    }
  },

  computed: {
    ...mapState({
      communityId: (state) => state.communityId,
    }),
  },
  mounted() {
    const params = {
      community_id: this.communityId,
    }
    this.$api
      .get(`api/categories/${this.$route.params.categoryId}/shops`, {
        params,
      })
      .then((res) => {
        this.shops = res.data
      })
  },
}
</script>
