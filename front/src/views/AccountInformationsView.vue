<template>
  <!--
    TODO: To avoid useless API call, save current information and look if
    there is any difference before calling the API when the user click on save
    button
  -->
  <!--
    TODO: Rename properly id
  -->
  <b-container class="main-body-style px-0" fluid no-gutters>
    <Header />
      <div class="mx-5 my-4">
        <h2>Gestion du compte</h2>
        <p>Les stages Girls Can Code! sont organisés par l'Association
        Prologin, qui agit en tant que contrôleur de données. Les réponses
        collectées dans ce formulaire nous permettent de préparer le stage:
        sélections, documents, nourritures, etc. Pour en apprendre plus
        à propos de notre gestion des données et de vos droits, consultez
        notre <b-link :to="{ name: 'privacy' }">page dédiée</b-link></p>
      </div>
      <b-row class="mx-0 mx-md-5">
        <b-col class="d-none d-md-block col-md-3">
          <div class="sidebar-item">
            <div class="make-me-sticky">
              <b-button class="secondary-button" block @click="scrollTo('personal-info')">
                <b-icon-person-circle aria-hidden="true" class="mr-3" />
                  Informations personnelles
              </b-button>
              <b-button class="secondary-button" block @click="scrollTo('password')" >
                <b-icon-unlock aria-hidden="true" class="mr-3"/>
                  Mot de passe
              </b-button>
                <b-button class="secondary-button" block @click="scrollTo('notifications')">
                  <b-icon-envelope aria-hidden="true" class="mr-3" />
                    Gestions des notifications
                </b-button>
                <b-button class="secondary-button" block @click="scrollTo('rgpd')">
                  <b-icon-gear aria-hidden="true" class="mr-3" />
                    Archive des données
                </b-button>
                <b-button class="secondary-button" block @click="scrollTo('delete')">
                  <b-icon-exclamation-diamond aria-hidden="true" class="mr-3" />
                    Suppression de compte
                </b-button>
            </div>
          </div>
        </b-col>

        <b-col>
          <b-col md="12" id="personal-info" class="mb-5 p-5 account-group">
            <h1>Informations personnelles</h1>
            <h3>Informations traitées seulement en cas de sélection à un stage, d'appel d'urgence, d'envois de courrier ou d'email ou lors de la connexion.</h3>
            <b-row class="mt-3">
              <b-col md="6">
                <b-form-group id="input-group-3" label="Nom :" label-for="input-3">
                  <b-form-input block id="input-3" v-model="accountInfo.lastName" type="text" placeholder="Entrer votre nom" required/>
                </b-form-group>
              </b-col>
              <b-col md="6">
                <b-form-group id="input-group-4" label="Prénom :" label-for="input-4">
                  <b-form-input id="input-4" v-model="accountInfo.firstName" type="text" placeholder="Entrer votre prénom" required/>
                </b-form-group>
              </b-col>
            </b-row>

            <b-form-group class="mt-1" id="input-group-1" label="Email :" label-for="input-1">
              <b-form-input id="input-1" v-model="accountInfo.email" type="email" placeholder="Entrer votre email" required/>
            </b-form-group>

            <b-form-group class="mt-3" id="input-group-5" label="Adresse :" label-for="input-5">
              <b-form-input id="input-5" v-model="accountInfo.address.numberAndRoad" type="text" placeholder="Nom et numéro de voie"/>
                <b-form-input id="input-5" v-model="accountInfo.address.complementary" type="text" placeholder="Complément d'adresse"/>
                  <b-input-group>
                    <b-form-input id="input-5" v-model="accountInfo.address.postalCode" type="text" placeholder="Code postal"/>
                      <b-form-input id="input-5" v-model="accountInfo.address.city" type="text" placeholder="Ville"/>
                  </b-input-group>
            </b-form-group>

            <b-form-group class="my-3" id="input-group-6" label="Numéro de téléphone :" label-for="input-6" description="Ex: +33 6 12 34 56 78">
              <b-form-input id="input-6" v-model="accountInfo.phone" type="tel" placeholder="Entrer votre numéro de téléphone"/>
            </b-form-group>

            <b-col offset-md="8" class="mt-5 p-0 col-12 col-md-4">
              <!-- TODO: Add save account information API call -->
              <b-button class="primary-button" block>Sauvegarder</b-button>
            </b-col>
          </b-col>

          <b-col md="12" class="my-5 p-5 account-group" id="password">
            <h1>Changer de mot de passe</h1>
            <b-form-group id="input-group-mdp-current" label="Mot de passe actuel :" label-for="input-current">
              <b-form-input id="input-current" v-model="accountInfo.oldPassword" type="password" placeholder="Entrer votre ancien mot de passe" required/>
            </b-form-group>
            <b-form-group id="input-group-mdp-new" label="Nouveau mot de passe :" label-for="input-new">
              <b-form-input id="input-new" v-model="accountInfo.newPassword" type="password" placeholder="Entrer votre nouveau mot de passe" required/>
            </b-form-group>
            <b-form-group id="input-group-mdp-confirm" label="Confirmer le nouveau mot de passe :" label-for="input-confirm">
              <b-form-input id="input-confirm" v-model="accountInfo.confirmPassword" type="password" placeholder="Confirmer votre nouveau mot de passe" required/>
            </b-form-group>

            <b-col offset-md="8" class="mt-5 p-0 col-12 col-md-4">
              <!-- TODO: Add change password API -->
              <b-button class="primary-button" block>Sauvegarder</b-button>
            </b-col>
          </b-col>

          <b-col md="12" class="my-5 p-5 account-group" id="notifications">
            <h1>Notifications</h1>
            <h3>Gérez les autorisations.</h3>
            <b-form-group label="Recevoir par email les prochains stages" v-slot="{ ariaDescribedby }">
              <b-form-radio-group
                id="radio-group-5"
                v-model="accountInfo.newsletter"
                :aria-describedby="ariaDescribedby"
                required
                >
                <b-form-radio value="YES">Oui</b-form-radio>
                <b-form-radio value="NO">Non</b-form-radio>
              </b-form-radio-group>
            </b-form-group>

            <b-col offset-md="8" class="mt-5 p-0 col-12 col-md-4">
              <!-- TODO: Add newsletter managment API call -->
              <b-button class="primary-button" block>Sauvegarder</b-button>
            </b-col>
          </b-col>

          <b-col md="12" class="my-5 p-5 account-group" id="rgpd">
            <h1>Exporter vos données personnelles</h1>
            <h3>Vous pouvez télécharger une archive contenant toutes vos données personnelles, comme prévu par le Droit à la portabilité (Art. 20 du RGPD).</h3>
            <div class="mt-4">
              <!-- TODO: Add getGDPRArchive API call -->
              <b-button class="primary-button" block>Télécharger</b-button>
            </div>
          </b-col>

          <b-col md="12" class="my-5 p-5 account-group" id="delete">
            <h1>Supprimer votre compte</h1>
            <h3>Vous pouvez supprimer votre compte et toutes les données personnelles associées, comme prévu par votre Droit à la suppression (Art. 17 du RGPD).</h3>
            <div class="mt-4">
              <!-- TODO: Add API call to delete account -->
              <!-- TODO: Add modal to ensure that the user will lose all informations and confirm -->
              <!-- MAYBE: Add text field or some radio button to know why the user delete the account -->
              <b-button class="primary-button red-button" block>Supprimer</b-button>
            </div>
          </b-col>
        </b-col>
      </b-row>

      <Footer />
  </b-container>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import Vue from 'vue'

export default Vue.extend({
  name: 'AccountPage',
  components: {
    Header,
    Footer
  },
  data () {
    return {
      accountInfo: null,
      oldPassword: '',
      newPassword: '',
      confirmPassword: ''
    }
  },
  created () {
    // TODO: Add getAllAccountInfo API call, see @/components/EventList.vue for
    // example
    // TODO: Manage error, maybe redirect to 500 error page?
    this.accountInfo = {
      address: {
        numberAndRoad: '14-16 rue Voltaire',
        complementary: '',
        postalCode: '94270',
        city: 'Le KB',
        country: 'France'
      },
      email: 'john.doe@example.com',
      firstName: 'John',
      lastName: 'Doe',
      newsletter: 'NO',
      phone: '06 00 00 00 00'
    }
  }
})
</script>

<style scoped>
.secondary-button {
  text-align: left;
}

.sidebar-item {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.make-me-sticky {
  position: -webkit-sticky;
  position: sticky;
  top: 70px;
}

.account-group {
  border-radius: var(--global-border-radius);
  border: 1px solid var(--light-text-color);
  background-color: white;
}

.main-body-style {
  height: 100%;
  background-attachment: fixed;
  background-image: url('~@/assets/basic_background.svg');
  background-position: top left;
  background-repeat: no-repeat;
  background-size: cover;
}

.red-button {
  background-color: #C70039;
  border: none;
}

.red-button:hover {
  background-color: #900C3F;
}
</style>
