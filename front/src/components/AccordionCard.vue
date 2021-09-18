<template>
  <b-card no-body>
    <b-card-header header-tag="header" role="tab">
      <b-row class="secondary-button px-4" v-b-toggle="'accordion-' + index">
        {{ title }}

        <span class="when-closed ml-auto">
          <b-icon icon="caret-down-fill"/>
        </span>
        <span class="when-open ml-auto">
          <b-icon icon="caret-up-fill"/>
        </span>
      </b-row>
    </b-card-header>
    <b-collapse :id="'accordion-' + index" role="tabpanel">
      <b-card-body>
        <b-card-text v-html="content" />
      </b-card-body>
    </b-collapse>
  </b-card>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'Accordion',
  props: ['index', 'title', 'content']
})

</script>

<style>
.card, .card-header {
  background-color: white !important;
}

.collapsed > .when-open,
.not-collapsed > .when-closed {
  display: none;
}
</style>
