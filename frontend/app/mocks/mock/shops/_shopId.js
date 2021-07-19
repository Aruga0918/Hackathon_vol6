const shopInfo = {
  id: 1,
  name: 'shop名',
  latitude: 32.1,
  longitude: 23.3,
  description: '説明',
  address: '住所',
  menu: [
    {
      menu_id: 1,
      name: 'メニューの名前 1',
      price: 300,
    },
    {
      menu_id: 2,
      name: 'メニューの名前 2',
      price: 200,
    },
  ],
}

export default {
  // 店舗情報取得API
  get({ values }) {
    return [200, shopInfo]
  },
}
