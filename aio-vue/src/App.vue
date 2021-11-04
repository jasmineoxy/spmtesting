<template>
<the-header></the-header>
  <!-- <courses-list msg="Check out our courses below"/> -->
  <router-view/>
</template>

<script>
import TheHeader from './components/layout/TheHeader.vue'


export default {
  name: 'App',
  components: {
    TheHeader,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
