<template>
  <b-container fluid>
          <b-row> <h2> Vos informations de contact </h2> </b-row>
          <b-row>
            <b-col md="6">
              <h3>
                Nom
              </h3>
              <b-form-input
                id="input-1"
                placeholder="Nom"
                required
                v-model="personal.familyname"
                />
            </b-col>
            <b-col md="6">
              <h3>
                Prénom
              </h3>
              <b-form-input
                id="input-1"
                placeholder="Prénom"
                required
                v-model="personal.name"
                />
            </b-col>
          </b-row>

          <b-row>
            <b-col>
              <h3>
                Email
              </h3>
              <b-form-input
                id="input-4"
                placeholder="email@example.com"
                required
                v-model="personal.email"
                type="email"
                />
            </b-col>
          </b-row>

          <b-row>
            <b-col>
              <h3>
                Adresse
              </h3>
              <b-form-input
                id="input-4"
                placeholder="Nom et numéro de voie"
                required
                v-model="personal.streetname"
                />
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-form-input
                id="input-5"
                placeholder="Complément d'adresse (optionnel)"
                v-model="personal.additionalstreetname"
                />
              </b-col>
            </b-row>
            <b-row>
              <b-col>
                <b-form-input
                  id="input-5"
                  placeholder="Code postal"
                  required
                  v-model="personal.postalcode"
                  />
              </b-col>
              <b-col>
                <b-form-input
                  id="input-6"
                  placeholder="Ville"
                  required
                  v-model="personal.town"
                  />
              </b-col>
          </b-row>
          <b-row>
            <b-col>
              <h3>
                Numéro de téléphone
              </h3>
              <b-form-input
                 id="input-7"
                 placeholder="Numéro de téléphone (+33 6 60 60 60 60)"
                 required
                 type="tel"
                 v-model="personal.phone"
                 />
            </b-col>
          </b-row>
  </b-container>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'ContactInformationComponent',
  data: () => {
    return {
      personal: {
        familyname: '',
        name: '',
        email: '',
        streetname: '',
        additionalstreetname: '',
        postalcode: '',
        town: '',
        phone: ''
      }
    }
  }
})
</script>

<style scoped>
.row {
  margin-top: 10px;
  margin-bottom: 10px;

}

</style>
