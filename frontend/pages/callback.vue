<template>
  <b-container fluid class="p-0">
    <b-list-group horizontal>
      <b-list-group-item>
        <b-img :src="require(`@/assets/indicator-loading.svg`)" alt="Loading" />
      </b-list-group-item>
      <b-list-group-item class="d-flex align-items-center light-color-text">
        Connexion en cours, veuillez patienter.
      </b-list-group-item>
    </b-list-group>
    User status:
    <b-badge>{{ $auth.$state.loggedIn ? "Logged In" : "Guest" }}</b-badge>

    State:
    <pre>{{ state }}</pre>
  </b-container>
</template>

<script>
import Vue from "vue";

export default Vue.extend({
  middleware: ['auth'],
  auth: true,
  computed: {
    state() {
      return JSON.stringify(this.$auth.$state, undefined, 2)
    }
  }
});
</script>
