<template>
  <div class="container" style="text-align: center">
    <div class="row" style="width: 100%">
      <div
        v-for="category in categories"
        :key="category.id"
        class="card col-6 col-xs-6 col-sm-6 col-md-6"
      >
        <nuxt-link
          class="nlink"
          :to="{
            name: 'category-categoryId-shop',
            params: { categoryId: category.id },
          }"
        >
          <div class="filter">
            <img class="card-img" :src="category.IconUrl" alt="" />
          </div>
          <div class="card-img-overlay">
            <p class="text-white">{{ category.CategoryName }}</p>
          </div>
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  asyncData() {
    const categories = require(`~/assets/category.json`)
    return {
      categories,
    }
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
