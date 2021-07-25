<template>
  <b-container class="commlist">
    <div
      v-for="(comm, idx) in belongings"
      :key="idx"
      class="d-flex"
      style="
        align-items: center;
        justify-content: center;
        border-top-style: ridge;
        border-bottom-style: groove;
        height: 100px;
      "
    >
      <div class="d-flex" style="align-items: center; width: 85%">
        <img
          v-if="comm.icon_url"
          :src="comm.icon_url"
          class="d-inline-block"
          style="border-radius: 50%; height: 60px; width: 60px; float: left"
        />
        <img
          v-else
          src="@/assets/community.png"
          class="d-inline-block"
          style="border-radius: 50%; height: 60px; width: 60px; float: left"
        />
        <div class="d-inline-block ml-auto mr-auto" style="width: 260px">
          <!-- <b-nav-item-dropdown text="詳細" right style="list-style: none">
            <b-dropdown-item href="#"
              >メンバー：{{ comm.member_cnt }}</b-dropdown-item
            >
            <b-dropdown-item><Invite :commid="comm.id" /></b-dropdown-item>
          </b-nav-item-dropdown> -->
          <NuxtLink :to="{ name: `community-id`, params: { id: comm.id } }">
            <big class="d-inline ml-auto">{{ comm.name }}</big>
          </NuxtLink>
        </div>

        <b-button
          v-if="comm.is_join"
          size="sm"
          variant="danger"
          class="mb-2 my-sm-0"
          type="submit"
          style="
            float: right;
            vertical-align: middle;
            color: white;
            background-color: #ba000d;
          "
          @click="Delete(comm.id)"
          >退会</b-button
        >
        <b-button
          v-else
          size="sm"
          variant="danger"
          class="mb-2 my-sm-0"
          type="submit"
          style="
            float: right;
            vertical-align: middle;
            color: white;
            background-color: #ba000d;
          "
          @click="Participate(comm.id)"
          >参加</b-button
        >
      </div>
    </div>
    {{ $route.params.userId }}
  </b-container>
</template>

<script>
export default {
  props: {
    belongings: {
      type: Array,
      required: true,
    },
  },

  mounted() {
    console.log(this.belongings)
  },
  methods: {
    Delete(id) {
      const url = `/api/communities/${id}/members/${this.$route.params.userId}`
      this.$api
        .delete(url)
        .then(() => {
          alert('退会しました')
        })
        .catch(() => {
          alert('An error occured')
        })
      console.log(url)
    },
    Participate(id) {
      const url = `/api/communities/${id}/join`
      this.$api
        .post(url)
        .then(() => {
          alert('参加しました')
        })
        .catch(() => {
          alert('An error occured')
        })
    },
  },
  // data() {
  //   return {
  //     comms: [
  //       { name: 'ベネ英語科', imglink: 'hoge' },
  //       { name: 'ガストしか勝たん', imglink: 'hogehoge' },
  //       { name: 'ラーメンハオチー', imglink: 'hogeege' },
  //       { name: '３年B組', imglink: 'hohoho' },
  //     ],
  //   }
  // },
}
</script>
