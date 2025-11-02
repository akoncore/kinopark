import Home from "@/components/Home.vue";
import MovieList from "@/components/MovieList.vue";
import { createRouter,createWebHistory } from "vue-router";


const routes = [
    {
    path:'/',
    name:'Home',
    component:Home,
    },
    {path:'/today',name:'Today',component:MovieList}
]

const router = createRouter({
    history:createWebHistory(),routes,
})

export default router