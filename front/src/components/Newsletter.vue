<template>
    <div class="background-style text-center py-5">
        <h1>S'inscrire à la newsletter</h1>
        <h3>Pour être tenu au courant de nos prochains évènements.</h3>
        <h4>Nous n'aimons pas le spam et nous ne partagerons jamais votre adresse email.</h4>
        <b-form class="w-50 mx-auto m-5" @submit="onSubmit">
            <b-input-group
                id="input-group-1"
                label-for="input-1"
                >
                <b-form-input
                    id="input-1"
                    v-model="form.email"
                    type="email"
                    placeholder="Votre.email@example.com"
                    class="rounded-input"
                    required
                    >
                </b-form-input>
                <b-input-group-append>
                    <b-button type="submit" class="primary-button">S'inscrire maintenant</b-button>
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

<style>
.background-style {
  background-color: #efefef;
  background-image: url('../assets/newsletter_bg.svg');
  background-repeat:no-repeat;
  background-size:cover;
}

.rounded-input {
  border-top-left-radius: var(--global-border-radius) !important;
  border-bottom-left-radius: var(--global-border-radius) !important;
}
</style>
