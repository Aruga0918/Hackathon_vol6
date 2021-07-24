const community = {
  id: 1,
  members: [
    {
      name: '名前',
      id: 1,
      uid: 'hoge',
      icon_url:
        'https://pakutaso.cdn.rabify.me/shared/img/top/img_os06.jpg.webp?d=300',
      is_join: true,
    },
    {
      name: '名前2',
      id: 2,
      uid: 'hogefuga',
      icon_url:
        'https://pakutaso.cdn.rabify.me/shared/img/top/img_os06.jpg.webp?d=300',
      is_join: false,
    },
  ],
  name: 'community name',
  comm_icon_url: '',
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
