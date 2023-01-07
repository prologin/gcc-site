<template>
  <div>
    <table class="table table-borderless">
      <thead>
        <tr>
          <th scope="col">Nom</th>
          <th scope="col">Status</th>
          <th scope="col">Infos</th>
          <th scope="col" />
        </tr>
      </thead>
      <tbody>
        <tr v-for="(app, index) in applications" :key="index">
          <td scope="row">{{ app.first_name }} {{ app.last_name }}</td>
          <td>
            {{ Status[app.status] }}
          </td>
          <td>
            <b-button v-b-modal="'modal-' + app.user"> Infos Perso.</b-button>
          </td>
          <td>
            <b-select :id="'select-' + app.user" right class="form-select">
              <option :selected="app.status == -2" value="-2"> Rejeté </option>
              <option :selected="app.status == -1" value="-1"> Abandonné </option>
              <option :selected="app.status == 0" value="0"> Inscrit </option>
              <option :selected="app.status == 1" value="1"> Non sélectionné </option>
              <option :selected="app.status == 2" value="2"> Sélectionné </option>
              <option :selected="app.status == 3" value="3"> Accepté </option>
              <option :selected="app.status == 4" value="4"> Confirmé </option>
            </b-select>
          </td>
          <!-- Modal = component a part -->
          <AppCardAdmin :app_id="app.id" :event_id="event_id" />
        </tr>
      </tbody>
    </table>

    <b-button variant="primary" @click="update"> Sauvegarder </b-button>
  </div>
</template>
<script>
import Vue from 'vue';
import { applicationsAPI } from '../../services/applications.api';
import AppCardAdmin from './ApplicationCardAdmin.vue';

export default Vue.extend({
  name: 'ApplicationListAdmin',
  components: {
    AppCardAdmin
  },
  props: ['event_id'],
  data () {
    return {
      applications: [],
      Status: {
        "-2": "Rejeté",
        "-1": "Abandonné",
        "0": "Inscrit",
        "1": "Non sélectionné",
        "2": "Sélectionné",
        "3": "Accepté",
        "4": "Confirmé",
      }
    }
  },
  created() {
    applicationsAPI.applicationsList(null, this.event_id).then((res) => {
      this.applications = res;
    })
  },
  methods: {
    async update_api(app, status) {
      const form = {"status": status};
      const req = await this.$axios.patch("/rest/v1/applications/" + app.id + "/update_status/", form);
      return req;
    },
    update() {
      this.applications.forEach((app) => {
        const new_status = document.getElementById('select-' + app.user).value;
        this.update_api(app, new_status);
        app.status = new_status;
      });
    },
  }
});
</script>

<style></style>
