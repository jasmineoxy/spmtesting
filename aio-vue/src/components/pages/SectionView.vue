<template>
  <div class="hello">
    <section>

    <div class="grid-container">
        <div class="item1">
            <h2>{{sectionDetails.sectionTitle}}</h2>
            <p style="padding: 5px; text-align: justify">{{sectionDetails.content}}</p>
        </div>
        <div class="side">
            <h4 style="padding: 5px">Time Estimate</h4>
            <p>~ {{sectionDetails.estimatedTime}} minutes</p>
        </div>
    </div>
    </section>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
    <base-button> baseButton template</base-button>
    <base-card>baseCard template</base-card>
  </div>
</template>

<script>
import axios from 'axios'
import BaseCard from '../ui/BaseCard.vue';
export default {
  components: {
    BaseCard
    //ClassAssignment,
  },
  data() {
    return {
      sectionDetails: '',
      sectionClassesResponse: '',
      sectionClassesDict: {},
    }
  },
  computed: {
    isLearner() {
      var user = this.$store.getters.getUserState;
      return user == 'learner'
    }
  },
  methods: {
    async loadAll() {
      const courseId = this.$route.params.courseId
      const classId = this.$route.params.classId
      const sectionId = this.$route.params.sectionId
      const [sectionDetails] = await axios.all([
        axios.get(`http://localhost:5006/myCourses/${courseId}/${classId}/${sectionId}`),
      ]);

      this.sectionDetails = sectionDetails.data.data
      console.log(this.sectionDetails)
    
    },

    // classesListLink(courseId) {
    //   return this.$route.path + '/' + courseId;
    // },
    // toggleView(aClass){
    //   if (aClass.visible == true){
    //     aClass.visible = false
    //   }
    //   else {
    //     aClass.visible = true
    //   }
    //   console.log(aClass.visible)
    //   return aClass
    // }
  },
  created() {
    this.loadAll()
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style: none;
  margin: 0;
  padding: 0;
  
}
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto auto;
  grid-gap: 20px;
  /* background-color: #2196F3; */
  padding: 10px;
}

.grid-container > div {
  /* background-color: rgba(255, 255, 255, 0.8); */
  text-align: center;
  padding: 20px 0;
  /* font-size: 30px; */
}

.item1 {
  grid-area: 1 / 1 / span 1 / span 3;
}

.side {
    padding: 20px;
}

</style>
