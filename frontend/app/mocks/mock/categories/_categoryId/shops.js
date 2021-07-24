const shops = [
  {
    id: 1,
    name: 'にぎりの徳兵衛 仙台駅前店',
    latitude: 32.1,
    longitude: 23.3,
    description: '説明',
    img: 'https://imgfp.hotp.jp/IMGH/10/90/P027711090/P027711090_238.jpg',
    address: '宮城県仙台市青葉区中央３-1-24　荘銀ビル2F',
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
  },
  {
    id: 2,
    name: '大戸屋 仙台ロフト店',
    latitude: 3.1,
    longitude: 239.3,
    description: '説明説明説明説明説明説明',
    img: 'https://imgfp.hotp.jp/IMGH/53/95/P036735395/P036735395_238.jpg',
    address: '住所住所住所住所住所住所住所住所',
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
  },
]

export default {
  // ショップ一覧取得API
  get({ values }) {
    return [200, shops]
  },
}
