<template>
  <div>
    <b-container fluid>
      <div class="form-style">
        <img :src="require('@/assets/logo_gcc.svg')" alt="Logo des stages Girls Can Code" class="logo" />
        <div>
          <b-form @submit="submitAnswers" inline>
          <div class="weight"> Informations personnelles </div>
          <b-form-group
            id="input-group-1"
            label-for="input-1">
            <b-row>
              <b-col>
                <b-form-input
                  id="input-1"
                  placeholder="Nom"
                  class="mb-2 mr-sm-2"
                  required
                  v-model="personal.familyname"
                  />
              </b-col>
              <b-col>
                <b-form-input
                  id="input-1"
                  placeholder="Prénom"
                  class="mb-2"
                  required
                  v-model="personal.name"
                  />
              </b-col>
            </b-row>
          </b-form-group>

          <b-form-group
            id="input-group-3"
            label-for="input-3">
            <b-form-input
              id="input-3"
              placeholder="Date de naissance"
              required
              v-model="personal.birthday"
              />
          </b-form-group>
          <b-form-group
            id="input-group-4"
            label-for="input-4">
            <b-form-input
              id="input-4"
              placeholder="Email"
              required
              v-model="personal.email"
              />
          </b-form-group>

          <div class="weight mb-2"> Adresse </div>

          <b-form-group
              id="input-group-4"
              label-for="input-4">
              <b-form-input
                id="input-4"
                placeholder="Nom et numéro de voie"
                required
                v-model="personal.streetname"
                />
              <b-form-input
                id="input-5"
                placeholder="Complément d'adresse"
                required
                v-model="personal.additionalstreetname"
                />
              <b-form-input
                id="input-5"
                placeholder="Code postal"
                required
                v-model="personal.postalcode"
                />
              <b-form-input
                id="input-6"
                placeholder="Ville"
                required
                v-model="personal.town"
                />
            </b-form-group>
            <div v-for="(question, i) in questions" v-bind:question="question" v-bind:key="i">
              Question {{ index }} : {{ question.text }}
              <b-form-textarea
                v-model="answers[i].answer"
                placeholder="Réponse"
                />
            </div>
            <b-button type="submit" class="primary-button"> Continuer </b-button>
          </b-form>
        </div>
      </div>
    </b-container>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios'

export default Vue.extend({
  name: 'FormPage',
  data: () => {
    return {
      number: '',
      personal: {
        familyname: '',
        name: '',
        birthday: '',
        email: '',
        streetname: '',
        additionalstreetname: '',
        postalcode: '',
        town: ''
      },
      questions: [
        { text: 'Toto?' },
        { text: 'Tato?' },
        { text: 'Tito?' },
        { text: 'Tuto?' }
      ],
      answers: [
        { answer: '' },
        { answer: '' },
        { answer: '' },
        { answer: '' }
      ]
    }
  },
  methods: {
    /* eslint-disable-next-line */
    submitAnswers (event: any) {
      event.preventDefault()

      console.log('Submit')
    }
  }
})
</script>

<!-- Fix hardcoded em, % doesn't work and i'm not sure how to fix it -->
<!-- Fix button same size -->
<style scoped>
.logo {
  width: 10em;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.weight {
  font-weight: 600;
}

.form-style {
  border-radius: var(--global-border-radius) !important;
  border: black 1px solid !important;
  background-color: white;
}

</style>
