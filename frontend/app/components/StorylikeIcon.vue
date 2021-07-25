<template>
  <div>
    <img
      v-if="community.icon_url"
      :class="[{ active: selected, nonactive: !selected }]"
      :src="community.icon_url"
      width="50"
    />
    <img
      v-else
      :class="[{ active: selected, nonactive: !selected }]"
      src="@/assets/community.png"
      width="50"
    />
    <p
      class="text-center small mb-1"
      style="
        max-width: 70px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      "
    >
      {{ community.name }}
    </p>
  </div>
</template>

<script>
export default {
  props: {
    community: {
      type: Object,
      required: true,
    },
    selected: {
      type: Boolean,
      required: true,
    },
  },
}
</script>

<style scoped>
.active {
  border-radius: 50%;
  border: 4px solid #f44336;
  vertical-align: middle;
}
.nonactive {
  border-radius: 50%;
  border: 1px solid #00cc00;
  vertical-align: middle;
}
.circle {
  vertical-align: middle;
  border-radius: 50%;
}
</style>
