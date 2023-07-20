<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>VueApp</strong></router-link>
      </div>

      <div class="navbar-menu">
        <div class="navbar-end">
          <template v-if="$store.state.isAuthenticated">
            <router-link to="/dashboard" class="navbar-item">Dashboard</router-link>

            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/dashboard/account" class="button is-success"><strong>My Account</strong></router-link>
              </div>
            </div>

          </template>

          <template v-else>
            <router-link to="/" class="navbar-item">Home</router-link>
          </template>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/sign-up" class="button is-success"><strong>Sign Up</strong></router-link>
              <router-link to="/login" class="button is-light"><strong>Login</strong></router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright &copy; 2022</p>
    </footer>
  </div>
</template>

<script>
  import axios from "axios"

  export default {
    name: 'App',
    beforeCreate() {
      this.$store.commit("initializeStore")

      const token = this.$store.state.token

      if (token) {
        axios.defaults.headers.common['Authorization'] = 'Token ' + token
      } else {
        axios.defaults.headers.common['Authorization'] = ''
      }
    }
  }
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
