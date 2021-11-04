<template>
    <div>
    <h3>Learners to Assign:</h3>
     <table align='center'>
         <thead>
             <tr>
                 <th>Learner ID</th>
                 <th>Learner Name</th>
                 <th>Pass Pre-Req?</th>
                 <th></th>
             </tr>
         </thead>
         <class-assignment-item v-for="eachLearnerId in LearnersCanBeAssigned" :key="eachLearnerId"
            :eachLearnerId="eachLearnerId"
         ></class-assignment-item>
     </table>
    <!-- <p v-for="each in Learners" :key="each.employeeId">{{each.employeeId}}</p> -->
    <hr>
    <h3>Learners Enrolled:</h3>
    </div>
</template>
<script>
import axios from 'axios'
import ClassAssignmentItem from '../classes/ClassAssignmentItem.vue'


export default {
  components: { ClassAssignmentItem },
    data() {
        return {
            Learners: '',
            LearnersByCompletedCourse: '',
            // LearnersListByCompletedCourse: [],
            // LearnersListByInProgressCourse: [],
            LearnersCanBeAssigned: [],
            assignLearnerStatus: 'Assign',
            wantToAssign: false,

        }
    },
    methods: {
        async loadLearners() {
            //how to link from button
            // const classId = this.$route.params.classId
            // const courseId = this.$route.params.courseId
            // console.log('this is classId:',classId)
            // console.log('this is courseId:',courseId)

            // const courseId = 'X7846'
            //#Function 3 Get course Pre-Req
            // @app.route("/course/pre_req/<string:courseId>")
            // const courseId

            //
            const Learners = await axios.get('http://localhost:5004/learner');
            this.Learners = Learners.data.data
            console.log('allLearners:',this.Learners)

            for (let i=0; i<Learners.data.data.length; i++){
                var each = Learners.data.data[i]
                console.log(each.employeeId,each.learnerCoursesCompleted,each.learnerCoursesInProgress)

                //need change X7846
                //add if not in classlist already or other classlist of the same course
                //add pre-req
                //string->list->check in list
                if (each.learnerCoursesCompleted != 'X7846' 
                    && each.learnerCoursesInProgress != 'X7846'
                    || each.learnerCoursesCompleted == '' 
                    || each.learnerCoursesInProgress == ''){
                    this.LearnersCanBeAssigned.push([each.employeeId,each.employeeName])
                    console.log('inside != function')
                }

                console.log('list of learners to assign for course 46', this.LearnersCanBeAssigned)
               
            }

            //break
            // const Employee = await axios.get('http://localhost:5002/Engineers/${em}');
            // this.Learners = Learners.data.data


            // console.log('learnerlist:', this.LearnersListByCompletedCourse)

            // //NOTE:need to change to dynamic courseId
            // const LearnersByCompletedCourse = await axios.get('http://localhost:5004/learner/coursesCompleted/X7846');
            // const LearnersByInProgressCourse = await axios.get('http://localhost:5004/learner/coursesInProgress/X7846');
            
            // for (let i=0; i<LearnersByCompletedCourse.data.data.length; i++){
            //     this.LearnersListByCompletedCourse.push(LearnersByCompletedCourse.data.data[i].employeeId)
            // }
            // console.log('learnerlist:', this.LearnersListByCompletedCourse)

            // for (let i=0; i<LearnersByInProgressCourse.data.data.length; i++){
            //     this.LearnersListByInProgressCourse.push(LearnersByInProgressCourse.data.data[i].employeeId)
            // }
            // console.log('learnerlist:', this.LearnersListByInProgressCourse)

            //break
            //given course=X7846
            //for each learner in all learner, 
            //if each learner is not in list-completed
            //and if each learner is not in list-inprogress
            //push to the list-canassign

        },
        assignLearner() {
            this.wantToAssign = ! this.wantToAssign
            if (this.wantToAssign){
                return this.assignLearnerStatus = "Assigned"
            }
            console.log('ok')
            return this.assignLearnerStatus = "Assign"
            }
    },
    mounted() {
        this.loadLearners()
    }
}

// export default {
//     data() {
//         return {
//             juniorEngineers: ''
//         }
//     },
//     methods: {
//         async loadJuniorEngineers() {
//             const juniorEngineers = await axios.get('http://localhost:5002/juniorEngineers')
//             this.juniorEngineers = juniorEngineers.data.data.juniorEngineer
//         }
//     },
//     mounted() {
//         this.loadJuniorEngineers()
//     }
// }
</script>