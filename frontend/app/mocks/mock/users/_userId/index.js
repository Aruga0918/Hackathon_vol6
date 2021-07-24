const user = {
  id: 2,
  name: '三手射　公夫',
  icon_url:
    'https://pakutaso.cdn.rabify.me/shared/img/top/img_os06.jpg.webp?d=300',
  uid: 'mitemitebokuwo',
  profile: '32歳　男性です。\n 仕事はフリーライターやってます。',
}

export default {
  get({ values }) {
    return [200, user]
  },
}
