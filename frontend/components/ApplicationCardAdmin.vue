<template>
  <tbody>
    <tr>
      <td scope="row">
        {{ app.first_name }} {{ app.last_name }}
      </td>
      <td>
        {{ app.status }}
      </td>
      <td>
        <b-button v-b-modal="'modal-' + app.user">
          Infos Perso.
        </b-button>
      </td>
      <td>
        <select
          :id="'select-' + app.user"
          value="Confirmé"
          right
          class="form-select"
        >
          <option :selected="app.status == -2" value="Rejeté"> Rejeté </option>
          <option :selected="app.status == 3" value="Accepté"> Accepté </option>
          <option :selected="app.status == 4" value="Confirmé"> Confirmé </option>
        </select>
      </td>
    </tr>
    <b-modal
      :id="'modal-' + app.user"
      centered
      ok-title="Fermer"
      ok-variant="secondary-button"
      size="xl"
    >
      Infos de la candidate
    </b-modal>
  </tbody>
</template>
<script>
import Vue from "vue";
import { applicationsAPI } from "../services/applications.api";

export default Vue.extend({
  name: "ApplicationCardAdmin",
  props: ["app_id"],
  data() {
    return { app: [] };
  },
  created() {
    applicationsAPI.applicationsRead(this.app_id).then((res) => {
      this.app = res;
    })
  },
  methods: {
    rejectApp () {
      console.log('Application Rejete');
    },
  }
});
</script>

<style></style>
