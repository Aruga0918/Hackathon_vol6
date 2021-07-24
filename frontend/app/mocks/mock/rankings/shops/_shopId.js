const ranking = [
  {
    menu_id: 1,
    name: 'メニュー名',
    price: 100,
    posted_cnt: 32,
  },
  {
    menu_id: 2,
    name: 'メニュー名',
    price: 2 - 0,
    posted_cnt: 3,
  },
]

export default {
  // ランキング取得API
  get({ values }) {
    return [200, ranking]
  },
}
