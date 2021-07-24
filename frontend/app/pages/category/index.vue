<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="py-1 col col-md-9">
        <div class="row">
          <div
            v-for="(category, idx) in categories"
            :key="idx"
            class="col-6 mt-1"
            @click="goShopListPage(category.id)"
          >
            <!-- <div v-for="(cj, _idx) in categoryJson" :key="_idx"> -->
            <div class="card bg-dark text-white">
              <img
                class="bd-placeholder-img bd-placeholder-img-lg card-img"
                width="100%"
                :src="categoryJson[category.name]"
              />
              <div class="card-img-overlay">
                <h5 class="card-title">
                  {{ category.name }}({{ category.shop_cnt }})
                </h5>
              </div>
            </div>
            <!-- </div> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import categoryJson from '@/assets/categories.json'
export default {
  data: () => {
    return {
      categories: [],
      categoryJson,
    }
  },

  fetch() {
    this.$api
      .get('/api/categories')
      .then((res) => {
        this.categories = res.data
        console.log(this.categories)
      })
      .catch((e) => {
        console.error(e)
      })
  },
  methods: {
    goShopListPage(categoryId) {
      this.$router.push(`/category/${categoryId}/shop`)
    },
  },
}
</script>

<style>
.nlink {
  width: 100%;
  height: 100%;
}

.card {
  padding: 0;
}
.filter {
  background-color: black;
  width: 100%;
  height: 100%;
}

.card-img {
  object-fit: cover;
  width: 100%;
  height: 100%;
  opacity: 0.5;
}
.card-img-overlay {
  padding: 0;
  top: calc(50% - 0.5rem);
  text-align: center;
  font-weight: bold;
  font-size: 30px;
}
</style>
