<template>
  <div style="text-align: right">
    <b-button v-b-modal.modal-2 variant="" style="margin-right: 16px"
      >メンバー招待</b-button
    >

    <b-modal id="modal-2" title="コミュニティ新規作成" @ok="submit">
      <div class="creater">
        <form action="" method="post">
          <div class="row d-inline-block" style="padding: 0px 16px">
            <div class="col-xs-8">
              <label for="Invitation">メンバー招待</label>
              <br />
              <input
                id="Invitation"
                v-model="memberID"
                class="form-control"
                type="text"
                name="Invitation"
                placeholder="ユーザーID"
              />
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
          v-for="member in members"
          :key="member"
          class="d-inline-block"
          style="width: 50%"
        >
          {{ member }}
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
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      members: [],
      memberID: '',
    }
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
      const url = `/communities/${this.id}/add`
      const params = {
        members: this.members,
      }
      this.$axios
        .patch(url, params)
        .then(() => {
          alert('invited')
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
