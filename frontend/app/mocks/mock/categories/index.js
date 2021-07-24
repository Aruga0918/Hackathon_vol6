const categories = [
  {
    id: 1,
    name: '和食',
    shop_cnt: 32,
  },
  {
    id: 2,
    name: '洋食',
    shop_cnt: 2,
  },
  {
    id: 3,
    name: 'イタリアン・フレンチ',
    shop_cnt: 5,
  },
  {
    id: 4,
    name: '中華',
    shop_cnt: 32,
  },
  {
    id: 5,
    name: 'ラーメン',
    shop_cnt: 2,
  },
  {
    id: 6,
    name: 'カフェ・スイーツ',
    shop_cnt: 8,
  },
]

export default {
  // カテゴリ一覧取得API
  get() {
    return [200, categories]
  },
}
