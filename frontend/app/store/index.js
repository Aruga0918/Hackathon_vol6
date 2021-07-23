import Vuex from 'vuex'

const store = () =>
  new Vuex.Store({
    state: {
      isSignin: false,
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
    },
  })

export default store
