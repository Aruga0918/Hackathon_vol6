<template>
  <div>
    <template v-if="isLoggedin">
      <ul class="horizontal-list">
        <template v-for="(community, idx) in communityList">
          <li :key="idx" class="item" @click="storeCommunityId(community.id)">
            <img
              v-if="community.icon_url"
              style="border-radius: 50%"
              :src="community.icon_url"
              width="30"
            />
            <img
              v-else
              style="border-radius: 50%"
              src="@/assets/community.png"
              width="30"
            />
          </li>
        </template>
      </ul>
    </template>
    <div v-else>ログインしましょう</div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  props: {
    communityList: {
      type: Array,
      required: true,
    },
    isLoggedin: {
      type: Boolean,
      required: true,
    },
  },
  methods: {
    ...mapMutations({ storeCommunityId: 'storeCommunityId' }),
  },
}
</script>

<style>
.horizontal-list {
  overflow-x: auto;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
  margin-bottom: 0%;
  padding-left: 0;
}

.item {
  /* 横スクロール用 */
  display: inline-block;

  /* 見た目調整 */
  height: 40px;
  margin: 5px;
  width: 40px;
}

.li img {
  height: 100%;
  width: 100%;
}
</style>
