<template>
  <ul class="horizontal-list">
    <li class="item">
      <img style="border-radius: 50%" src="https://placekitten.com/g/30/30" />
    </li>
    <li class="item">
      <img style="border-radius: 50%" src="https://placekitten.com/g/30/30" />
    </li>
    <li class="item">
      <img style="border-radius: 50%" src="https://placekitten.com/g/30/30" />
    </li>
    <li class="item">
      <img style="border-radius: 50%" src="https://placekitten.com/g/30/30" />
    </li>
    <li class="item">
      <img style="border-radius: 50%" src="https://placekitten.com/g/30/30" />
    </li>
    <li class="item">
      <img style="border-radius: 50%" src="https://placekitten.com/g/30/30" />
    </li>
    <li class="item">
      <img style="border-radius: 50%" src="https://placekitten.com/g/30/30" />
    </li>
  </ul>
</template>
<style>
.horizontal-list {
  overflow-x: auto;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
  margin-bottom: 0%;
  padding-left: 0;
}

.item {
  /* 横スクロール用 */
  display: inline-block;

  /* 見た目調整 */
  height: 40px;
  margin: 5px;
  width: 40px;
}

.li img {
  height: 100%;
  width: 100%;
}
</style>
