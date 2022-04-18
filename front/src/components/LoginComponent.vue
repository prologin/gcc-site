<template>
  <b-container fluid>
    <b-row align-h="center" class="py-5">
      <b-col cols="10">
        <b-alert v-model="showError" variant="danger">
          <b-icon-exclamation-circle class="mx-2" /> La connexion a échouée, merci de réessayer.
        </b-alert>
        <b-form-group
          id="input-group-1"
          label="Email :"
          label-for="input-1"
          >
          <b-form-input
            id='input-1'
            v-model='loginForm.email'
            type='email'
            placeholder='Entrer votre email'
            required
            />
        </b-form-group>

          <b-form-group
            id='input-group-2'
            label="Mot de passe :"
            >
            <b-form-input
              id='input-2'
              type="password"
              placeholder="Entrer votre mot de passe"
              />
          </b-form-group>

            <b-button @click="login" class="primary-button mt-4" block>Se connecter</b-button>

            <hr class="hr-text mt-5" data-content="Ou se connecter avec :">

            <b-button block class="prologin-login-button">
              <b-row align-v="center">
                <b-col cols="2">
                  <b-img
                    :src="require('@/assets/prologin.svg')"
                    style="max-width: 30px"
                    alt="Logo de Prologin" />
                </b-col>
                <b-col cols="10">
                  Prologin
                </b-col>
              </b-row>
            </b-button>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Vue from 'vue'
import { mapActions } from 'vuex'

export default Vue.extend({
  name: 'LoginComponent',
  data () {
    return {
      loginForm: {
        email: '',
        password: ''
      },
      showError: false
    }
  },
  methods: {
    ...mapActions(['LogIn']),
    // TODO: Create user from form.
    async login () {
      const user = {
        firstName: 'Alice',
        lastName: 'Doe',
        email: 'alice.doe@example.com'
      }
      await this.LogIn(user).then(() => {
        this.$router.push(this.$route.query.redirect || { name: 'home' })
      }).catch(() => {
        this.showError = true
      })
    }
  }
})
</script>

<style>
.hr-text {
  line-height: 1em;
  position: relative;
  outline: 0;
  border: 0;
  color: black;
  text-align: center;
  height: 1.5em;
  opacity: .5;
}

.hr-text:before {
  content: '';
  background: linear-gradient(to right, transparent, black, transparent);
  position: absolute;
  left: 0;
  top: 50%;
  width: 100%;
  height: 1px;
}

.hr-text:after {
  content: attr(data-content);
  position: relative;
  display: inline-block;
  color: black;

  padding: 0 .5em;
  line-height: 1.5em;
  color: #818078;
  background-color: white;
}

.form-control, .prologin-login-button {
  border-radius: var(--global-border-radius) !important;
}

label, legend {
  margin-left: 0.6rem;
}

.prologin-login-button {
  background:
  linear-gradient(white, white) padding-box,
  linear-gradient(to right, yellow, red, blue) border-box;
  border: 2px solid transparent !important;
  color: var(--main-dark-color) !important;
}

.prologin-login-button:hover {
  background: var(--light-text-color) !important;
  color: white !important;
}
</style>
