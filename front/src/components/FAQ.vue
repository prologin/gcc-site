<template>
    <b-container fluid class="faq-background p-2 p-sm-0">
        <b-row>
            <b-col class="col-12 col-sm-8">
                <b-img :src="require('@/assets/photo_1.png')" alt="Photo des stages Girls Can Code!" fluid/>
                    <b-col class="content-background ml-1 ml-sm-5 mr-1 p-3">
                        <h1>Foire Aux Questions</h1>
                        <div class="accordion p-1" role="tablist">
                            <AccordionCard v-for="(faq_elt, index) in faq_entries"
                            v-bind:key="index"
                            v-bind:index="index"
                            v-bind:title="faq_elt.question"
                            v-bind:content="faq_elt.answer"
                            />
                        </div>
                    </b-col>
            </b-col>
            <b-col class="d-none d-sm-block">
                <b-img :src="require('@/assets/photo_2.png')" alt="Photo des stages Girls Can Code!" fluid/>
            </b-col>
        </b-row>
        <b-row>
            <b-col class="d-none d-sm-block">
                <b-img :src="require('@/assets/photo_3.png')" alt="Photo des stages Girls Can Code!" fluid/>
            </b-col>
            <b-col>
                <b-img :src="require('@/assets/photo_4.png')" alt="Photo des stages Girls Can Code!" fluid/>
                    <b-col class="content-background mt-5 p-4 mx-auto back-mode">
                        <h1>Une question ?</h1>
                        <p>Si vous avez une question qui ne figure pas dans la FAQ, vous pouvez nous envoyer un mail à l'adresse suivante :</p>
                        <h3>info@prologin.org</h3>
                    </b-col>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import Vue from 'vue'
import AccordionCard from '@/components/AccordionCard.vue'

export default Vue.extend({
  name: 'FAQ',
  components: {
    AccordionCard
  },
  data () {
    return {
      faq_entries: [
        {
          question: 'Qu\'es ce qu\'un stage GCC! ?',
          answer: '<p>C\'est un stage où vous apprenez et pratiquez la programmation, accompagnées par des étudiants et étudiantes en informatique. Nous proposons deux type de stages :<ul><li> les stages longs qui durent du lundi matin au samedi midi</li><li> Les stages courts qui durent le temps d\'un week-end</li></ul>Le tout dans une atmosphère détendue, nous ne forçons personne, ce stage est là pour vous faire découvrir un domaine afin de vous aider dans votre orientation. Nous ne vous en voudrons pas si vous n\'aimez pas la programmation.<br><br>Nous organisons aussi des conférences animées par des femmes du numérique pour qu\'elles partagent leur vécu dans le monde du travail.</p>'
        },
        {
          question: 'Qui peux s\'inscrire aux stages ?',
          answer: 'Toutes personnes s\'identifiant comme une femme et étant actuellement ou à la rentrée prochaine dans l\'enseignement secondaire (collège et lycée) ou équivalent. Il faut aussi être en capacité d\'être presente sur le lieu du stage quand ceux-ci sont en présentiel.'
        },
        {
          question: 'Combien coûte un stage ?',
          answer: 'Nous prennons en charge l\'ensemble des repas ainsi que tous les frais relatifs aux activités pendant le stage. Si vous avez besoin d\'une aide financière pour le logement et/ou le transport vous pouvez faire une demande de bourse à bourse@prologin.org. Nous pouvons aussi vous mettre en relation avec les autres familles volontaires pour l\'hébergement ou pour du covoiturage, pour cela envoyez un mail à info@prologin.org.'
        },
        {
          question: 'Quels sont les critères de sélection ?',
          answer: 'Nous nous basons principalement sur la motivation et réponses lors de la candidature. Le niveau est absolument pas un critère car nous adaptons les exercices en fonction de celui-ci. Les filles n\'aillant jamais participées au stage sont prioritaires par rapport à celles qui l\'ont déjà fait.'
        },
        {
          question: 'Quel est le niveau requis pour participer ?',
          answer: 'Il n\'y a pas de niveau minimal. Nous nous adaptons à tous les niveaux, il ne faut pas hésiter à nous communiquer s\'il y a des sujets spécifiques que vous souhaitez découvrir ou approfondir. Nous nous adaptons à tous les profils.'
        },
        {
          question: 'Qui organise le stage ?',
          answer: 'Nous somme l\'association Prologin et en plus des stages "Girls Can Code!", nous organisons le concours <a href="https://prologin.org">Prologin</a>. Notre but est de promouvoir l\'informatique auprès des jeunes. Les encadrants sont principalement des étudiants et étudiantes en informatique. Ils sont là pour vous aider dans les exercices et répondre à toutes vos questions que ce soit d\'informatique ou d\'orientation.'
        },
        {
          question: 'Comment bénéficier de la bourse ?',
          answer: 'Il suffit d\'envoyer un mail à bourse@prologin.org et l\'ensemble de la procedure vous sera transmise par un responsable de l\'association.'
        },
        {
          question: 'Peut-on faire le stage plusieurs fois ?',
          answer: 'Oui, c\'est possible cependant vous ne serez pas prioritaire lors de la sélection. De plus, la grande majorité des sujets reste sensiblement les mêmes.'
        },
        {
          question: 'Je ne suis pas éligible aux stages GCC!, que me suggerez vous ?',
          answer: '<h4>Si tu as déjà codé</h4><p>Nous te proposons de participer au concours <a href="https://prologin.org">Prologin</a>.<h4>Si tu souhaites débuter</h4> Tu peux te laisser guider par les exercices de <a href="http://www.france-ioi.org/">France-IOI</a> et si tu te debrouille en anglais, il y a <a href="https://www.codecademy.com/">Codecademy</a>.</p>'
        }
      ]
    }
  }
})
</script>

<style scoped>
.faq-background {
    background-color: #efefef;
    background-image: url(~@/assets/faq_bg.svg);
    background-size: contain;
    background-repeat: no-repeat;
    background-position: bottom 0 right 0;
}
</style>
