import Home from "@/components/Home.vue";
import Movie from "@/components/Movie.vue";
import Header from "@/components/Header.vue";
import { createRouter,createWebHistory } from "vue-router";


const routes = [
    {
    path:'/',
    name:'Home',
    component:Home,
    },
    {path:'/today',name:'Today',component:Movie}
]

const router = createRouter({
    history:createWebHistory(),routes,
})

export default router