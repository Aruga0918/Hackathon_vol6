# PLUGINS

**This directory is not required, you can delete it if you don't want to use it.**

This directory contains Javascript plugins that you want to run before mounting the root Vue.js application.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/guide/plugins).

#ページ遷移
SPAなので
this.$router.push('/login');
これを組み込んだfunctionをつくる,v-onで実行
それか
 ＜nuxt-link
    :to="{ name: 'event_list-id', params: { id: event.id } }"
  ＞
  "-"は"/"の意味、paramsのなかみはidに入る

#props
注意！
同じページ内でしか渡せない
ー子コンポーネントー
 props: {
    変数名: {
      値: ,
      type: Object,
      required: true,
    },
  },

ー親コンポーネントー
<ChildComponent :key="event.id" :event="event" />