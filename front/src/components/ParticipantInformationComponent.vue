<template>
  <b-container fluid>
     <b-form>
       <b-row> <h2> Information de la participante </h2> </b-row>
       <!-- Autofill fields if |yes| -->
       <b-row>
         <h3> Utiliser les informations de contact ci-dessus </h3>
       </b-row>
       <b-row>
         <b-form-group v-slot="{ ariaDescribedby }">
          <b-form-radio-group v-model="use_contact_info" :aria-describedby="ariaDescribedby" name="some-radios">
            <b-form-radio value="yes"> Oui </b-form-radio>
            <b-form-radio value="no"> Non </b-form-radio>
          </b-form-radio-group>
         </b-form-group>
       </b-row>

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
             id="input-2"
             placeholder="Prénom"
             required
             v-model="personal.name"
             />
         </b-col>
       </b-row>
       <b-row>
         <b-col md="6">
           <h3>
             Date de naissance
           </h3>
           <b-form-datepicker
             id="input-3"
             placeholder="01/01/1970"
             required
             v-model="personal.birthday"
             />
         </b-col>
       </b-row>
       <!-- TODO: Add slider (or range) for class level + conditionnal text field if other selected in slider -->
       <b-row>
         <h3> Acceptez-vous le partage de ces informations dans le cadre de l'organisation d'un covoiturage ? </h3>
       </b-row>
       <b-row>
         <b-form-group v-slot="{ ariaDescribedby }">
          <b-form-radio-group v-model="carpool_use_contact_info" :aria-describedby="ariaDescribedby" name="some-radios">
            <b-form-radio value="yes"> Oui </b-form-radio>
            <b-form-radio value="no"> Non </b-form-radio>
          </b-form-radio-group>
         </b-form-group>
       </b-row>

     </b-form>
  </b-container>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'ContactInformationComponent',
  data: () => {
    return {
      use_contact_info: '',
      carpool_use_contact_info: '',
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
