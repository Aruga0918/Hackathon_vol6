<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="py-5 col col-md-4">
        <img
          class="d-block mx-auto mb-0"
          src="@/assets/fooriend_logo_bland_color.png"
          width="100"
        />
        <h4 class="fooriend text-center mb-3" style="color: #f44336">
          fooriend
        </h4>
        <div v-if="failed" class="alert alert-danger">
          サインインに失敗しました
        </div>
        <form>
          <div class="form-group">
            <label for="userId">ユーザーid</label>
            <input
              id="userId"
              v-model="userId"
              type="text"
              class="mb-3 form-control"
              required
            />

            <label for="password">パスワード</label>
            <input
              id="password"
              v-model="password"
              type="password"
              class="mb-3 form-control"
              required
            />
            <button
              type="button"
              class="btn btn-primary btn-block"
              :disabled="userId === '' || password === ''"
              @click="onSubmit"
            >
              サインイン
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable no-console */
import { mapMutations } from 'vuex'
export default {
  data() {
    return {
      userId: '',
      password: '',
      failed: false,
    }
  },
  created() {
    if (localStorage.getItem('accessToken') !== null) {
      this.$router.push('/')
    }
  },
  methods: {
    ...mapMutations({
      storeSignin: 'storeSignin',
    }),
    onSubmit() {
      const form = {
        uid: this.userId,
        password: this.password,
      }
      this.$api
        .post('/api/auth/signin', form)
        .then((res) => {
          const data = res.data
          const accessToken = res.data.access_token
          const refreshToken = res.data.refresh_token
          localStorage.setItem('uid', data.uid)
          if (data.icon_url !== null) {
            localStorage.setItem('user_icon_url', data.icon_url)
          } else {
            localStorage.removeItem('user_icon_url')
          }
          localStorage.setItem('username', data.username)
          localStorage.setItem('accessToken', accessToken)
          localStorage.setItem('refreshToken', refreshToken)
          this.storeSignin()
          this.failed = false
          this.$router.go(-1)
        })
        .catch((e) => {
          console.error(e)
          this.failed = true
        })
    },
  },
}
</script>
