<template>
  <div class="hello">
    <section>
        <!-- <base-card id=courseSections>
            <li align='left'>
                <h2>{{courseInfo.courseName}}</h2>
                <br>
                {{courseInfo.courseDescription}}
            </li>
        </base-card> -->
        <div class="courseSections">
            <li align='left'>
                <h2>{{courseInfo.courseName}}</h2>
                <p style="font-style: italic;">{{courseInfo.courseDescription}}</p>
            </li>
        </div>

      <ul>
      <li v-for="section in listOfSections" :key="section.sectionId" align="left">

        <base-card>
            <h3>
                <router-link
                :to="{
                    name: `section1`, 
                    params: {courseId: section.courseId, classId: section.classId, sectionId: section.sectionId}}">
                
                {{section.sectionTitle}}
                
                </router-link>
            </h3>
            <p>~ {{section.estimatedTime}} mins</p>
        </base-card>

      </li>
      </ul>

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
      listOfSections: '',
      courseInfo: '',
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
      const [courseInfo, listOfSections] = await axios.all([
        axios.get(`http://localhost:5000/course/${courseId}`),
        axios.get(`http://localhost:5006/myCourses/${courseId}/${classId}`),
      ]);

      this.listOfSections = listOfSections.data.data
      this.courseInfo = courseInfo.data.data
      console.log(this.courseInfo.courseName)
      //console.log(this.listOfSections)
    
    },

    // sectionsListLink(sectionId) {
    //   return this.$route.path + '/' + sectionId;
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
li {
  list-style: none;
}

.courseSections {
    background-color: bisque;
    height: 130px;
    padding: 20px;
}

</style>
