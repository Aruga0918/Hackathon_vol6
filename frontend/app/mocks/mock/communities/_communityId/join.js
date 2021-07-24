export default {
  // コミュニティ参加API
  post() {
    return [200, { community_id: 1 }]
  },
  // コミュニティ参加拒否API
  delete() {
    return [200]
  },
}
