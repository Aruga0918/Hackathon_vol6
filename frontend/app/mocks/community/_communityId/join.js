export default {
  post({ values }) {
    return [200, { data: { id: values.communityId } }]
  },
}
