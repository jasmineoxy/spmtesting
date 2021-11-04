
<template>
  <div class="hello">
    <section>
      <base-card id="course-header">
          <router-link to='/'>Back to Courses</router-link>
        <li align='left'>
          <h2>{{courseInfo.courseName}} </h2><br>
          Course ID: {{courseInfo.courseId}}  <br>
          Description: {{courseInfo.courseDescription}} <br>
          Pre-Requisities: {{courseInfo.coursePrereq}} <br>
        </li>
      </base-card>
    </section>
      <section>
      <h3>Available Classes</h3>
        <table align='center' >
          <thead>
            <tr>
              <th>ID</th>
              <th>Start Date</th>
              <th>End Date</th>
              <th>Start Time</th>
              <th>End Time</th>
              <th>Day</th>
              <th>Current Class Size</th>
              <th>Max Class Size</th>
              <th>Trainer Name</th>
              <th></th>
            </tr>
          </thead>
            <classes-list-item v-for="eachClass in listOfClasses" :key="eachClass.id" align="left"
              :id="eachClass.classId"
              :startDate = "eachClass.classStartDate"
              :endDate = "eachClass.classEndDate"
              :classStartTime = "eachClass.classStartTime"
              :classEndTime = "eachClass.classEndTime"
              :classDay = "eachClass.classDay"
              :currentClassSize="eachClass.currentClassSize"
              :maxClassSize = "eachClass.maxClassSize"
              :trainerName = "eachClass.employeeName"
            ></classes-list-item>
        </table>
    <br>
    <br>
    <br>
    </section>
    
  </div>
</template>

<script>
import axios from 'axios'
import ClassesListItem from '../classes/ClassesListItem.vue'
export default {
  components: { ClassesListItem },
  data() {
    return {
      courseId: '',
      courseInfo: '',
      listOfClasses: '',
      enrollButtonStatus: 'Enroll Class', 

    }
  },
  methods: {
    async loadAll() {
      const courseId = this.$route.params.courseId
      console.log(courseId)
      const [courseInfo, listOfClasses] = await axios.all([
        axios.get(`http://localhost:5000/course/${courseId}`),
        axios.get(`http://localhost:5001/class/${courseId}`)
      ]);

      this.courseInfo = courseInfo.data.data
      this.listOfClasses = listOfClasses.data.data
      console.log(this.courseInfo)
      console.log(this.listOfClasses)
    }
  },
  created() {
    this.loadAll()
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#course-header {
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  margin: 0.5rem 0;
  background-color:black;
  color: white;
}

a {
  display: block;
  text-align: left;
  text-decoration: none;
  color:white;
  font-style: italic;
}
li {
  list-style: none;
}
</style>
