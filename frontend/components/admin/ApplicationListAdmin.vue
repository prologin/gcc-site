<template>
  <div>
    <b-table
      hover
      fixed
      stacked="lg"
      responsive="xl"
      class="table-style"
      :fields="fields"
      :items="applications"
      selectable
      @row-clicked="
        (item) =>
          $set(item, '_showDetails', !item._showDetails && item.status != -2)
      "
    >
      <template #cell(name)="data">
        <b-list-group horizontal>
          <b-list-group-item class="d-flex align-items-center light-color-text">
            <h3>{{ data.item.first_name }} {{ data.item.last_name }}</h3>
          </b-list-group-item>
        </b-list-group>
      </template>

      <template #cell(status)="data">
        {{ Status[data.item.status] }}
      </template>

      <template #cell(selected)="data">
        <div v-if="data.rowSelected && data.item.status != -2">
          <span aria-hidden="true">
            <b-icon
              font-scale="2"
              variant="secondary"
              icon="chevron-compact-up"
            />
          </span>
        </div>
        <div v-else-if="data.item.status != -2">
          <span aria-hidden="true">
            <b-icon
              font-scale="2"
              variant="secondary"
              icon="chevron-compact-down"
            />
          </span>
        </div>
      </template>

      <template #row-details="data">
        <div v-if="data.item.status != -2" class="mb-2">
          <h3>
            Profil de {{ data.item.first_name }} {{ data.item.last_name }}
          </h3>
          <p>
            <b> Nombre de participations: </b>
            <span :id="'participations-' + data.item.id">
              {{ users[data.index].participations_count }}
            </span>
          </p>
          <p>
            <b> E-mail: </b>
            <span :id="'email-' + data.item.id">
              {{ users[data.index].email }}
            </span>
          </p>
          <p>
            <b> Date de naissance: </b>
            <span :id="'dob-' + data.item.id"> {{ data.item.dob }} </span>
          </p>
          <p>
            <b> Adresse: </b>
            <span :id="'address-' + data.item.id">
              {{ users[data.index].address }}, {{ users[data.index].city }},
              {{ users[data.index].country }}
            </span>
          </p>

          <b-row>
            <b-col>
              <b> Changez le status </b> <br>
              <select :id="'select-' + data.item.user" left class="form-select">
                <option :selected="data.item.status == -2" value="-2">
                  Rejeté
                </option>
                <option :selected="data.item.status == -1" value="-1">
                  Abandonné
                </option>
                <option :selected="data.item.status == 0" value="0">
                  Inscrit
                </option>
                <option :selected="data.item.status == 1" value="1">
                  Non sélectionné
                </option>
                <option :selected="data.item.status == 2" value="2">
                  Sélectionné
                </option>
                <option :selected="data.item.status == 3" value="3">
                  Accepté
                </option>
                <option :selected="data.item.status == 4" value="4">
                  Confirmé
                </option>
              </select>
            </b-col>
          </b-row>
        </div>
      </template>
    </b-table>

    <b-button variant="primary" @click="update"> Sauvegarder </b-button>
    <b-button variant="primary" @click="dlInfo"> Téléchargement </b-button>
  </div>
</template>
<script>
import Vue from "vue";
import { applicationsAPI } from "../../services/applications.api";
import { usersAPI } from "../../services/users.api";
import { eventsAPI } from "../../services/events.api";
import AppCardAdmin from "./ApplicationCardAdmin.vue";

export default Vue.extend({
  name: "ApplicationListAdmin",
  components: {
    AppCardAdmin,
  },
  props: ["event_id"],
  data() {
    return {
      fields: ["name", { key: "status", sortable: true }, "Informations"],
      applications: [],
      users: [],
      formEvent: {},
      formAnswers: [],
      Status: {
        "-2": "Rejeté",
        "-1": "Abandonné",
        0: "Inscrit",
        1: "Non sélectionné",
        2: "Sélectionné",
        3: "Accepté",
        4: "Confirmé",
      }
    };
  },
  mounted () {
    // Modfier ca c'est pas beau j'aime pas
    applicationsAPI.applicationsList(null, this.event_id).then((res) => {
      this.applications = res;

      this.applications.forEach((app) => {
        usersAPI.usersRead(app.user).then((res) => {
          this.users.push(res);
        })

        applicationsAPI.applicationsRead(app.id).then((res) => {
          this.formAnswers.push(res.form_answer);
        })
      });

      eventsAPI.eventsForm(this.event_id).then((res) => {
        this.formEvent = res;
      })
    });
  },

  methods: {
    // Myabe faire un .js a part ?
    async update_api(app, status) {
      const form = { status };
      const req = await this.$axios.patch(
        "/rest/v1/applications/" + app.id + "/update_status/",
        form
      )
      return req;
    },
    update() {
      this.applications.forEach((app) => {
        const new_status = document.getElementById("select-" + app.user).value;
        this.update_api(app, new_status);
        app.status = new_status;
      })
    },
    dlInfo() {
      let csv =
        "Nom de famille,Prénom, Nom représentant légal, Prénom représentant légal, Email représentant légal\n";
      for (let index = 0; index < this.applications.length; index++) {
        // Arreter d'harcode ca et mettre l'enum
        if (this.applications[index].status === 4) {
          csv +=
            this.applications[index].last_name +
            "," +
            this.applications[index].first_name;
          csv += "\n";
        }
      }
      const hiddenElement = document.createElement('a');
      hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);
      hiddenElement.target = '_blank';
      // provide the name for the CSV file to be downloaded
      hiddenElement.download = "Infos_GCC!.csv";
      hiddenElement.click();
    },
  },
})
</script>

<style></style>
