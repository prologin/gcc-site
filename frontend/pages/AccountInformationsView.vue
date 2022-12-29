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
      <p>
        Les stages Girls Can Code! sont organisés par l'Association Prologin,
        qui agit en tant que contrôleur de données. Les réponses collectées dans
        ce formulaire nous permettent de préparer le stage: sélections,
        documents, nourritures, etc. Pour en apprendre plus à propos de notre
        gestion des données et de vos droits, consultez
        <NuxtLink to="/Privacy"> page dédiée </NuxtLink>
      </p>
    </div>
    <b-row class="mx-0 mx-md-5">
      <b-col class="d-none d-md-block col-md-3">
        <div class="sidebar-item">
          <div class="make-me-sticky">
            <b-button
              class="secondary-button"
              block
              @click="scrollTo('personal-info', 'center')"
            >
              <b-icon-person-circle aria-hidden="true" class="mr-3" />
              Informations personnelles
            </b-button>
            <b-button
              class="secondary-button"
              block
              @click="scrollTo('email', 'center')"
            >
              <b-icon-envelope aria-hidden="true" class="mr-3" />
              E-mail
            </b-button>
            <b-button
              class="secondary-button"
              block
              @click="scrollTo('password', 'center')"
            >
              <b-icon-unlock aria-hidden="true" class="mr-3" />
              Mot de passe
            </b-button>
            <b-button
              class="secondary-button"
              block
              @click="scrollTo('notifications', 'center')"
            >
              <b-icon-bell aria-hidden="true" class="mr-3" />
              Gestion des notifications
            </b-button>
            <b-button
              class="secondary-button"
              block
              @click="scrollTo('rgpd', 'center')"
            >
              <b-icon-gear aria-hidden="true" class="mr-3" />
              Archive des données
            </b-button>
            <b-button
              class="secondary-button"
              block
              @click="scrollTo('delete', 'center')"
            >
              <b-icon-exclamation-diamond aria-hidden="true" class="mr-3" />
              Suppression de compte
            </b-button>
          </div>
        </div>
      </b-col>

      <b-col>
        <b-col id="personal-info" md="12" class="mb-5 p-5 account-group">
          <h1>Informations personnelles</h1>
          <h3>
            Informations traitées seulement en cas de sélection à un stage,
            d'appel d'urgence, d'envois de courrier ou d'email ou lors de la
            connexion.
          </h3>
          <b-row class="mt-3">
            <b-col md="6">
              <b-form-group
                id="input-group-3"
                label="Nom :"
                label-for="input-3"
              >
                <b-form-input
                  id="input-3"
                  v-model="accountInfo.lastName"
                  block
                  type="text"
                  placeholder="Entrer votre nom"
                  required
                />
              </b-form-group>
            </b-col>
            <b-col md="6">
              <b-form-group
                id="input-group-4"
                label="Prénom :"
                label-for="input-4"
              >
                <b-form-input
                  id="input-4"
                  v-model="accountInfo.firstName"
                  type="text"
                  placeholder="Entrer votre prénom"
                  required
                />
              </b-form-group>
            </b-col>
          </b-row>

          <b-form-group
            id="input-group-5"
            class="mt-3"
            label="Adresse :"
            label-for="input-5"
          >
            <b-form-input
              id="input-5"
              v-model="accountInfo.address.numberAndRoad"
              type="text"
              placeholder="Nom et numéro de voie"
            />
            <b-input-group>
              <b-form-input
                id="input-6"
                v-model="accountInfo.address.postalCode"
                type="text"
                placeholder="Code postal"
              />
              <b-form-input
                id="input-7"
                v-model="accountInfo.address.city"
                type="text"
                placeholder="Ville"
              />
            </b-input-group>
            <b-form-input
              id="input-8"
              v-model="accountInfo.address.country"
              type="text"
              placeholder="Pays"
            />
          </b-form-group>

          <b-col offset-md="8" class="mt-5 p-0 col-12 col-md-4">
            <!-- TODO: Add save account information API call -->
            <b-button class="primary-button" block> Sauvegarder </b-button>
          </b-col>
        </b-col>

        <b-col id="email" md="12" class="my-5 p-5 account-group">
          <h1>Changer d'adresse email</h1>
          <b-form-group
            id="input-group-email"
            label="E-mail :"
            label-for="input-current-email"
          >
            <b-form-input
              id="input-current-email"
              v-model="email"
              type="email"
              placeholder="Entrer votre nouvel email"
              required
            />
          </b-form-group>

          <b-col offset-md="8" class="mt-5 p-0 col-12 col-md-4">
            <!-- TODO: Add change email API -->
            <b-button class="primary-button" block> Sauvegarder </b-button>
          </b-col>
        </b-col>

        <b-col id="password" md="12" class="my-5 p-5 account-group">
          <h1>Changer de mot de passe</h1>
          <b-form-group
            id="input-group-password-current"
            label="Mot de passe actuel :"
            label-for="input-current-password"
          >
            <b-form-input
              id="input-current-password"
              v-model="oldPassword"
              type="password"
              placeholder="Entrer votre ancien mot de passe"
              required
            />
          </b-form-group>
          <b-form-group
            id="input-group-password-new"
            label="Nouveau mot de passe :"
            label-for="input-new-password"
          >
            <b-form-input
              id="input-new-password"
              v-model="newPassword"
              type="password"
              placeholder="Entrer votre nouveau mot de passe"
              required
            />
          </b-form-group>
          <b-form-group
            id="input-group-password-confirm"
            label="Confirmer le nouveau mot de passe :"
            label-for="input-confirm-password"
          >
            <b-form-input
              id="input-confirm-password"
              v-model="confirmPassword"
              type="password"
              placeholder="Confirmer votre nouveau mot de passe"
              required
            />
          </b-form-group>

          <b-col offset-md="8" class="mt-5 p-0 col-12 col-md-4">
            <!-- TODO: Add change password API -->
            <b-button class="primary-button" block> Sauvegarder </b-button>
          </b-col>
        </b-col>

        <b-col id="notifications" md="12" class="my-5 p-5 account-group">
          <h1>Notifications</h1>
          <h3>Gérez les autorisations.</h3>
          <b-form-group
            v-slot="{ ariaDescribedby }"
            label="Recevoir par email les prochains stages"
          >
            <b-form-radio-group
              id="radio-group-5"
              v-model="accountInfo.newsletter"
              :aria-describedby="ariaDescribedby"
              required
            >
              <b-form-radio value="YES"> Oui </b-form-radio>
              <b-form-radio value="NO"> Non </b-form-radio>
            </b-form-radio-group>
          </b-form-group>

          <b-col offset-md="8" class="mt-5 p-0 col-12 col-md-4">
            <!-- TODO: Add newsletter managment API call -->
            <b-button class="primary-button" block> Sauvegarder </b-button>
          </b-col>
        </b-col>

        <b-col id="rgpd" md="12" class="my-5 p-5 account-group">
          <h1>Exporter vos données personnelles</h1>
          <h3>
            Vous pouvez télécharger une archive contenant toutes vos données
            personnelles, comme prévu par le Droit à la portabilité (Art. 20 du
            RGPD).
          </h3>
          <b-col offset-md="8" class="mt-5 p-0 col-12 col-md-4">
            <!-- TODO: Add getGDPRArchive API call -->
            <b-button class="primary-button" block> Télécharger </b-button>
          </b-col>
        </b-col>

        <b-col id="delete" md="12" class="my-5 p-5 account-group">
          <h1>Supprimer votre compte</h1>
          <h3>
            Vous pouvez supprimer votre compte et toutes les données
            personnelles associées, comme prévu par votre Droit à la suppression
            (Art. 17 du RGPD).
          </h3>
          <b-col offset-md="8" class="mt-5 p-0 col-12 col-md-4">
            <!-- TODO: Add API call to delete account -->
            <!-- TODO: Add modal to ensure that the user will lose all informations and confirm -->
            <!-- MAYBE: Add text field or some radio button to know why the user delete the account -->
            <b-button class="primary-button red-button" block>
              Supprimer
            </b-button>
          </b-col>
        </b-col>
      </b-col>
    </b-row>

    <Footer />
  </b-container>
</template>

<script>
import Vue from "vue";
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

export default Vue.extend({
  name: 'AccountPage',
  components: {
    Header,
    Footer,
  },
  middleware: "auth",
  data () {
    return {
      accountInfo: null,
      oldPassword: '',
      newPassword: '',
      confirmPassword: '',
      email: '',
    }
  },
  created () {
    this.accountInfo = {
      address: {
        numberAndRoad: this.$store.getters.getAddress,
        postalCode: this.$store.getters.getZipCode,
        city: this.$store.getters.getCity,
        country: this.$store.getters.getCountry
      },
      email: this.$store.getters.getEmail,
      firstName: this.$store.getters.getFirstName,
      lastName: this.$store.getters.getLastName,
      newsletter: 'NO',
    }
    this.email = this.$store.getters.getEmail
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
  background-image: url("~@/assets/basic_background.svg");
  background-position: top left;
  background-repeat: no-repeat;
  background-size: cover;
}

.red-button {
  background-color: #c70039;
  border: none;
}

.red-button:hover {
  background-color: #900c3f;
}
</style>
