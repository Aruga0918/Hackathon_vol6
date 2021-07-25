<template>
  <div class="m-0">
    <div class="d-flex align-middle" style="overflow-x: scroll; width: 100%">
      <storylike-icon
        :community="publicCommunity"
        :selected="communityId === publicCommunity.id"
        @click="storeCommunity(publicCommunity)"
      />
      <template v-for="(community, idx) in communityList">
        <div :key="idx" @click="storeCommunity(community)">
          <storylike-icon
            :community="community"
            :selected="communityId === community.id"
          />
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  props: {
    communityList: {
      type: Array,
      required: true,
    },
  },
  data: () => {
    return {
      publicCommunity: {
        name: 'public community',
        id: 0,
      },
    }
  },
  computed: {
    ...mapState({
      communityId: (state) => state.community.id,
    }),
  },
  methods: {
    ...mapMutations({ storeCommunity: 'storeCommunity' }),
  },
}
</script>
