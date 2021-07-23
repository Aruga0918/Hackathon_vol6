<template>
  <b-nav-item-dropdown right>
    <template #button-content>
      <img
        v-if="icon_url !== null"
        :src="icon_url"
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
          userId: userId,
        },
      }"
      nuxt
      >プロフィール</b-dropdown-item
    >
    <b-dropdown-item @click="signout">ログアウト</b-dropdown-item>
  </b-nav-item-dropdown>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  computed: {
    icon_url() {
      return localStorage.getItem('user_icon_url')
    },
    userId() {
      return localStorage.getItem('uid')
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
