<template>
  <b-container class="background-login main-body-style" fluid>
    <b-row class="offset-0 col-xl-4 offset-xl-4 p-0" no-gutters>
      <b-col cols="12" align="center">
        <NuxtLink to="/">
          <b-img class="mb-4" :src="require('@/assets/logo_gcc.svg')" />
        </NuxtLink>
        <h2 v-if="showLogin" class="mb-4">
          Se connecter sur <b>Girls can code!</b>
        </h2>
        <h2 v-else class="mb-4">S'inscrire sur <b>Girls can code!</b></h2>
      </b-col>
      <b-container fluid class="content-background">
        <b-col v-if="showLogin" cols="12">
          <LoginComponent />
        </b-col>
        <b-col v-else cols="12">
          <RegisterComponent />
        </b-col>
        <b-col v-if="showLogin" cols="12" align="center">
          <h4 class="mt-3">
            Je n'ai pas de compte,
            <b-link @click="showLogin = !showLogin"> s'inscrire </b-link>
          </h4>
        </b-col>
        <b-col v-else cols="12" align="center">
          <h4 class="mt-3">
            J'ai déjà un compte,
            <b-link @click="showLogin = !showLogin"> se connecter </b-link>
          </h4>
        </b-col>
      </b-container>
    </b-row>
  </b-container>
</template>

<script>
import Vue from "vue";
import LoginComponent from "@/components/LoginComponent.vue";
import RegisterComponent from "@/components/RegisterComponent.vue";

export default Vue.extend({
  name: "LoginView",
  components: {
    LoginComponent,
    RegisterComponent,
  },
  data() {
    return {
      showLogin: true,
    }
  },
});
</script>
<style scoped>
label {
  margin-left: 0.6rem !important;
}

.main-body-style {
  height: 100vh !important;
  background-color: var(--main-light-color) !important;
  padding-top: 0px !important;
  justify-content: center;
}

.content {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.background-login {
  height: 100vh;
  background-image: url("~@/assets/code-background-v2.svg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
</style>
