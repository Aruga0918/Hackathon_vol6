const categories = [
  {
    id: 1,
    name: '和食',
    shop_cnt: 32,
  },
  {
    id: 2,
    name: 'fuga',
    shop_cnt: 2,
  },
  {
    id: 3,
    name: 'hogefuga',
    shop_cnt: 0,
  },
]

export default {
  // カテゴリ一覧取得API
  get() {
    return [200, categories]
  },
}
