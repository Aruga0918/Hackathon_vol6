<template>
  <div class="container" style="text-align: center">
    <div class="row" style="width: 90vh">
      <div v-for="category in categories" :key="category" class="card col-6">
        <img class="card-img" :src="category.IconUrl" alt="" />
        <div class="card-img-overlay">
          <p class="text-white">{{ category.CategoryName }}</p>
        </div>
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
