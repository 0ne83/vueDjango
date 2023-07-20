<template>
  <div class="page-signup">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign Up</h1>
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>E-mail</label>
            <div class="control">
              <input type="email" class="input" v-model="email" name="email">
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" class="input" v-model="password" name="password">
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Sign Up</button>
            </div>
          </div>

        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {

  name: 'SignUp',
  data  () {
    return {
      email: '',
      password: '',
      errors: []
    }
  },
  methods: {
    submitForm (e) {
      const formData = {
        email: this.email,
        password: this.password
      }
      axios.post('/api2/users/', formData).then(respose => {
        console.log(respose)
        this.$router.push('/login')
      }).catch(error => {
        if (error.respose){
          for (const key in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`)
          }
          console.log(JSON.stringify(error.response.data))
        } else if (error.message){
          console.log(JSON.stringify(error.response))
        } else {
          console.log(JSON.stringify(error))
        }
      })
    }
  }
}
</script>
