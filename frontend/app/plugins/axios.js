export default function ({ $axios, app: { router } }, inject) {
  const api = $axios.create({
    headers: {
      'Content-Type': 'application/json',
    },
  })

  api.interceptors.request.use((config) => {
    const accessToken = localStorage.getItem('accessToken')
    if (accessToken) {
      config.headers = {
        Authorization: `Bearer ${accessToken}`,
      }
    }
    return config
  })

  api.interceptors.response.use(
    (response) => response,
    async (error) => {
      if (error.response.status !== 401) {
        throw error
      }

      // アクセストークンを取得出来なかったとき
      if (error.config._retry) {
        throw error
      }

      const refreshToken = localStorage.getItem('refreshToken')
      if (!refreshToken) {
        router.push('/signin')
      }

      error.config._retry = true
      const res = await $axios.$get('/auth/refresh', {
        headers: { Authorization: `Bearer ${refreshToken}` },
      })
      localStorage.setItem('accessToken', res.access_token)

      const response = await api.request(error.config).catch((err) => {
        throw err
      })
      return response
    }
  )

  inject('api', api)
}
