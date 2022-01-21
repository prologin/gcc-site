<template>
  <b-container fluid class="p-0">
    <b-list-group horizontal>
      <b-list-group-item>
        <b-img :src="require(`@/assets/indicator-` + iconImageName + `.svg`)" alt="Status"/>
      </b-list-group-item>
      <b-list-group-item class="d-flex align-items-center light-color-text">
        {{ statusText }}
      </b-list-group-item>
    </b-list-group>
  </b-container>
</template>

<script>
import ApplicationStatusEnum from '@/enums/ApplicationStatusEnum.js'
import Vue from 'vue'

export default Vue.extend({
  name: 'ApplicationStatusComponent',
  mixins: [ApplicationStatusEnum.Mixin],
  props: ['status'],
  computed: {
    iconImageName: function () {
      switch (this.status) {
        case ApplicationStatusEnum.ONGOING:
          return 'loading'
        case ApplicationStatusEnum.REJECTED:
          return 'rejected'
        case ApplicationStatusEnum.ACCEPTED_WAITING_VALIDATION:
          return 'waiting'
        case ApplicationStatusEnum.ACCEPTED_AND_VALIDATED:
          return 'validated'
        case ApplicationStatusEnum.COMPLETE:
          return 'finished'
        default:
          return ''
      }
    },
    statusText: function () {
      switch (this.status) {
        case ApplicationStatusEnum.ONGOING:
          return 'Votre candidature est en cours d\'examen.'
        case ApplicationStatusEnum.REJECTED:
          return 'Votre candidature n\'a pas été retenue.'
        case ApplicationStatusEnum.ACCEPTED_WAITING_VALIDATION:
          return 'Votre canditature a été acceptée, veuillez confirmer votre présence.'
        case ApplicationStatusEnum.ACCEPTED_AND_VALIDATED:
          return 'Votre candidature est complète !'
        case ApplicationStatusEnum.COMPLETE:
          return 'Stage terminé.'
        default:
          return ''
      }
    }
  }
})

</script>
