const communityInfo = [
  {
    id: 1,
    name: 'community name 1',
    icon_url:
      'https://pakutaso.cdn.rabify.me/shared/img/top/img_os06.jpg.webp?d=300',
    member_cnt: 23,
  },
  {
    id: 2,
    name: 'community name 2',
    icon_url:
      'https://pakutaso.cdn.rabify.me/shared/img/top/img_os06.jpg.webp?d=300',
    member_cnt: 30,
  },
]

export default {
  // 所属コミュニティ一覧取得API
  get({ values }) {
    return [200, communityInfo]
  },
}
