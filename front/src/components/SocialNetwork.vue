<template>
    <a :href="`${link}`">
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
