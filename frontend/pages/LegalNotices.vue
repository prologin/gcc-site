<template>
  <div class="main-body-style">
    <b-container fluid class="p-0 content">
      <Header />
      <div class="basic-background">
        <b-jumbotron class="mx-5 px-5">
          <template #header> Mentions Légales </template>

          <template #lead>
            Les stages Girls Can Code! sont organisés par l'association
            <a href="https://prologin.org/">Prologin</a>
            pour les jeunes collégiennes et lycéennes pour leur faire découvrir
            l'informatique.
          </template>
          <hr class="my-4" />
          <b-row>
            <b-col class="my-auto">
              <span class="light-text">Adresse :</span><br />
              {{ Constants.ADDRESS_LINE_1 }}<br />
              {{ Constants.ADDRESS_LINE_2 }}<br />
              {{ Constants.ADDRESS_LINE_3 }}<br /><br />

              <span class="light-text">Téléphone :</span><br />
              {{ Constants.CONTACT_PHONE }}<br /><br />

              <span class="light-text">E-mail :</span><br />
              {{ Constants.CONTACT_EMAIL }}<br /><br />
            </b-col>
            <b-col>
              <span class="light-text">Statut légal</span><br />
              Prologin est une association loi de 1901, déclarée à la
              sous-préfecture de L'Hay-les-Roses le 04-08-2000.<br /><br />

              <span class="light-text">Numéro de déclaration CNIL :</span><br />
              {{ Constants.CNIL_DECL_NUM }}<br /><br />

              <span class="light-text">Conformément à l'article 34 de la loi « Informatique et Liberté
                », vous disposez d'un droit d'accès, de rectification et
                suppression des données à caractère personnel vous concernant.
                Pour exercer ce droit, veuillez contacter Prologin en utilisant
                l'une des méthodes listées sur cette page.</span>
            </b-col>
          </b-row>
        </b-jumbotron>
      </div>
      <Footer />
    </b-container>
  </div>
</template>

<script>
import Vue from 'vue';
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';

import * as Constants from '@/constants';

export default Vue.extend({
  name: 'LegalNotices',
  components: {
    Header,
    Footer
  },
  created () {
    this.Constants = Constants
  },
})
</script>
