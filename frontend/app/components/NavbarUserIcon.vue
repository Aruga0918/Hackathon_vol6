<template>
  <b-nav-item-dropdown right>
    <template #button-content>
      <img
        v-if="existIconUrl"
        :src="user.icon_url"
        style="border-radius: 50%"
        height="30px"
      />
      <img
        v-else
        src="@/assets/person.png"
        style="border-radius: 50%"
        height="30px"
      />
    </template>
    <b-dropdown-item
      :to="{
        name: 'user-userId',
        params: {
          userId: user.id,
        },
      }"
      nuxt
      >プロフィール</b-dropdown-item
    >
    <b-dropdown-item @click="signout">ログアウト</b-dropdown-item>
  </b-nav-item-dropdown>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
export default {
  computed: {
    ...mapState({
      user: (state) => state.user,
    }),
    existIconUrl() {
      return ![null, undefined].includes(this.user.icon_url)
    },
  },
  methods: {
    ...mapMutations({ storeSignout: 'storeSignout' }),
    signout() {
      localStorage.clear()
      this.storeSignout()
      this.$router.replace('/')
    },
  },
}
</script>
