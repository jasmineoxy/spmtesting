<template>
  <div>
    <header>
      <nav>
        <h1>
          <router-link to="/">All In One</router-link>
        </h1>
        <ul>
          <li>
            <router-link to="/courses" class="user" @click="changeUser('learner')">LEARNER</router-link>
          </li>
          <li>
            <router-link to="/courses" class="user" @click="changeUser('hr')">HR</router-link>
          </li>
        </ul>
      </nav>
    </header>
    <ul id="title">
        <li><h3>All Courses</h3></li>
        <li v-if="isLearner">
          <router-link to="/myCourses">My Courses</router-link>
          </li>
      </ul>
  </div>
</template>
<script>
export default {
  methods: {
    changeUser(role) {
      this.$store.dispatch('setUser',role)
      console.log(this.$store.getters.getUserState);
    }
  },
  computed: {
    isLearner() {
      return this.$store.getters.getUserState == 'learner'
    }
  },
}
</script>
<style scoped>
header {
  width: 100%;
  height: 5rem;
  /* background-color: #F0F0F0; */
  display: flex;
  justify-content: center;
  align-items: center;
}

header a {
  text-decoration: none;
  color: black;
  display: inline-block;
  padding: 0.75rem 1.5rem;
  border: 1px solid transparent;
}

/* a:active,
a:hover,
a.router-link-active, */
.user {
  background-color: #FFCC00;
  border-radius: 5px;
}

h1 {
  margin: 0;
}

h1 a {
  color: black;
  margin: 0;
}

h1 a:hover,
h1 a:active,
h1 a.router-link-active {
  border-color: transparent;
}

header nav {
  width: 90%;
  margin: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

li {
  margin: 0 0.5rem;
}

a {
  text-decoration: none;
}

#title {
   width: 100%;
  height: 2rem;
  background-color: #F0F0F0;
  display: flex;
  justify-content: left;
  align-items: center;
}
</style>