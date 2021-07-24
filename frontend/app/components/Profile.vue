<template>
  <div>
    <div
      class="TopContainer d-flex"
      style="height: 20vh; vertical-align: center"
    >
      <img :src="user.icon_url" style="object-fit: contain" />
      <div class="d-inline-block ml-auto mr-auto" style="margin-top: 16px">
        <div class="primarydata mr-auto" style="width: 50%">
          <big style="height: 20%; font-weight: bold">{{ user.name }}</big>
          <p style="height:20% color:gray">ID: {{ user.uid }}</p>
        </div>
        <p style="height: 20%"><br />{{ user.profile }}</p>
      </div>
    </div>
    <div class="TimeLine">
      <div class="bar">投稿</div>
      <b-container class="posts">
        <div
          v-for="post in user.posts"
          :key="post.name"
          class="d-flex"
          style="
            align-items: center;
            justify-content: center;
            border-top-style: none;
            border-bottom-style: ridge;
            height: 100px;
          "
        >
          <div class="d-flex" style="align-items: center; width: 85%">
            <img
              :src="user.icon_url"
              class="d-inline-block"
              style="padding-right:16px border-radius: 50%; height: 60px; width: 60px; float:left"
            />
            <div
              class="d-inline-block mr-auto"
              style="width: 260px; margin-left: 16px"
            >
              <div class="d-inline ml-auto mb-auto">
                {{ user.name }}<br />{{ post.foods }}<br />
                <p style="font-size: 6px; margin-bottom: 0">を食べました</p>
              </div>
              <p style="color: gray; margin-bottom: 4px">
                -場所- {{ post.shop }}
              </p>
            </div>
          </div>
        </div>
      </b-container>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        name: '三手射　公夫',
        icon_url:
          'https://pakutaso.cdn.rabify.me/shared/img/top/img_os06.jpg.webp?d=300',
        uid: 'mitemitebokuwo',
        profile: '32歳　男性です。\n 仕事はフリーライターやってます。',
        posts: [
          {
            shop: '大戸屋仙台ロフト店',
            foods: '鳥と野菜の黒酢あん定食',
          },
          {
            shop: '丸亀製麺 仙台東口店',
            foods: 'ぶっかけうどん(温・冷)',
          },
          {
            shop: 'ヘンボッハン テッペ',
            foods: 'いちご飴',
          },
        ],
      },
    }
  },
}
</script>
<style scoped>
.bar {
  color: #ff7961;
  font-weight: bold;
  padding-left: 10%;
  padding-top: 1%;
  border-bottom: 3px solid #ff7961;
}
</style>
