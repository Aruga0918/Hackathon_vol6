<template>
  <div>
    <CommodalForIndex
      class="d-inline-block"
      style="width: 15%; margin-top: 0; text-align: left"
    />

    <Storylike
      class="d-inline-block"
      style="width: 70%"
      :community-list="communityList"
      :is-loggedin="isLoggedin"
    />

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
</template>

<script>
import { mapState } from 'vuex'
export default {
  props: {
    userId: {
      type: Number,
      required: true,
    },
  },
  data: () => {
    return {
      communityList: [],
    }
  },
  fetch() {
    if (this.isLoggedin) {
      this.$api
        .get('/users/communities')
        .then((res) => {
          this.communityList = res.data
        })
        .catch((e) => {
          console.error(e)
        })
    } else {
      console.log('no login')
    }
  },
  computed: {
    ...mapState({
      isSignin: (state) => state.isSignin,
    }),
    isLoggedin() {
      return ![null, undefined].includes(this.userId) && this.isSignin
    },
  },
}
</script>
