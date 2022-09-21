<template>
  <b-row v-if="status === ApplicationStatusEnum.ONGOING">
    <b-button class="primary-button mx-3">Modifier sa candidature</b-button>
    <b-button class="primary-button mx-3">Annuler sa candidature</b-button>
  </b-row>
  <b-row v-else-if="status === ApplicationStatusEnum.ACCEPTED_WAITING_VALIDATION">
    <b-button class="primary-button mx-3">Confirmer sa venue</b-button>
    <b-button class="primary-button mx-3">Annuler sa candidature</b-button>
  </b-row>
  <b-row v-else-if="status === ApplicationStatusEnum.ACCEPTED_AND_VALIDATED">
    <b-button class="primary-button mx-3">Télécharger les documents</b-button>
    <b-button class="primary-button mx-3">Annuler sa candidature</b-button>
  </b-row>
  <b-row v-else-if="status === ApplicationStatusEnum.COMPLETE">
    <b-button class="primary-button mx-3">Télécharger ses documents</b-button>
    <b-button class="primary-button mx-3" href="https://www.flickr.com/photos/prologin/albums">Voir les photos</b-button>
  </b-row>
</template>

<script>

import Vue from 'vue'
import ApplicationStatusEnum from '@/enums/ApplicationStatusEnum.js'

export default Vue.extend({
  name: 'ApplicationDetailsComponent',
  mixins: [ApplicationStatusEnum.Mixin],
  props: ['status']
})

</script>
