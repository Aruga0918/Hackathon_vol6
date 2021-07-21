<template>
  <div class="sidebar">
    <div class="sidebar-wrapper">
      <div class="sidebar-link-area">
        <!-- サイドバーメニュー -->
        <p>
          <router-link to="/shops_jp" class="sidebar-link">和食</router-link>
        </p>
        <p>
          <router-link to="/shops_yo" class="sidebar-link">洋食</router-link>
        </p>
        <p>
          <router-link to="/shops_italy" class="sidebar-link"
            >イタリアン</router-link
          >
        </p>
        <p>
          <router-link to="/shops_china" class="sidebar-link">中華</router-link>
        </p>
        <p>
          <router-link to="/shops_ramen" class="sidebar-link"
            >ラーメン</router-link
          >
        </p>
        <p>
          <router-link to="/shops_cafe" class="sidebar-link"
            >カフェ</router-link
          >
        </p>
        <p>
          <router-link to="/shop_oteher" class="sidebar-link"
            >その他</router-link
          >
        </p>
      </div>
    </div>
  </div>
</template>

<style>
.sidebar {
  background-color: #ff7961;
  height: 100%; /* サイドバーの高さ */
  width: 200px; /* サイドバーのwidthを指定 */
  max-width: 200px; /* widthの最大値 */
  opacity: 0.9.5; /* 透過する 0に近くほど透過する */
  position: fixed; /* 左上に要素を固定する(スクロールしても位置は固定される) */
  overflow-x: hidden; /* 横軸ではみ出た要素を非表示にする */
  box-sizing: border-box; /* paddingとborderを、widthとheightに含める */
  padding-left: 40px; /* サイドバー内のリンクの位置を右にずらす */
}

.sidebar-link-area {
  padding-top: 20px; /* サイドバーリンクの上部に空白を作る */
}

.sidebar-link {
  color: #ffffff; /* リンクの文字色を白に */
}

.sidebar-link:hover {
  color: #ffffff; /* マウスがリンクに乗った時も文字色を白に */
}
</style>
