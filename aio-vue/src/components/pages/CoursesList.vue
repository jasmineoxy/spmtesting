<template>
  <div class="hello">
    <section>
      <!-- <ul id="title">
        <li><h3>All Courses</h3></li>
        <li>
          <router-link to="/myCourses">My Courses</router-link>
          </li>
      </ul> -->
      <!-- {{ listOfCourses }} -->
      <ul>
        <li v-for="course in listOfCourses" :key="course.courseName" align="left">
          <base-card>
            Course Name: {{course.courseName}} <br>
            Course ID: {{course.courseId}}  <br>
            Description: {{course.courseDescription}} <br>
            Pre-Requisities: {{course.coursePrereq}} <br>
            <br>
              <div v-if='isLearner'>
                <base-button link :to="classesListLink(course.courseId)">View Classes</base-button>
              </div>
              <div v-else>
                <span v-for="aClass in courseClassesDict[course.courseId]" :key="aClass">
                  <base-button @click="toggleView(aClass)">{{aClass.classId}}</base-button>
                  <class-assignment v-if="aClass.visible == true"></class-assignment>
                </span>
              </div>
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
import ClassAssignment from '../classes/ClassAssignment.vue'
export default {
  components: {
    ClassAssignment,
  },
  data() {
    return {
      listOfCourses: '',
      courseClassesResponse: '',
      courseClassesDict: {},
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
      const [courses, courseClasses] = await axios.all([
        axios.get('http://localhost:5000/course'),
        axios.get('http://localhost:5001/class/all'),
      ]);

      this.listOfCourses = courses.data.data.course
      this.courseClassesResponse = courseClasses.data.data
      // to toggle view of a class's assignment section
      for (let i = 0; i < this.courseClassesResponse.length; i++){
        this.courseClassesResponse[i].visible = false
      }
      for (let i = 0; i < this.listOfCourses.length; i++){
        this.getCourseClasses(this.listOfCourses[i].courseId)
      }
    },
    getCourseClasses(courseId) {
      var classesofCoursesDict = {}
      for (let i = 0; i < this.listOfCourses.length; i++){
        classesofCoursesDict[this.listOfCourses[i].courseId] = []
        // console.log(this.listOfCourses[i].courseId)
      }
      for (let i = 0; i < this.courseClassesResponse.length; i++){
        var classesOfCourse = this.courseClassesResponse[i]
        if (classesOfCourse.classId){
          classesofCoursesDict[classesOfCourse.courseId].push({"classId":classesOfCourse.classId, "visible":classesOfCourse.visible})
        }
      }
      this.courseClassesDict[courseId] = classesofCoursesDict[courseId] 
      return classesofCoursesDict[courseId]
    },
    classesListLink(courseId) {
      return this.$route.path + '/' + courseId;
    },
    toggleView(aClass){
      if (aClass.visible == true){
        aClass.visible = false
      }
      else {
        aClass.visible = true
      }
      console.log(aClass.visible)
      return aClass
    }
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

</style>
