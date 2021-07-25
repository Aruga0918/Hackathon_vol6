import Vuex from 'vuex'

const store = () =>
  new Vuex.Store({
    state: {
      isSignin: false,
      user: {},
      // communityId: 0,
      community: {
        name: 'public community',
        id: 0,
      },
    },
    getters: {
      isSignin(state) {
        return state.isSignin
      },
    },
    mutations: {
      storeSignin(state) {
        if (localStorage.getItem('accessToken')) {
          state.isSignin = true
        }
      },
      storeSignout(state) {
        if (!localStorage.getItem('accessToken')) {
          state.isSignin = false
          state.community = {
            name: 'public community',
            id: 0,
          }
        }
      },
      storeUser(state, user) {
        state.user = user
      },
      // storeCommunityId(state, communityId) {
      //   state.communityId = communityId
      // },
      storeCommunity(state, community) {
        state.community = community
      },
    },
  })

export default store
