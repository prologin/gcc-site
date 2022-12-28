import Vue from 'vue'

Vue.mixin({
  methods: {
    scrollTo (index: string, pos?: ScrollLogicalPosition) {
      const selectedElement = window.document.getElementById(index)
      if (selectedElement !== null) {
        selectedElement.scrollIntoView({ block: pos || 'start', behavior: 'smooth' })
      }
    }
  }
})
