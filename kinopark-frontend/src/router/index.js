import Home from "@/components/Home.vue";
import MovieList from "@/components/MovieList.vue";
import UnderHeader from "@/components/UnderHeader.vue";
import { createRouter,createWebHistory } from "vue-router";


const routes = [
    {
    path:'/',
    name:'Home',
    component:Home,
    },
    {path:'/today',name:'Today',component:MovieList},
    {path:'/underheader', name:'UnderHeader',component:UnderHeader},
    
]

const router = createRouter({
    history:createWebHistory(),routes,
})

export default router