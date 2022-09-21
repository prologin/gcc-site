<template>
  <b-container fluid>
    <b-row align-h="center" class="py-5">
      <b-col cols="10">
        <b-alert v-model="emptyFields" variant="danger">
          <b-icon-exclamation-circle class="mx-2" /> Tous les champs sont
          requis.
        </b-alert>
        <b-alert v-model="showError" variant="danger">
          <b-icon-exclamation-circle class="mx-2" /> {{ error }}
        </b-alert>
        <b-form-group id="input-group-1" label="Email :" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="loginForm.email"
            type="email"
            placeholder="Entrer votre email"
            required
          />
        </b-form-group>
        <b-form-group id="input-group-2" label="Mot de passe :">
          <b-form-input
            id="input-2"
            v-model="loginForm.password"
            type="password"
            placeholder="Entrer votre mot de passe"
            required
          />
        </b-form-group>
        <b-button @click="login" class="primary-button mt-4" block
          >Se connecter</b-button
        >
        <hr class="hr-text mt-5" data-content="Ou se connecter avec :" />

        <b-button block class="login-button">
            <b-row align-v="center">
                <b-col cols="2">
                  <b-img :src="require(`@/assets/logo-prologin.svg`)" style="max-width: 30px" :alt="`Logo de Prologin`" />
                </b-col>
                <b-col cols="10">
                    Prologin
                </b-col>
            </b-row>
        </b-button>

        <!-- Logo from fontawesome -->
        <ConnectButton v-for="(sn, index) in Constants.BUTTON_SNS"
          :logo="sn.logo" v-bind:name="sn.name" v-bind:key="index" />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Vue from "vue";
import ConnectButton from '@/components/ConnectButton.vue'

import * as Constants from '@/constants'

export default Vue.extend({
  name: "LoginComponent",
  components: {
    ConnectButton
  },
  created () {
    this.Constants = Constants
  },
  data() {
    return {
      loginForm: {
        email: "",
        password: "",
      },
      error: "",
      showError: false,
      emptyFields: false,
    };
  },
  methods: {
    async login() {
      this.emptyFields = false;
      if (this.loginForm.email === "" || this.loginForm.password === "") {
        this.emptyFields = true;
      } else {
        await this.$store
          .dispatch("user/login", this.loginForm)
          .then(() => {
            window.$nuxt.$router.push("/")
          })
          .catch((err) => {
            this.showError = true;
            if (err.response) {
              if (err.response.status === 500) {
                this.error =
                  "Une erreur inattendue est survenue du côté de notre serveur. Réessayez plus tard.";
              } else {
                this.error = err.response.data.detail;
              }
            } else {
              this.error =
                "Une erreur inconnue est survenue. Si le problème persiste, nous vous invitons à réessayer plus tard.";
            }
          });
      }
    },
  },
});
</script>

<style scoped>
.hr-text {
  line-height: 1em;
  position: relative;
  outline: 0;
  border: 0;
  color: black;
  text-align: center;
  height: 1.5em;
  opacity: 0.5;
}

.hr-text:before {
  content: "";
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

  padding: 0 0.5em;
  line-height: 1.5em;
  color: #818078;
  background-color: white;
}

.form-control,
.login-button {
  border-radius: var(--global-border-radius) !important;
}

.login-button {
  background:
    linear-gradient(white, white) padding-box,
    linear-gradient(to right, #00AED3, #E4006D, #A6C613) border-box;
  border: 2px solid transparent !important;
  color: var(--main-dark-color) !important;
}

.login-button:hover {
  background: var(--light-text-color) !important;
  color: white !important;
}
</style>