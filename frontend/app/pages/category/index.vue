<template>
  <section class="container">
    <div>
      <app-logo />
      <h1 class="title">
        {{ name }}
      </h1>
      <h2 class="subtitle">
        {{ description }}
      </h2>
    </div>
  </section>
</template>

<script>
import AppLogo from '~/components/Logo.vue'
export default {
  components: {
    AppLogo,
  },
  data: () => {
    return {
      name: 'category page',
    }
  },
}
</script>
