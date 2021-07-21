<template>
  <b-container class="commlist">
    <div
      v-for="comm in comms"
      :key="comm.name"
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
          src="https://placekitten.com/g/30/30"
          class="d-inline-block"
          style="border-radius: 50%; height: 60px; width: 60px; float: left"
        />
        <div class="d-inline-block ml-auto mr-auto" style="width: 260px">
          <p class="d-inline ml-auto">{{ comm.name }}</p>
          <b-nav-item-dropdown text="詳細" right style="list-style: none">
            <b-dropdown-item href="#">メンバー：</b-dropdown-item>
            <b-dropdown-item>メンバーを招待</b-dropdown-item>
          </b-nav-item-dropdown>
        </div>

        <b-button
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
          >退会</b-button
        >
      </div>
    </div>
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      comms: [
        { name: 'ベネ英語科', imglink: 'hoge' },
        { name: 'ガストしか勝たん', imglink: 'hogehoge' },
        { name: 'ラーメンハオチー', imglink: 'hogeege' },
        { name: '３年B組', imglink: 'hohoho' },
      ],
    }
  },
}
</script>
