<template>
  <b-container class="commlist">
    <div
      v-for="user in users"
      :key="user.name"
      class="d-flex"
      style="
        align-items: center;
        justify-content: center;
        border-top-style: ridge;
        border-bottom-style: groove;
        height: 100px;
      "
    >
      <div class="d-flex" style="align-items: center; width: 70%">
        <img
          src="https://placekitten.com/g/30/30"
          class="d-inline-block"
          style="border-radius: 50%; height: 60px; width: 60px; float: left"
        />
        <div class="d-inline-block ml-auto mr-auto" style="width: 260px">
          <p class="d-inline ml-auto">
            {{ user.name }}は<br />{{ user.latestpost.foods }}を食べました
          </p>
          <p style="color: gray; margin-bottom: 4px">
            -場所- {{ user.latestpost.shop }}
          </p>
        </div>
      </div>
    </div>
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      users: [
        {
          name: 'コラショ',
          latestpost: {
            shop: 'なか卯',
            foods: 'カツ丼',
          },
        },
        {
          name: 'トリッピー',
          latestpost: {
            shop: '串鳥',
            foods: 'コロッケ定食',
          },
        },
        {
          name: 'しゃちょう',
          latestpost: {
            shop: 'マクドナルド',
            foods: 'ビッグマック',
          },
        },
      ],
    }
  },
}
</script>
