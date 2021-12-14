<template>
  <!--

    Set the |target| attribute to '_blank' so when someone clicks on the
    link, it will open up in a new tab, or possibly a new window
    depending on the person's browser settings.

    The |rel| attribute sets the relationship between your page and the
    linked URL. Setting it to 'noopener noreferrer' is to prevent a
    typen of phishing known as tabnabbing.

    Source: https://www.freecodecamp.org/news/how-to-use-html-to-open-link-in-new-tab/
  -->
  <a :href="`${link}`" target="_blank" rel="noopener noreferrer" >
    <img class="picture-size social-network-icon"
         :src="require(`@/assets/${imgName}`)"
         :alt="`${alt}`" />
  </a>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'SocialNetwork',
  props: ['link', 'imgName', 'alt']
})

</script>
<style>
.social-network-icon:hover {
  filter: brightness(2);
}
</style>
