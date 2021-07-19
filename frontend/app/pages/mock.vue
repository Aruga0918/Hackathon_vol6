<template>
  <div class="container">
    <div class="row justify-content-center my-5">
      <div class="col col-md-10">
        <h3>コミュニティAPI</h3>

        <table class="table">
          <tbody>
            <tr>
              <td><h5>コミュニティ情報取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getCommunityInfo"
                  >getCommunityInfo</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>コミュニティ作成API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="createCommunity"
                  >createCommunity</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>コミュニティ削除API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="deleteCommunity"
                  >deleteCommunity</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>コミュニティ編集API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="editCommunity"
                  >editCommunity</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>コミュニティ参加API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="joinCommunity"
                  >joinCommunity</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>コミュニティ参加拒否API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="cancelJoinCommunity"
                  >cancelJoinCommunity</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>ユーザー招待API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="inviteCommunity"
                  >inviteCommunity</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>ユーザー退会API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="withdrawCommunity"
                  >withdrawCommunity</b-button
                >
              </td>
            </tr>
          </tbody>
        </table>

        <h3>ユーザーAPI</h3>
        <table class="table">
          <tbody>
            <tr>
              <td><h5>ユーザー一覧取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getUsersInfo"
                  >getUsersInfo</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>ユーザー情報取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getUserInfo"
                  >getUserInfo</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>ユーザー削除API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="deleteUser"
                  >deleteUser</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>ユーザー編集API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="editUser"
                  >editUser</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>所属コミュニティ一覧取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getMyCommunities"
                  >getMyCommunities</b-button
                >
              </td>
            </tr>
          </tbody>
        </table>

        <h3>店舗API</h3>
        <table class="table">
          <tbody>
            <tr>
              <td><h5>店舗情報取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getShopInfo"
                  >getShopInfo</b-button
                >
              </td>
            </tr>
          </tbody>
        </table>

        <h3>投稿API</h3>

        <table class="table">
          <tbody>
            <tr>
              <td><h5>投稿取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getPostInfo"
                  >getPostInfo</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>ユーザー投稿取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getUserPostsInfo"
                  >getUserPostsInfo</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>ショップ投稿取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getShopPostsInfo"
                  >getShopPostsInfo</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>コミュニティ投稿取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getCommunityPostsInfo"
                  >getCommunityPostsInfo</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>新規投稿API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="postsData"
                  >postsData</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>投稿編集API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="editPostsData"
                  >editPostsData</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>投稿削除API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="deletePostsData"
                  >deletePostsData</b-button
                >
              </td>
            </tr>
          </tbody>
        </table>

        <h3>カテゴリAPI</h3>

        <table class="table">
          <tbody>
            <tr>
              <td><h5>カテゴリ一覧取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getCategoryList"
                  >getCategoryList</b-button
                >
              </td>
            </tr>
            <tr>
              <td><h5>ショップ一覧取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getShopList"
                  >getShopList</b-button
                >
              </td>
            </tr>
          </tbody>
        </table>

        <h3>ランキングAPI</h3>
        <table class="table">
          <tbody>
            <tr>
              <td><h5>ランキング取得API</h5></td>
              <td>
                <b-button
                  type="button"
                  variant="info"
                  size="sm"
                  @click="getRanking"
                  >getRanking</b-button
                >
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable no-console */
export default {
  data() {
    return {}
  },
  computed: {},
  mounted() {},
  methods: {
    async getCommunityInfo() {
      const res = await this.$axios.get('/mock/communities/1')
      console.log(res.data)
    },
    async createCommunity() {
      const params = {
        community_name: 'hoge',
        description: 'hogehoge',
        members: [1, 2, 3],
      }
      const res = await this.$axios.post('/mock/communities/create', params)
      console.log(res.data)
    },
    async deleteCommunity() {
      const res = await this.$axios.delete('/mock/communities/1')
      console.log(res)
    },
    async editCommunity() {
      const params = {
        community_name: 'hoge',
        description: 'hogehoge',
      }
      const res = await this.$axios.patch('/mock/communities/1', params)
      console.log(res)
    },
    async joinCommunity() {
      const res = await this.$axios.post('/mock/communities/1/join')
      console.log(res.data)
    },
    async cancelJoinCommunity() {
      const res = await this.$axios.delete('/mock/communities/1/join')
      console.log(res)
    },
    async inviteCommunity() {
      const params = {
        members: [1, 2, 3, 4],
      }
      const res = await this.$axios.patch('/mock/communities/1/add', params)
      console.log(res)
    },
    async withdrawCommunity() {
      const res = await this.$axios.delete('/mock/communities/1/members/1')
      console.log(res)
    },
    async getUserInfo() {
      const res = await this.$axios.get('/mock/users/1')
      console.log(res.data)
    },
    async getUsersInfo() {
      const res = await this.$axios.get('/mock/users')
      console.log(res.data)
    },
    async deleteUser() {
      const res = await this.$axios.delete('/mock/users/withdrawal')
      console.log(res)
    },
    async editUser() {
      const params = {
        user_name: 'user name',
        user_id: 1,
        password: 'hge',
      }
      const res = await this.$axios.patch('/mock/users/edit', params)
      console.log(res)
    },
    async getMyCommunities() {
      const res = await this.$axios.get('/mock/users/communities')
      console.log(res.data)
    },
    async getShopInfo() {
      const res = await this.$axios.get('/mock/shops/1')
      console.log(res.data)
    },
    async getPostInfo() {
      const res = await this.$axios.get('/mock/posts/1')
      console.log(res.data)
    },
    async getUserPostsInfo() {
      const res = await this.$axios.get('/mock/posts/users/1')
      console.log(res.data)
    },
    async getShopPostsInfo() {
      const res = await this.$axios.get('/mock/posts/shops/1')
      console.log(res.data)
    },
    async getCommunityPostsInfo() {
      const res = await this.$axios.get('/mock/posts/communities/1')
      console.log(res.data)
    },
    async postsData() {
      const res = await this.$axios.post('/mock/posts/users/1/shops/1')
      console.log(res)
    },
    async editPostsData() {
      const res = await this.$axios.patch('/mock/posts/1')
      console.log(res)
    },
    async deletePostsData() {
      const res = await this.$axios.delete('/mock/posts/1')
      console.log(res)
    },
    async getCategoryList() {
      const res = await this.$axios.get('/mock/categories')
      console.log(res.data)
    },
    async getShopList() {
      const params = { community_id: 1 }
      const res = await this.$axios.get('/mock/categories/1/shops', params)
      console.log(res.data)
    },
    async getRanking() {
      const params = { community_id: 1 }
      const res = await this.$axios.get('/mock/rankings/shops/1', params)
      console.log(res.data)
    },
  },
}
</script>

<style scoped>
h3 {
  border-left: solid 5px lightgray;
  padding-left: 10px;
  margin-top: 50px;
}
</style>
