<template>
  <!-- <div class="row"> -->
  <table v-if="isLoggedin" class="table table-borderless my-2">
    <tbody>
      <tr>
        <td class="align-middle m-0 p-0">
          <CommodalForIndex style="width: 20vw" />
        </td>
        <td class="align-middle m-0 p-0">
          <Storylike :community-list="communityList" style="width: 80vw" />
        </td>
      </tr>
    </tbody>
  </table>
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
        .get('/api/users/communities')
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
