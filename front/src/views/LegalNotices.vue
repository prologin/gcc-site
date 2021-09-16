<template>
    <div class="basic-background">
        <Header />
            <b-jumbotron class="mx-5 px-5">
                <template #header>Mentions Légales</template>

                <template #lead>
                    Les stages Girls Can Code! sont organisés par l'association <a href="https://prologin.org/">Prologin</a> pour les jeunes collégiennes et lycéennes pour leur faire découvrir l'informatique.
                </template>
                <hr class="my-4">
                <b-row>
                    <b-col class="my-auto">
                        <span class="light-text">Adresse :</span><br>
                        Association Prologin<br>
                        14-16 Rue Voltaire<br>
                        94270 Le Kremlin Bicêtre<br><br>

                        <span class="light-text">Téléphone :</span><br>
                        +331 44 08 01 90<br><br>

                        <span class="light-text">E-mail :</span><br>
                        info@prologin.org<br><br>
                    </b-col>
                    <b-col>
                        <span class="light-text">Statut légal</span><br>
                        Prologin est une association loi de 1901, déclarée à la sous-préfecture de L'Hay-les-Roses le 04-08-2000.<br><br>

                        <span class="light-text">Numéro de déclaration CNIL :</span><br>
                        830039.<br><br>

                        <span class="light-text">Conformément à l'article 34 de la loi « Informatique et Liberté », vous disposez d'un droit d'accès, de rectification et suppression des données à caractère personnel vous concernant. Pour exercer ce droit, veuillez contacter Prologin en utilisant l'une des méthodes listées dans l'encart « Informations de contact. »</span>
                    </b-col>
                </b-row>
            </b-jumbotron>
      <Footer />
    </div>
</template>

<script>
import Vue from 'vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default Vue.extend({
  name: 'LegalNotices',
  components: {
    Header,
    Footer
  }
})
</script>

<style>

</style>
