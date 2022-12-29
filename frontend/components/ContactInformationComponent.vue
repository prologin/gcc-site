<template>
  <b-container fluid>
    <b-row> <h2>Vos informations de contact</h2> </b-row>
    <b-row>
      <b-col md="6">
        <h3>Nom</h3>
        <b-form-input
          id="input-1"
          v-model="personal.familyname"
          placeholder="Nom"
          required
        />
      </b-col>
      <b-col md="6">
        <h3>Prénom</h3>
        <b-form-input
          id="input-1"
          v-model="personal.name"
          placeholder="Prénom"
          required
        />
      </b-col>
    </b-row>

    <b-row>
      <b-col>
        <h3>Email</h3>
        <b-form-input
          id="input-4"
          v-model="personal.email"
          placeholder="email@example.com"
          required
          type="email"
        />
      </b-col>
    </b-row>

    <b-row>
      <b-col>
        <h3>Adresse</h3>
        <b-form-input
          id="input-4"
          v-model="personal.streetname"
          placeholder="Nom et numéro de voie"
          required
        />
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-form-input
          id="input-5"
          v-model="personal.additionalstreetname"
          placeholder="Complément d'adresse (optionnel)"
        />
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-form-input
          id="input-5"
          v-model="personal.postalcode"
          placeholder="Code postal"
          required
        />
      </b-col>
      <b-col>
        <b-form-input
          id="input-6"
          v-model="personal.town"
          placeholder="Ville"
          required
        />
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <h3>Numéro de téléphone</h3>
        <b-form-input
          id="input-7"
          v-model="personal.phone"
          placeholder="Numéro de téléphone (+33 6 60 60 60 60)"
          required
          type="tel"
        />
      </b-col>
    </b-row>
  </b-container>
</template>

<script lang="ts">
import Vue from 'vue';

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
        phone: '',
      }
    }
  },
});
</script>

<style scoped>
.row {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>
