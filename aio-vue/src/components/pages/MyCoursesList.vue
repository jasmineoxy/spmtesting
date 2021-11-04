<template>
    <div>
        <base-card class="course">
            <h2>{{myCoursesResponse.courseName}}</h2> <br>
            {{myCoursesResponse.courseDescription}}
            <!-- should create a nested component e.g courseSections.vue for the sections -->
            <base-button link :to="CourseSectionsLink">View Details</base-button>
        </base-card>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            myCoursesResponse: {},
        }
    },
    methods: {
        async loadAll() {
            const learnerId = this.$store.getters.getUserDetails.employeeId
            let [myCourses] = await axios.all([
                axios.get(`http://localhost:5004/learner/${learnerId}/coursesInProgress`),
            ])
            const courseId = myCourses.data.data
            const courseDetails = await  axios.get(`http://localhost:5000/course/${courseId}`)
             this.myCoursesResponse = courseDetails.data.data
        }
    },
    computed: {
        CourseSectionsLink() {
            return this.$route.path + '/' + 'X7846' + '/' + 'G1';
        }
    },
    created() {
        this.loadAll()
    }
}
</script>
<style>
.course {
    background-color: #fbceb1;
    text-align: left;
}
</style>