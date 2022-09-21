<!-- TODO: Add input validation check https://bootstrap-vue.org/docs/reference/validation -->
<!-- TODO: Add API call -->
<!-- TODO: Check and add legal sentences -->

<template>
  <b-container fluid>
    <b-row align-h="center" class="py-5">
      <b-container fluid align="mb-5">
        <ul class="wizard-h" :style="progressBarCss">
          <li class="l-wizard-h-step" v-bind:class="getWizardClass(this.RegisterStepsEnum.ACCOUNT)">
            <b-icon class="fa" icon="person" aria-hidden="true" scale="0.5"/>
              <span>Compte</span>
          </li>
          <li class="l-wizard-h-step" v-bind:class="getWizardClass(this.RegisterStepsEnum.PERSONAL_INFORMATIONS)">
            <b-icon class="fa" icon="envelope" aria-hidden="true" scale="0.5"/>
              <span>Contact</span>
          </li>
          <li class="l-wizard-h-step" v-bind:class="getWizardClass(this.RegisterStepsEnum.COMPLETED)">
            <b-icon class="fa" icon="check" aria-hidden="true"/>
              <span>Fin</span>
          </li>
        </ul>
      </b-container>

      <b-col md="10" class="mt-5" v-if="this.currentStep === this.RegisterStepsEnum.ACCOUNT">
        <b-form-group id="input-group-1" label="Email :" label-for="input-1">
          <b-form-input id="input-1" v-model="registerForm.email" type="email" placeholder="Entrer votre email" required/>
        </b-form-group>
        <b-form-group id="input-group-2" label="Mot de passe :" label-for="input-2" description="Nous vous recommendons une longueur minimale de 12.">
          <b-form-input id="input-2" v-model="registerForm.password" type="password" placeholder="Entrer un mot de passe" required/>
        </b-form-group>
      </b-col>

      <b-col md="10" class="mt-5" v-if="this.currentStep === this.RegisterStepsEnum.PERSONAL_INFORMATIONS">
        <b-row>
          <b-col md="6">
            <b-form-group id="input-group-3" label="Nom :" label-for="input-3">
              <b-form-input block id="input-3" v-model="registerForm.lastName" type="text" placeholder="Entrer votre nom" required/>
            </b-form-group>
          </b-col>
          <b-col md="6">
            <b-form-group id="input-group-4" label="Prénom :" label-for="input-4">
              <b-form-input id="input-4" v-model="registerForm.firstName" type="text" placeholder="Entrer votre prénom" required/>
            </b-form-group>
          </b-col>
        </b-row>

        <b-form-group class="mt-4" id="input-group-5" label="Adresse : (optionnel)" label-for="input-5">
          <b-form-input id="input-5" v-model="registerForm.address.numberAndRoad" type="text" placeholder="Nom et numéro de voie"/>
            <b-form-input id="input-5" v-model="registerForm.address.complementary" type="text" placeholder="Complément d'adresse"/>
              <b-input-group>
                <b-form-input id="input-5" v-model="registerForm.address.postalCode" type="text" placeholder="Code postal"/>
                  <b-form-input id="input-5" v-model="registerForm.address.city" type="text" placeholder="Ville"/>
              </b-input-group>
        </b-form-group>

        <b-form-group class="my-5" id="input-group-6" label="Numéro de téléphone : (optionnel)" label-for="input-6" description="Ex: +33 6 12 34 56 78">
          <b-form-input id="input-6" v-model="registerForm.phone" type="tel" placeholder="Entrer votre numéro de téléphone"/>
        </b-form-group>
      </b-col>

      <b-col md="12" class="mt-5" v-if="this.currentStep === this.RegisterStepsEnum.COMPLETED">
        <b-form-group label="Recevoir par email les prochains stages" v-slot="{ ariaDescribedby }">
          <b-form-radio-group
            id="radio-group-2"
            v-model="registerForm.newsletter"
            :aria-describedby="ariaDescribedby"
            required
            >
            <b-form-radio value="YES">Oui</b-form-radio>
            <b-form-radio value="NO">Non</b-form-radio>
          </b-form-radio-group>
        </b-form-group>

        <!-- TODO: Add Captcha ? -->
        <h4 class="mt-5">En cliquant sur s'enregistrer, j'autorise l'association Prologin (organisateur des stages Girls can code!) à traiter les informations saisies.</h4>
      </b-col>

      <b-col md="6" class="my-3">
        <b-button block class="secondary-button" v-if="this.currentStep > 0" v-on:click="goPrevious">Précédent</b-button>
      </b-col>
      <b-col md="6" class="my-3">
        <b-button block class="primary-button" v-if="this.currentStep !== this.RegisterStepsEnum.COMPLETED" v-on:click="goNext">Suivant</b-button>
        <b-button block class="primary-button" v-else>S'enregistrer</b-button>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Vue from 'vue'
import RegisterStepsEnum from '@/enums/RegisterStepsEnum.js'

export default Vue.extend({
  name: 'RegisterComponent',
  mixins: [RegisterStepsEnum.Mixin],
  data () {
    return {
      registerForm: {
        address: {
          numberAndRoad: '',
          complementary: '',
          postalCode: '',
          city: '',
          country: ''
        },
        email: '',
        firstName: '',
        lastName: '',
        password: '',
        phone: '',
        newsletter: ''
      },
      currentStep: RegisterStepsEnum.ACCOUNT,
      progressBarCss: 'background: linear-gradient(90deg, var(--main-hover-color) 15%, #dbdbdb 15%);'
    }
  },
  methods: {
    getWizardClass: function (item) {
      if (item < this.currentStep) {
        return 'wizard-h__step--previous'
      } else if (item === this.currentStep) {
        return 'wizard-h__step--current'
      } else {
        return 'wizard-h__step'
      }
    },
    goNext: function () {
      event.preventDefault()
      this.currentStep += 1
      this.computeProgressBar()
    },
    goPrevious: function () {
      this.currentStep -= 1
      this.computeProgressBar()
    },
    computeProgressBar: function () {
      if (this.currentStep === this.RegisterStepsEnum.ACCOUNT) {
        this.progressBarCss = 'background: linear-gradient(90deg, var(--main-hover-color) 15%, #dbdbdb 15%);'
      } else if (this.currentStep === this.RegisterStepsEnum.PERSONAL_INFORMATIONS) {
        this.progressBarCss = 'background: linear-gradient(90deg, var(--main-hover-color) 45%, #dbdbdb 45%);'
      } else {
        this.progressBarCss = 'background: linear-gradient(90deg, var(--main-hover-color) 100%, #dbdbdb 100%);'
      }
    }
  }
})
</script>

<style>
.wizard-h {
  color: #b8b8b8;
  margin-bottom: 0;
  padding: 0;
  position: relative;
  display: flex;
  justify-content: space-around;
}
.wizard-h::before {
  background-image: linear-gradient(white 25%, transparent 25%, transparent 30%, white 30%);
  bottom: 0;
  content: "";
  height: 100%;
  position: absolute;
  width: 100%;
}
.l-wizard-h-step {
  float: left;
  width: calc(100% / 3);
}
.wizard-h .wizard-h__step, .wizard-h .wizard-h__step--previous, .wizard-h .wizard-h__step--current {
  display: inline-block;
  height: 30px;
  line-height: 30px;
  margin-bottom: 20px;
  position: relative;
}
.wizard-h .wizard-h__step--previous {
  color: var(--main-hover-color);
}
.wizard-h .wizard-h__step, .wizard-h .wizard-h__step--previous, .wizard-h .wizard-h__step--current {
  display: inline-block;
  height: calc(100% / 3);
  margin-bottom: 0;
  text-align: center;
}
.wizard-h .wizard-h__step .fa, .wizard-h .wizard-h__step--previous .fa, .wizard-h .wizard-h__step--current .fa {
  background: #f5f5f5 none repeat scroll 0 0;
  border-radius: 50%;
  display: block;
  height: calc(100% / 3 * 2);
  left: 30%;
  line-height: 43px;
  position: relative;
  width: calc(100% / 3);
  text-align: center;
  margin-bottom: 10px;
}
.wizard-h .wizard-h__step--previous .fa {
  background: #f5f5f5 none repeat scroll 0 0;
  border: 2px solid var(--main-hover-color);
  border-radius:50%;
  text-align: center;
}
.wizard-h .wizard-h__step--current {
  color: var(--main-hover-color);
  font-weight: 700;
}
.wizard-h .wizard-h__step--current .fa {
  background: var(--main-hover-color) none repeat scroll 0 0;
  border: 2px solid var(--main-hover-color);
  color: white;
  border-radius:50%;
  text-align: center;
}
.wizard-h .wizard-h__step span, .wizard-h .wizard-h__step--previous span, .wizard-h .wizard-h__step--current span {
  display: inline-block;
}

.form-control {
  border-radius: var(--global-border-radius) !important;
}
</style>
