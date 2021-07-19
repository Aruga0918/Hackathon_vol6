const community = {
  id: '1',
  members: [
    {
      name: '名前',
      id: 1,
      uid: 'hoge',
      icon_url:
        'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.freeiconspng.com%2Fthumbs%2Fwebsite-icon%2Fwebsite-icon-11.png&imgrefurl=https%3A%2F%2Fwww.freeiconspng.com%2Fimages%2Fwebsite-icon&tbnid=E7P3KElxAqquQM&vet=12ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ..i&docid=cPTjaZFLrbiubM&w=320&h=320&q=icon%20free%20url&ved=2ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ',
      is_join: true,
    },
    {
      name: '名前2',
      id: 2,
      uid: 'hogefuga',
      icon_url:
        'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.freeiconspng.com%2Fthumbs%2Fwebsite-icon%2Fwebsite-icon-11.png&imgrefurl=https%3A%2F%2Fwww.freeiconspng.com%2Fimages%2Fwebsite-icon&tbnid=E7P3KElxAqquQM&vet=12ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ..i&docid=cPTjaZFLrbiubM&w=320&h=320&q=icon%20free%20url&ved=2ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ',
      is_join: false,
    },
  ],
  name: 'community name',
  comm_icon_url:
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F93%2F93792.png&imgrefurl=https%3A%2F%2Fwww.freepik.com%2Ffree-icon%2Fcommunity_860202.htm&tbnid=XZ09H4t8YJqKZM&vet=12ahUKEwjWhMuN3O7xAhW0NKYKHbg6ArEQMygAegUIARCxAQ..i&docid=57VSv3_0ygkB9M&w=512&h=512&q=icon%20free%20community&ved=2ahUKEwjWhMuN3O7xAhW0NKYKHbg6ArEQMygAegUIARCxAQ',
  description: 'コミュニティの説明',
  host_user: 1,
}

export default {
  // コミュニティ情報取得API
  get() {
    return [200, community]
  },

  // コミュニティ削除API
  delete() {
    return [200]
  },

  // コミュニティ編集API
  patch() {
    return [200]
  },
}
