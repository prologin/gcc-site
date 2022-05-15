<template>
  <b-container fluid>
       <b-row> <h2> Information de la participante </h2> </b-row>
       <!-- Autofill fields if |yes| -->
       <b-row>
         <b-col>
           <h3> Utiliser les informations de contact ci-dessus </h3>
         </b-col>
       </b-row>
       <b-row>
         <b-col>
           <b-form-group v-slot="{ ariaDescribedby }">
            <b-form-radio-group v-model="use_contact_info" :aria-describedby="ariaDescribedby" name="some-radios">
              <b-form-radio value="yes"> Oui </b-form-radio>
              <b-form-radio value="no"> Non </b-form-radio>
            </b-form-radio-group>
           </b-form-group>
         </b-col>
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
       <b-row>
         <b-col>
           <h3> Acceptez-vous le partage de ces informations dans le cadre de l'organisation d'un covoiturage ? </h3>
         </b-col>
       </b-row>
       <b-row>
         <b-col>
           <b-form-group v-slot="{ ariaDescribedby }">
            <b-form-radio-group v-model="carpool_use_contact_info" :aria-describedby="ariaDescribedby" name="some-radios">
              <b-form-radio value="yes"> Oui </b-form-radio>
              <b-form-radio value="no"> Non </b-form-radio>
            </b-form-radio-group>
           </b-form-group>
         </b-col>
       </b-row>

         <h3>Sélectionner votre classe</h3>
         <b-form-input required class="slider" type="range" min="0" max="7" step="1" v-model="class_level" />
         <div class="sliderticks">
           <p>6<sup class="sup-vertical-correction">e</sup></p>
           <p>5<sup class="sup-vertical-correction">e</sup></p>
           <p>4<sup class="sup-vertical-correction">e</sup></p>
           <p>3<sup class="sup-vertical-correction">e</sup></p>
           <p>2<sup class="sup-vertical-correction">e</sup></p>
           <p>1<sup class="sup-vertical-correction">e</sup></p>
           <p>Terminale</p>
           <p>Autre</p>
         </div>
         <!-- TODO: Use an enum, add an animation -->
         <div v-if="class_level === ClassTypeEnum.AUTRE">
           Insérer votre classe
           <b-form-input required v-model="other_class" :disabled="class_level !== ClassTypeEnum.AUTRE" placeholder="Insérer votre classe ici" />
         </div>
  </b-container>
</template>

<script lang="ts">
import Vue from 'vue'
import ClassTypeEnum from '@/enums/ClassTypeEnum.js'

export default Vue.extend({
  name: 'ContactInformationComponent',
  mixins: [ClassTypeEnum.Mixin],
  data: () => {
    return {
      class_level: ClassTypeEnum.AUTRE,
      other_class: '',
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

.sliderticks p {
  position: relative;
  display: flex;
  justify-content: center;
  text-align: center;
  width: 0px;
  margin: 0 0 20px 0;
}

.sliderticks {
  -webkit-appearance: none;
  display: flex;
  justify-content: space-between;
  padding: 0 10px;
}

/* Used to fix vertical alignment of text */
.sup-vertical-correction {
  margin-top: 8px;
}
</style>
