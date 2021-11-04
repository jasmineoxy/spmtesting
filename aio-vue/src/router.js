import { createRouter, createWebHistory } from 'vue-router';


import CoursesList from './components/pages/CoursesList.vue';
import ClassesList from './components/pages/ClassesList.vue';
import MyCoursesList from './components/pages/MyCoursesList.vue';
import SectionsList from './components/pages/SectionsList.vue';
import SectionView from './components/pages/SectionView.vue';



const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            redirect: '/courses'
        },
        {   path: '/courses',
            component: CoursesList
        },
        {
            path: '/courses/:courseId', 
            component: ClassesList,
            props: true,    
        },
        {   path: '/classes',
            component: ClassesList
        },
        {
            path: '/myCourses',
            component: MyCoursesList
        },
        {
            path: '/myCourses/:courseId/:classId', 
            component: SectionsList,
            props: true,    
        },
        {
            path: '/myCourses/:courseId/:classId/:sectionId', 
            component: SectionView,
            name: "section1",
            //props: true,    
        }
        
    ]
})

export default router;
