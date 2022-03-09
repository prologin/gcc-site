<template>
  <b-container class="background-login main-body-style" fluid>
    <b-row class="content col-12 offset-0 col-xl-4 offset-xl-4 p-0" no-gutters>
      <b-col>
        <b-row align-h="center" class="mb-4">
          <b-img :src="require('@/assets/logo_gcc.svg')" />
        </b-row>
        <LoginComponent />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Vue from 'vue'
import LoginComponent from '@/components/LoginComponent.vue'

export default Vue.extend({
  name: 'LoginView',
  components: {
    LoginComponent
  }
})
</script>
<style scoped>
.main-body-style {
  height: 100vh !important;
  background-color: var(--main-light-color) !important;
  padding-top: 0px !important;
}

.content {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.background-login {
  height: 100vh;
  background-image: url('~@/assets/code-background-v2.svg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
</style>
