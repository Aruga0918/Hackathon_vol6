<template>
  <div style="text-align: center">
    <b-button
      v-b-modal.modal-1
      class="btn-circlelg"
      style="
        color: #cddc39;
        border-color: #cddc39;
        border: solid;
        background-color: white;
        line-height: 36px;
      "
      >＋</b-button
    >
    <!-- <p class="small text-center">作成</p> -->

    <b-modal id="modal-1" title="コミュニティ新規作成" @ok="submit">
      <div class="creater">
        <form action="" method="post">
          <label for="ComunityName"
            >作成するコミュニティの名前を記入してください</label
          >
          <input
            id="ComunityName"
            v-model="community_name"
            class="form-control"
            type="text"
            name="ComunityName"
          />
        </form>
        <br />
        <form action="" method="post">
          <label for="ComunityDescription">説明</label>
          <br />
          <input
            id="ComunityDescription"
            v-model="description"
            class="form-control"
            type="text"
            name="ComunityDescription"
            placeholder="任意"
          />
        </form>
        <br />
        <form action="" method="post">
          <div class="row d-inline-block" style="padding: 0px 16px">
            <div class="col-xs-8">
              <label for="Invitation">メンバー招待</label>
              <br />
              <!-- <input
                id="Invitation"
                v-model="memberID"
                class="form-control"
                type="text"
                name="Invitation"
                placeholder="ユーザーID"
              /> -->
              <b-form-input
                id="Invitation"
                v-model="memberID"
                placeholder="ユーザーID"
                list="candidates"
              ></b-form-input>
              <datalist id="candidates">
                <option
                  v-for="member in allmembers"
                  :key="member.uid"
                  :value="member.id"
                >
                  {{ member.uid }}
                </option>
              </datalist>
            </div>
          </div>
          <!-- type = buttonにすると閉じない -->
          <button
            type="button"
            class="btn btn-danger btn-circle btn-circle-sm m-1 d-inline-block"
            @click="AddInvite"
          >
            ＋
          </button>
        </form>
        <li
          v-for="(member, idx) in members"
          :key="idx"
          class="d-inline-block"
          style="width: 50%"
        >
          {{ member.uid }}
          <b-button
            variant="outline-secondary"
            type="button"
            @click="Remove(member)"
            >削除</b-button
          >
        </li>
      </div>
    </b-modal>
  </div>
</template>

<script>
export default {
  data() {
    return {
      members: [],
      memberID: '',
      community_name: '',
      description: '',
      allmembers: [],
      // alldata: [],
    }
  },
  async fetch() {
    await this.$api.get(`api/users`).then((res) => {
      this.allmembers = res.data
    })
    // for (const part of this.alldata) {
    //   this.allmembers.push({part.uid : part.id})
    // }
  },
  methods: {
    AddInvite() {
      this.members.push(this.memberID)
    },
    Remove(target) {
      const index = this.members.indexOf(target)
      this.members.splice(index, 1)
      // splice(始まり,消去数)
    },
    submit() {
      const url = '/api/communities/create'
      const params = {
        community_name: this.community_name,
        description: this.description,
        members: this.members,
      }
      this.$api
        .post(url, params)
        .then(() => {
          alert('created')
        })
        .catch(() => {
          alert('An error occured')
        })
    },
  },
}
</script>

<style scoped>
.btn-circle {
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  vertical-align: center;
  padding: 0px;
  font-weight: bold;
  font-size: 20px;
  border-radius: 50%;
}
.btn-circlelg {
  width: 40px;
  height: 40px;
  line-height: 40px;
  text-align: center;
  vertical-align: center;
  padding: 0px;
  font-weight: bold;
  font-size: 27px;
  border-radius: 50%;
}
</style>
