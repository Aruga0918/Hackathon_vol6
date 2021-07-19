const posts = [
  {
    user_name: 'ユーザーの名前1',
    user_id: 1,
    uid: 'hoge',
    user_icon_url:
      'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.freeiconspng.com%2Fthumbs%2Fwebsite-icon%2Fwebsite-icon-11.png&imgrefurl=https%3A%2F%2Fwww.freeiconspng.com%2Fimages%2Fwebsite-icon&tbnid=E7P3KElxAqquQM&vet=12ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ..i&docid=cPTjaZFLrbiubM&w=320&h=320&q=icon%20free%20url&ved=2ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ',
    shop_id: 1,
    shop_name: 'shop name 1',
    shop_icon_url:
      'https://www.google.com/imgres?imgurl=https%3A%2F%2Feverydayicons.jp%2Fwp%2Fwp-content%2Fthemes%2Feverydayicons%2Ficons%2Fthumbs%2Fei-shop.png&imgrefurl=https%3A%2F%2Feverydayicons.jp%2Ficons%2Fshop%2F&tbnid=YIodxarh64k9JM&vet=12ahUKEwios4nenu_xAhVKVJQKHWS4CVUQMygAegUIARC3AQ..i&docid=3FNo265Cl4KMSM&w=400&h=400&q=shop%20icon%20free&ved=2ahUKEwios4nenu_xAhVKVJQKHWS4CVUQMygAegUIARC3AQ',
    message: '投稿のコメント',
    menu: [
      {
        menu_id: 1,
        name: 'メニューの名前1',
        price: 100,
      },
      {
        menu_id: 2,
        name: 'メニューの名前2',
        price: 200,
      },
    ],
    created_at: 'Mon, 19 Jul 2021 13:31:22 GMT',
  },
  {
    user_name: 'ユーザーの名前2',
    user_id: 2,
    uid: 'hogefuga',
    user_icon_url:
      'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.freeiconspng.com%2Fthumbs%2Fwebsite-icon%2Fwebsite-icon-11.png&imgrefurl=https%3A%2F%2Fwww.freeiconspng.com%2Fimages%2Fwebsite-icon&tbnid=E7P3KElxAqquQM&vet=12ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ..i&docid=cPTjaZFLrbiubM&w=320&h=320&q=icon%20free%20url&ved=2ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ',
    shop_id: 2,
    shop_name: 'shop name 2',
    shop_icon_url:
      'https://www.google.com/imgres?imgurl=https%3A%2F%2Feverydayicons.jp%2Fwp%2Fwp-content%2Fthemes%2Feverydayicons%2Ficons%2Fthumbs%2Fei-shop.png&imgrefurl=https%3A%2F%2Feverydayicons.jp%2Ficons%2Fshop%2F&tbnid=YIodxarh64k9JM&vet=12ahUKEwios4nenu_xAhVKVJQKHWS4CVUQMygAegUIARC3AQ..i&docid=3FNo265Cl4KMSM&w=400&h=400&q=shop%20icon%20free&ved=2ahUKEwios4nenu_xAhVKVJQKHWS4CVUQMygAegUIARC3AQ',
    message: '投稿のコメント',
    menu: [
      {
        menu_id: 1,
        name: 'メニューの名前1',
        price: 100,
      },
      {
        menu_id: 2,
        name: 'メニューの名前2',
        price: 200,
      },
    ],
    created_at: 'Mon, 19 Jul 2021 13:31:22 GMT',
  },
]

export default {
  get() {
    return [200, posts[0]]
  },
  patch() {
    return [200]
  },
  delete() {
    return [200]
  },
}
