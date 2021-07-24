import Vuex from 'vuex'

const store = () =>
  new Vuex.Store({
    state: {
      isSignin: false,
      user: {},
      communityId: '',
    },
    getters: {
      isSignin(state) {
        return state.isSignin
      },
    },
    mutations: {
      storeSignin(state) {
        if (localStorage.getItem('accessToken') !== null) {
          state.isSignin = true
        }
      },
      storeSignout(state) {
        if (localStorage.getItem('accessToken') === null) {
          state.isSignin = false
        }
      },
      storeUser(state, user) {
        state.user = user
      },
      storeCommunityId(state, communityId) {
        state.communityId = communityId
      },
    },
  })

export default store
