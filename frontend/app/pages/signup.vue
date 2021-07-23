<template>
  <div id="container" class="container">
    <div class="row justify-content-center">
      <div class="py-5 col col-md-4">
        <img
          class="d-block mx-auto mb-0"
          src="@/assets/fooriend_logo_bland_color.png"
          width="100"
        />
        <h4 class="text-center mb-3" style="color: #f44336">fooriend</h4>
        <h3 class="text-center">アカウント作成</h3>
        <div v-if="failed" class="alert alert-danger" role="alert">
          {{ errorMessage }}
        </div>
        <form>
          <div class="form-group">
            <label>ユーザー名</label>
            <input
              v-model="username"
              class="form-control"
              type="text"
              required
            />
          </div>
          <div class="form-group">
            <label>ユーザーid</label>
            <input v-model="userId" class="form-control" type="text" required />
          </div>
          <div class="form-group">
            <label>パスワード</label>
            <input
              v-model="password1"
              class="form-control"
              type="password"
              required
            />
          </div>
          <div class="form-group">
            <label>パスワード（確認）</label>
            <input
              v-model="password2"
              class="form-control"
              type="password"
              required
            />
          </div>
          <p
            v-if="isSamePassword && !emptyPassword"
            class="text-success"
            role="alert"
          >
            <span
              class="glyphicon glyphicon-exclamation-sign"
              aria-hidden="true"
            ></span>
            パスワードが一致しました
          </p>
          <p v-else-if="!isSamePassword" class="text-danger" role="alert">
            <span
              class="glyphicon glyphicon-exclamation-sign"
              aria-hidden="true"
            ></span>
            パスワードが一致しません
          </p>

          <div class="form-group">
            <button
              type="button"
              class="btn btn-primary btn-block"
              tabindex="-1"
              role="button"
              aria-disabled="true"
              :disabled="!isSamePassword || emptyPassword || emptyUsername"
              @click="onSubmit"
            >
              登録
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable no-console */
export default {
  data() {
    return {
      username: '',
      userId: '',
      password1: '',
      password2: '',
      errorMessage: '',
      failed: false,
    }
  },
  computed: {
    emptyUsername() {
      return this.username === ''
    },
    emptyPassword() {
      return this.password1 === '' || this.password2 === ''
    },
    isSamePassword() {
      return this.password1 === this.password2
    },
  },
  created() {
    if (localStorage.getItem('accessToken') !== null) {
      this.$router.push('/')
    }
  },
  methods: {
    onSubmit() {
      const form = {
        uid: this.userId,
        username: this.username,
        password: this.password1,
      }
      this.$api
        .post('/api/auth/signup', form)
        .then((res) => {
          console.log(res.data)
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
          this.failed = false
          this.$router.go(-1)
          alert('アカウント作成に成功しました')
        })
        .catch((e) => {
          console.error(e)
          this.failed = true
          console.error(e)
          this.errorMessage = 'アカウント作成に失敗しました'
        })
    },
  },
}
</script>
