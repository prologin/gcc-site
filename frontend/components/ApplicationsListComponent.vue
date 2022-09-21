<template>
  <b-container fluid class="p-0">
    <!--

      The following table apply a style for each choosen field as describe
      here:
      https://bootstrap-vue.org/docs/components/table#header-and-footer-custom-rendering-via-scoped-slots

      The following option is needed to be able to click everywhere on the row
      to open the detailed tab.
      @row-clicked="item=>$set(item, '_showDetails', !item._showDetails)"

      More info here:
      https://bootstrap-vue.org/docs/components/table#row-details-support
    -->
    <b-table
      hover
      stacked="lg"
      responsive="xl"
      class="table-style"
      :fields="fields"
      :items="applications"
      thead-class="d-none"
      selectable
      @row-clicked="item=>$set(item, '_showDetails', !item._showDetails && item.status != ApplicationStatusEnum.REJECTED)"
      >

      <template #cell(displayName)="data">
        <b-list-group horizontal>
          <b-list-group-item>
            <b-icon-person-circle aria-hidden="true" font-scale="2" variant="secondary"/>
          </b-list-group-item>
          <b-list-group-item class="d-flex align-items-center light-color-text">
            <h2>{{ data.item.displayName }}</h2>
          </b-list-group-item>
        </b-list-group>
      </template>

      <template #cell(event)="data">
        <h2><b>{{ data.item.eventName }}</b></h2>
        <h3>{{ data.item.eventDate }}</h3>
      </template>

      <template #cell(status)="data">
        <ApplicationStatusComponent v-bind:status="data.item.status" />
      </template>

      <template #cell(selected)="data">
        <div v-if="data.rowSelected && data.item.status != ApplicationStatusEnum.REJECTED">
          <span aria-hidden="true">
            <b-icon font-scale="2" variant="secondary" icon="chevron-compact-up"/>
          </span>
        </div>
        <div v-else-if="data.item.status != ApplicationStatusEnum.REJECTED">
          <span aria-hidden="true">
            <b-icon font-scale="2" variant="secondary" icon="chevron-compact-down"/>
          </span>
        </div>
      </template>

      <template #row-details="data">
          <b-row class="mb-2" v-if="data.item.status != ApplicationStatusEnum.REJECTED">
            <b-col><ApplicationDetailsComponent v-bind:status="data.item.status" /></b-col>
          </b-row>
      </template>
    </b-table>
  </b-container>
</template>

<script>

import Vue from 'vue'
import ApplicationDetailsComponent from '@/components/ApplicationDetailsComponent.vue'
import ApplicationStatusComponent from '@/components/ApplicationStatusComponent.vue'
import ApplicationStatusEnum from '@/enums/ApplicationStatusEnum.js'

export default Vue.extend({
  name: 'ApplicationsList',
  mixins: [ApplicationStatusEnum.Mixin],
  components: {
    ApplicationDetailsComponent,
    ApplicationStatusComponent
  },
  data () {
    return {
      fields: [
        'displayName',
        // A virtual column made up from two fields (eventName, eventDate)
        { key: 'event', label: 'Event info' },
        'status',
        'selected'
      ],
      applications: [
        { id: 1, displayName: '1 Poupette TOTO', eventName: 'Stage long à EPITA Paris', eventDate: '12 janvier au 15 décembre 1245', status: 'ONGOING', buttons: [{ type: 0, title: 'Supprimer la candidature', action: function () { console.log('yea') } }] },
        { id: 2, displayName: '2 Poupette TOTO', eventName: 'Stage court à EPITA Paris', eventDate: '12 janvier au 15 décembre 1245', status: 'REJECTED', buttons: [{ type: 0, title: 'Supprimer la candidature', action: function () { console.log('yea') } }] },
        { id: 3, displayName: '3 Valentin SEUX', eventName: 'Stage long à l’ENS Lyon', eventDate: '12 janvier au 15 décembre 1245', status: 'ACCEPTED_WAITING_VALIDATION', buttons: [] },
        { id: 4, displayName: '4 Poupette TOTO', eventName: 'Stage long à l’ENS Lyon', eventDate: '12 janvier au 15 décembre 1245', status: 'ACCEPTED_AND_VALIDATED', buttons: [{ type: 0, title: 'Confirmer sa venue', action: function () { console.log('yea') } }, { type: 1, title: 'Annuler sa candiature', action: function () { console.log('yea') } }] },
        { id: 5, displayName: '5 Poupette TOTO', eventName: 'Stage long à l’ENS Lyon', eventDate: '12 janvier au 15 décembre 1245', status: 'COMPLETE', buttons: [{ type: 0, title: 'Télécharger ses fichiers', action: function () { console.log('yea') } }, { type: 0, title: 'Voir les photos', action: function () { console.log('yea') } }] }
      ]
    }
  }
})
</script>

<style>
.table-style {
  border-radius: var(--global-border-radius) !important;
  border: black 1px solid !important;
  background-color: white;
}

.list-group-item {
  border: 0 !important;
  background-color: inherit !important;
}

/*
  Disable header in stacked mode (only on mobile) as thead-class="d-none" does
  not work as intended
*/
td::before {
  display: none !important;
}
</style>
