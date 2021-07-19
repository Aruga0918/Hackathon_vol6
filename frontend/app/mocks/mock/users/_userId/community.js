const communityInfo = [
  {
    id: 1,
    name: 'community name 1',
    icon_url:
      'https://www.google.com/imgres?imgurl=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F93%2F93792.png&imgrefurl=https%3A%2F%2Fwww.freepik.com%2Ffree-icon%2Fcommunity_860202.htm&tbnid=XZ09H4t8YJqKZM&vet=12ahUKEwjWhMuN3O7xAhW0NKYKHbg6ArEQMygAegUIARCxAQ..i&docid=57VSv3_0ygkB9M&w=512&h=512&q=icon%20free%20community&ved=2ahUKEwjWhMuN3O7xAhW0NKYKHbg6ArEQMygAegUIARCxAQ',
    member_cnt: 23,
  },
  {
    id: 2,
    name: 'community name 2',
    icon_url:
      'https://www.google.com/imgres?imgurl=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F93%2F93792.png&imgrefurl=https%3A%2F%2Fwww.freepik.com%2Ffree-icon%2Fcommunity_860202.htm&tbnid=XZ09H4t8YJqKZM&vet=12ahUKEwjWhMuN3O7xAhW0NKYKHbg6ArEQMygAegUIARCxAQ..i&docid=57VSv3_0ygkB9M&w=512&h=512&q=icon%20free%20community&ved=2ahUKEwjWhMuN3O7xAhW0NKYKHbg6ArEQMygAegUIARCxAQ',
    member_cnt: 30,
  },
]

export default {
  // 所属コミュニティ一覧取得API
  get({ values }) {
    return [200, communityInfo]
  },
}
