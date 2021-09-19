<template>
    <div class="background-style text-center py-5">
        <div class="mx-2 mx-sm-auto">
          <h1>S'inscrire à la newsletter</h1>
          <h3>Pour être tenu au courant de nos prochains évènements.</h3>
          <h4>Nous n'aimons pas le spam et nous ne partagerons jamais votre adresse email.</h4>
        </div>
        <b-form class="col-sm-7 mx-auto my-4" @submit="onSubmit">
            <b-input-group
                id="input-group-1"
                label-for="input-1"
                >
                <b-form-input
                    id="input-1"
                    v-model="form.email"
                    type="email"
                    placeholder="Votre.email@example.com"
                    class="rounded-input-left"
                    required
                    >
                </b-form-input>
                <b-input-group-append>
                    <b-button type="submit" class="primary-button rounded-input-right d-none d-sm-block">S'inscrire maintenant</b-button>
                    <b-button type="submit" class="primary-button rounded-input-right d-block d-sm-none">S'inscrire</b-button>
                </b-input-group-append>
            </b-input-group>
        </b-form>
    </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'Newsletter',
  data () {
    return {
      form: {
        email: ''
      }
    }
  },
  methods: {
    onSubmit (event) {
      event.preventDefault()
      alert(JSON.stringify(this.form))
    }
  }
})
</script>

<style scoped>
.background-style {
  background-color: #efefef;
  background-image: url('~@/assets/newsletter_bg.svg');
  background-repeat:no-repeat;
  background-size:cover;
}

.rounded-input-left {
  border-top-left-radius: var(--global-border-radius) !important;
  border-bottom-left-radius: var(--global-border-radius) !important;
}

.rounded-input-right {
  border-top-right-radius: var(--global-border-radius) !important;
  border-bottom-right-radius: var(--global-border-radius) !important;
}
</style>
