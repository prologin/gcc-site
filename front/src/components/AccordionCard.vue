<template>
  <b-card no-body>
    <b-card-header class="p-1" header-tag="header" role="tab">
      <b-button class="primary-button" block v-b-toggle="'accordion-' + index">
        {{ title }}

        <span class="when-closed">
          <b-icon icon="caret-down-fill"/>
        </span>
        <span class="when-open">
          <b-icon icon="caret-up-fill"/>
        </span>
      </b-button>
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
  border: none !important;
  background-color: white !important;
}

.collapsed > .when-open,
.not-collapsed > .when-closed {
  display: none;
}
</style>
