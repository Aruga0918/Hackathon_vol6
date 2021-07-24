<template>
  <div class="wrapper" style="min-height: 100vh; position: relative">
    <div style="height: 100%; display: flex; border-bottom-style: ridge">
      <CommodalForIndex
        class="d-inline-block"
        style="width: 15%; margin-top: 0"
      />
      <Storylike class="d-inline-block" style="width: 70%" />
      <img
        src="~/static/common.png"
        class="mx-auto"
        style="
          margin-top: 5px;
          height: 30px;
          width: 30px;
          border: 1px solid;
          border-radius: 50%;
        "
      />
    </div>
    <Post style="z-index: 100; position: sticky; top: 85vh; left: 65vh" />
    <Timeline />
  </div>
</template>

<script>
import CommodalForIndex from '../components/CommodalForIndex.vue'
import Post from '../components/Post.vue'
export default {
  components: { Post, CommodalForIndex },
}
</script>
