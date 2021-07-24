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
          :src="shop.img"
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
// 例:http://localhost:3000/category/1で和食を出す
export default {
  asyncData() {
    const Shoplist = require(`~/assets/shopdata.json`)
    const categories = require(`~/assets/category.json`)
    return {
      Shoplist,
      categories,
    }
  },
  data() {
    return {
      shops: [],
    }
  },
  mounted() {
    // window: (onload = function () {
    const id = this.$route.params.categoryId
    const category = this.categories[id - 1].CategoryName
    for (const i of this.Shoplist) {
      if (i.category === category) {
        this.shops.push(i)
      }
    }
    // }),

    // async getEventInfo() {
    //   this.shops = await this.$axios
    //     .get('mock/categories/this.$route.params.categoryId/shops')
    //     .then((res) => res.data)
    // },
    // console.log(this.shops)
  },
}
</script>
