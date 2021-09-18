<template>
  <div class="basic-background">
    <Header />
    <b-container>
    <h1 class="text-center m-3">Girls Can Code! (GCC!) et vos données personnelles</h1>
    <b-container class="accordion mb-1" role="tablist">
      <AccordionCard v-for="(privacy_element, index) in privacy_list"
      v-bind:key="index"
      v-bind:index="index"
      v-bind:title="privacy_element.title"
      v-bind:content="privacy_element.content"/>
    </b-container>
    </b-container>
    <Footer />
  </div>
</template>

<script>
import Vue from 'vue'
import AccordionCard from '@/components/AccordionCard.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default Vue.extend({
  name: 'Privacy',
  components: {
    AccordionCard,
    Footer,
    Header
  },
  data () {
    return {
      privacy_list: [
        {
          title: 'Objet du traitement de données',
          content: '<h4>Finalités</h4><p>Le traitement a pour objet <strong>l\'organisation des stages Girls Can Code! (GCC!)</strong>.<br>Il permet à l\'association Prologin :</p><ul><li>de traiter les demandes de participation ;</li> <li>d\'attribuer ou non une bourse financière ;</li> <li>d\'adapter le contenu pédagogique aux attentes des participantes ;</li> <li>d\'adapter les repas aux contraintes alimentaires de chacune ;</li> <li>de répondre aux sollicitations de la part des participantes ;</li> <li>de piloter les stages (évaluation de la satisfaction des participantes, production de statistiques).</li> </ul><p></p><h4>Base légale</h4><p>Ce traitement repose sur le consentement des inscrits et de leur responsable légal le cas échéant (mineures de 16 ans), ce sont les articles 6(1)a et 8 du RGPD.</p>'
        },
        {
          title: 'Données traitées',
          content: '<h4>Catégories de données traitées</h4><ul> <li>Données d\'identification : nom, prénom, adresse postale... ;</li> <li>Vie scolaire (dite professionnelle) : niveau d\'étude ;</li> <li>Vie personnelle : habitudes alimentaires ;</li> <li>Informations d\'ordre économique et financier, si une demande de bourse est faite par la participante ;</li> <li>Internet : mesure d\'audience ;</li> <li>Données de santé : éventuels traitements médicaux et allergies.</li></ul><h4>Source des données</h4><p>Ces informations sont recueillies directement auprès de la participante, et/ou de son responsable légal le cas échéant (mineures de 16 ans).</p><h4>Caractère obligatoire des réponses</h4><p>L\'inscription à un stage GCC! prévoit, sauf mention contraire, le recueil obligatoire de données qui sont nécessaires au traitement de l\'inscription.</p><h4>Prise de décision automatisée</h4><p>Le traitement ne prévoit pas de prise de décision automatisée : toutes les demandes d\'inscription sont revues par un être humain :)</p>'
        },
        {
          title: 'Personnes concernées',
          content: '<p>Le traitement de données concerne :</p><ul> <li>les personnes physiques souhaitant participer à un stage GCC! ;</li> <li>les responsables légaux des personnes ci-dessus le cas échéant (mineures de 16 ans) ;</li> <li>les membres de Prologin chargés de l\'organisation des stages ;</li> <li>les personnes physiques ou morales partenaires ou sous-traitants de Prologin.</li> </ul><p></p>'
        },
        {
          title: 'Destinataires des données',
          content: '<h4>Catégories de destinataires</h4><p>En fonction de leurs besoins respectifs, sont destinataires de tout ou partie des données : </p><ul> <li>les membres autorisés de Prologin ;</li> <li>les membres autorisés des partenaires et/ou sous-traitants de Prologin ;</li> <li>les autres participantes à un même stage ;</li> <li>les services de secours d\'urgence en cas de besoin.</li> </ul><p></p><h4>Transfert des données hors UE</h4><p>Aucun transfert de données hors de l\'Union européenne n\'est réalisé.</p>'
        },
        {
          title: 'Durée de conservation',
          content: '<p>Les données d’identification, de vie scolaire et personnelle sont conservées jusqu\'à la désinscription de la personne.<br>Les informations d\'ordre économique et financier sont conservées le temps d\'attribuer ou non une bourse plus un mois.<br>Les données de santé sont conservées jusqu\'à 3 ans après la fin du stage.</p>'
        },
        {
          title: 'Sécurité',
          content: '<p>Des mesures de sécurité visant à garantir la confidentialité, l\'intégrité et la disponibilité des données collectées, issues du référentiel ISO/IEC27002 ont été mises en œuvre. Elles comprennent, sans s\'y limiter, le chiffrement des données en transit et leur sauvegarde régulière externalisée.</p>'
        },
        {
          title: 'Vos droits sur vos données',
          content: '<h4>L\'essentiel</h4><p>Vous disposez (le cas échéant <em>via</em> le responsable légal) des droits d\'accéder et d\'obtenir copie des données vous concernant, de vous opposer au traitement de ces données, de les faire rectifier ou les faire effacer. Vous disposez également d\'un droit à la limitation du traitement de vos données. <a href="https://www.cnil.fr/fr/comprendre-vos-droits">Rendez-vous sur le site de la CNIL pour mieux comprendre vos droits.</a></p><h4>Exercer vos droits</h4><p>Toute demande d\'exercice de vos droits doit être adressée par voie électronique à <a href="mailto:info@prologin.org">info@prologin.org</a>.</p><h4>Réclamation auprès de la CNIL</h4><p>Si vous estimez, après nous avoir contacté, que vos droits sur vos données ne sont pas respectés, vous pouvez alors <a href="https://www.cnil.fr/fr/webform/adresser-une-plainte">adresser une réclamation à la CNIL</a>.</p>'
        }
      ]
    }
  }
})
</script>

<style>
</style>
