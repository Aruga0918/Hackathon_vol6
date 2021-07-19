const users = [
  {
    name: '名前1',
    id: 1,
    uid: 'hoge',
    icon_url:
      'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.freeiconspng.com%2Fthumbs%2Fwebsite-icon%2Fwebsite-icon-11.png&imgrefurl=https%3A%2F%2Fwww.freeiconspng.com%2Fimages%2Fwebsite-icon&tbnid=E7P3KElxAqquQM&vet=12ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ..i&docid=cPTjaZFLrbiubM&w=320&h=320&q=icon%20free%20url&ved=2ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ',
  },
  {
    name: '名前2',
    id: 2,
    uid: 'hogefuga',
    icon_url:
      'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.freeiconspng.com%2Fthumbs%2Fwebsite-icon%2Fwebsite-icon-11.png&imgrefurl=https%3A%2F%2Fwww.freeiconspng.com%2Fimages%2Fwebsite-icon&tbnid=E7P3KElxAqquQM&vet=12ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ..i&docid=cPTjaZFLrbiubM&w=320&h=320&q=icon%20free%20url&ved=2ahUKEwjr1vXF2-7xAhUWAqYKHeCFB28QMygXegUIARDfAQ',
  },
]

export default {
  // ユーザー一覧取得API
  get({ values }) {
    return [200, { data: users }]
  },
}
