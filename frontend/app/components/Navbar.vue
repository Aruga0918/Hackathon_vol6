<template>
  <b-navbar
    toggleable="sm"
    class="navbar-dark"
    style="background-color: #f44336; color: #ffffff"
  >
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-navbar-brand to="/" nuxt>
      <table class="table table-borderless p-0 m-0">
        <tbody class="p-0 m-0">
          <tr class="p-0 m-0">
            <td class="p-0 m-0">
              <b-img
                src="@/assets/fooriend_logo_bland_color_reverse.jpg"
                alt="Rounded image"
                height="50px"
              ></b-img>
            </td>
            <td class="align-middle p-0 m-0 pl-1 text-white">fooriend</td>
          </tr>
        </tbody>
      </table>
    </b-navbar-brand>

    <navbar-user-icon v-if="isSignin" class="d-block d-sm-none" />
    <navbar-login-icon v-else class="d-block d-sm-none" />

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item class="entranceShop">
          <nuxt-link class="nlink" :to="{ name: 'category' }">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-shop"
              viewBox="0 0 16 16"
            >
              <path
                d="M2.97 1.35A1 1 0 0 1 3.73 1h8.54a1 1 0 0 1 .76.35l2.609 3.044A1.5 1.5 0 0 1 16 5.37v.255a2.375 2.375 0 0 1-4.25 1.458A2.371 2.371 0 0 1 9.875 8 2.37 2.37 0 0 1 8 7.083 2.37 2.37 0 0 1 6.125 8a2.37 2.37 0 0 1-1.875-.917A2.375 2.375 0 0 1 0 5.625V5.37a1.5 1.5 0 0 1 .361-.976l2.61-3.045zm1.78 4.275a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 1 0 2.75 0V5.37a.5.5 0 0 0-.12-.325L12.27 2H3.73L1.12 5.045A.5.5 0 0 0 1 5.37v.255a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0zM1.5 8.5A.5.5 0 0 1 2 9v6h1v-5a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v5h6V9a.5.5 0 0 1 1 0v6h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1V9a.5.5 0 0 1 .5-.5zM4 15h3v-5H4v5zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3zm3 0h-2v3h2v-3z"
              />
            </svg>
            お店を探す
          </nuxt-link>
        </b-nav-item>

        <b-nav-item>
          <nuxt-link class="nlink" :to="{ name: 'community' }">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-people"
              viewBox="0 0 16 16"
            >
              <path
                d="M15 14s1 0 1-1-1-4-5-4-5 3-5 4 1 1 1 1h8zm-7.978-1A.261.261 0 0 1 7 12.996c.001-.264.167-1.03.76-1.72C8.312 10.629 9.282 10 11 10c1.717 0 2.687.63 3.24 1.276.593.69.758 1.457.76 1.72l-.008.002a.274.274 0 0 1-.014.002H7.022zM11 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm3-2a3 3 0 1 1-6 0 3 3 0 0 1 6 0zM6.936 9.28a5.88 5.88 0 0 0-1.23-.247A7.35 7.35 0 0 0 5 9c-4 0-5 3-5 4 0 .667.333 1 1 1h4.216A2.238 2.238 0 0 1 5 13c0-1.01.377-2.042 1.09-2.904.243-.294.526-.569.846-.816zM4.92 10A5.493 5.493 0 0 0 4 13H1c0-.26.164-1.03.76-1.724.545-.636 1.492-1.256 3.16-1.275zM1.5 5.5a3 3 0 1 1 6 0 3 3 0 0 1-6 0zm3-2a2 2 0 1 0 0 4 2 2 0 0 0 0-4z"
              />
            </svg>
            コミュニティ
          </nuxt-link>
        </b-nav-item>
      </b-navbar-nav>

      <navbar-user-icon v-if="isSignin" class="d-none d-sm-block ml-auto" />
      <navbar-login-icon v-else class="d-none d-sm-block ml-auto" />
    </b-collapse>
  </b-navbar>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  data: () => {
    return {}
  },
  computed: {
    ...mapGetters(['isSignin']),
  },
}
</script>

<style>
.nlink {
  color: white;
}
</style>
