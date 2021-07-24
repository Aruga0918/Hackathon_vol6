const shopInfo = [
  {
    id: 'J001039291',
    name: 'にぎりの徳兵衛 仙台駅前店',
    latitude: 38.260470197,
    longitude: 140.8789994015,
    img: 'https://imgfp.hotp.jp/IMGH/10/90/P027711090/P027711090_238.jpg',
    description:
      '月～日、祝日、祝前日: 11:00～22:15 （料理L.O. 22:00 ドリンクL.O. 22:00）',
    budjet: '昼：1200円　夜：1600円',
    address: '宮城県仙台市青葉区中央３-1-24　荘銀ビル2F',
    menu: [
      {
        menu_id: 1,
        name: '国産本まぐろ赤身',
        price: '418円（税込）',
      },
      {
        menu_id: 2,
        name: '穴子天',
        price: '418円（税込）',
      },
      {
        menu_id: 3,
        name: '穴子一本焼き',
        price: '418円（税込）',
      },
      {
        menu_id: 4,
        name: 'はまちネギ塩炙り',
        price: '286円（税込）',
      },
      {
        menu_id: 5,
        name: 'サーモンネギ塩炙り',
        price: '286円（税込）',
      },
    ],
  },
]

export default {
  // 店舗情報取得API
  get({ values }) {
    return [200, shopInfo[0]]
  },
}
