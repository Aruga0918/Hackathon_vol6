<template>
  <div class="container">
    <div class="row justify-content-center my-5">
      <div class="col col-md-10">
        <p v-if="isLogin" class="text-center">user name : {{ displayName }}</p>
        <div class="my-4">
          <b-card bg-variant="light">
            <b-form-group
              label-cols-lg="3"
              label="sign up"
              label-size="lg"
              label-class="font-weight-bold pt-0"
              class="mb-0"
            >
              <b-form-group
                label="username"
                label-cols-sm="3"
                label-align-sm="right"
              >
                <b-form-input v-model="username" type="text"></b-form-input>
              </b-form-group>

              <b-form-group
                label="user id"
                label-cols-sm="3"
                label-align-sm="right"
              >
                <b-form-input v-model="signupUserid" type="text"></b-form-input>
              </b-form-group>
              <b-form-group
                label="password"
                label-cols-sm="3"
                label-align-sm="right"
              >
                <b-form-input
                  v-model="signupPassword1"
                  type="password"
                ></b-form-input>
              </b-form-group>
              <b-form-group
                label="password"
                label-cols-sm="3"
                label-align-sm="right"
              >
                <b-form-input
                  v-model="signupPassword2"
                  type="password"
                ></b-form-input>
              </b-form-group>
            </b-form-group>
            <b-button type="button" variant="primary" @click="signup"
              >sign up</b-button
            >
          </b-card>
        </div>

        <p v-if="loginFailed" class="alert alert-danger">
          ログインに失敗しました
        </p>
        <div class="my-4">
          <b-card bg-variant="light">
            <b-form-group
              label-cols-lg="3"
              label="login"
              label-size="lg"
              label-class="font-weight-bold pt-0"
              class="mb-0"
            >
              <b-form-group
                label="user id"
                label-cols-sm="3"
                label-align-sm="right"
              >
                <b-form-input v-model="userid" type="text"></b-form-input>
              </b-form-group>

              <b-form-group
                label="password"
                label-cols-sm="3"
                label-align-sm="right"
              >
                <b-form-input v-model="password" type="password"></b-form-input>
              </b-form-group>
            </b-form-group>
            <b-button type="button" variant="primary" @click="login"
              >login</b-button
            >
            <b-button type="button" variant="danger" @click="logout"
              >logout</b-button
            >
          </b-card>
        </div>

        <div>
          <h4 class="text-center">template databaseの中身</h4>
          <b-button @click="getDatabase">更新</b-button>
          <div>
            <b-table striped hover :items="items"></b-table>
          </div>
        </div>

        <div class="my-4">
          <b-form inline>
            <b-form-input
              v-model="description"
              class="mb-2 mr-sm-2 mb-sm-0"
              placeholder="post contents"
            ></b-form-input>

            <b-button variant="primary" @click="post">post</b-button>
          </b-form>
          <p v-if="postFailed" class="text-danger">postに失敗しました</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable no-console */
export default {
  data() {
    return {
      displayName: '',
      userid: '',
      password: '',
      signupUserid: '',
      signupPassword1: '',
      signupPassword2: '',
      username: '',
      loginFailed: false,
      isLogin: false,
      postFailed: false,
      description: '',
      items: [],
    }
  },
  computed: {},
  mounted() {
    this.getDatabase()
  },
  methods: {
    login() {
      const form = { uid: this.userid, password: this.password }
      this.$api
        .post('/api/auth/signin', form)
        .then((res) => {
          const accessToken = res.data.access_token
          const refreshToken = res.data.refresh_token
          this.displayName = res.data.username
          localStorage.setItem('accessToken', accessToken)
          localStorage.setItem('refreshToken', refreshToken)
          this.isLogin = true
          this.loginFailed = false
          console.log(localStorage.getItem('accessToken'))
        })
        .catch(() => {
          this.loginFailed = true
        })
      this.userid = ''
      this.password = ''
    },
    signup() {
      if (
        this.signupPassword1 === this.signupPassword2 &&
        this.signupPassword1 !== '' &&
        this.signupUserid !== '' &&
        this.username !== ''
      ) {
        const form = {
          uid: this.signupUserid,
          password: this.signupPassword1,
          username: this.username,
        }
        this.$api
          .post('/api/auth/signup', form)
          .then((res) => {
            const accessToken = res.data.access_token
            const refreshToken = res.data.refresh_token
            localStorage.setItem('accessToken', accessToken)
            localStorage.setItem('refreshToken', refreshToken)
            this.displayName = res.data.username
            this.isLogin = true
            this.loginFailed = false
            console.log(localStorage.getItem('accessToken'))
          })
          .catch(() => {
            console.error('signup error')
          })
      }
      this.signupPassword1 = ''
      this.signupPassword2 = ''
      this.username = ''
      this.signupUserid = ''
    },
    logout() {
      localStorage.setItem('accessToken', null)
      localStorage.setItem('refreshToken', null)
      console.log(localStorage.getItem('accessToken'))
      this.isLogin = false
    },
    post() {
      const form = { description: this.description }
      this.$api
        .post('/api/template', form)
        .then(() => {
          this.postFailed = false
          this.getDatabase()
        })
        .catch(() => {
          this.postFailed = true
          console.error("can't post description")
        })
    },
    getDatabase() {
      this.$api
        .get('/api/template')
        .then((res) => {
          this.refreshItems(res.data)
        })
        .catch(() => {
          console.error("can't get database data")
        })
    },
    refreshItems(items) {
      this.items = items
    },
  },
}
</script>
