<template>
  <div>
    <div class="form-page-image-background" />
    <div class="form-page-below-background" />
    <b-container>
      <b-jumbotron class="form-page-form">
        <img :src="require('@/assets/logo_gcc.svg')" alt="Logo des stages Girls Can Code" class="logo" />
        <!-- TODO: [1]-[2]-[3] -->
        <div v-if="state == 0">
          <b-form @submit="submitPersonalInformation" inline>
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
            <b-button type="submit" class="primary-button"> Continuer </b-button>
          </b-form>
        </div>

        <div v-if="state == 1">
          <b-form @submit="submitAnswers" inline>
            <div v-for="(question, i) in questions" v-bind:question="question" v-bind:key="i">
              Question {{ index }} : {{ question.text }}
              <b-form-textarea
                v-model="answers[i].answer"
                placeholder="Réponse"
                />
            </div>
              <b-button type="submit" class="primary-button"> Continuer </b-button>
          </b-form>
          <b-button @click="previousState()" class="primary-button"> Précédent </b-button>
        </div>
        <div v-if="state == 2">
          <b-jumbotron class="recap">
            Informations personnelles :
            <b-row> Prénom {{ personal.name }} </b-row>
            <b-row> Nom de famille : {{ personal.familyname }} </b-row>
            <b-row> Date de naissance : {{ personal.birthday }} </b-row>
            <b-row> Email : {{ personal.email }} </b-row>
            <b-row> Nom et numéro de voie : {{ personal.streetname }} </b-row>
            <b-row> Complément d'adresse : {{ personal.additionalstreetname }} </b-row>
            <b-row> Code postal : {{ personal.postalcode }} </b-row>
            <b-row> Ville : {{ personal.town }} </b-row>
            <b-button @click="setState(0)"> edit </b-button>
          </b-jumbotron>
          <b-jumbotron class="recap">
            <ul>
            <div v-for="(question, i) in questions" v-bind:question="question" v-bind:key="i">
              <li>
              Question {{ i }} : {{ question.text }}
              {{ answers[i].answer }}
              </li>
            </div>
            <b-button @click="setState(1)"> edit </b-button>
            </ul>

          </b-jumbotron>
          <b-button @click="previousState()" class="primary-button"> Précédent </b-button>
        </div>

      </b-jumbotron>
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
      state: 0,
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
    previousState () {
      this.state--
    },
    setState (i: number) {
      this.state = i
    },
    increment () {
      this.state++
    },
    /* eslint-disable-next-line */
    submitPersonalInformation (event: any) {
      event.preventDefault()
      alert(JSON.stringify(this.personal))
      this.increment()
    },
    /* eslint-disable-next-line */
    submitAnswers (event: any) {
      event.preventDefault()
      this.increment()
    }
  }
})
</script>

<!-- Fix hardcoded em, % doesn't work and i'm not sure how to fix it -->
<!-- Fix button same size -->
<style scoped>
.form-page-image-background {
  background-color: black;
  width: 100%;
  height: 30%;
  min-height: 15em;
  margin: 0;
}

.form-page-below-background {
  background-color: #F9F9F9;
  width: 100%;
  height: 70%;
  min-height: 70em;
}

.form-page-form {
  margin-top: -75em;
  min-height: 40em;
  background-color: white;
}

.logo {
  width: 10em;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.wish {
  font-weight: 600;
  font-size: 1.3rem;
}

.weight {
  font-weight: 600;
}

.recap {
  border: solid;
  border-width: 1px;
  background-color: #F9F9F9;
}

</style>
