<script>

import Header from './Header.vue';
import MovieList from './MovieList.vue';
import Movie from './Movie.vue';
import MyCinema from './MyCinema.vue';
import SoonMovie from './SoonMovie.vue';
import UnderHeader from './UnderHeader.vue';


export default {
    components:{
        MovieList,Header,Movie,MyCinema,SoonMovie,UnderHeader
    },
    data(){
        return{
            hidden_movie:true,
            hidden_movie1:false
        }
    },
    methods:{
        SoonKino(){
            this.hidden_movie = false
            this.hidden_movie1 = true
        },
        TodayKino(){
            this.hidden_movie = true
            this.hidden_movie1 = false
        }
    }
}
</script>
<template>
    <div class="under-header">
        <UnderHeader/>
    </div>
    <div class="advertising-slider-wrapper">
    </div>
    <section class="section">
        <div class="section_content" v-show="hidden_movie">
            <Movie @soon-in-kino = "SoonKino"/>
        </div>
        <div class="section_content" v-show="hidden_movie1">
            <SoonMovie @soon-in-today = "TodayKino"/>
        </div>
        <div class="section_content">
            <MyCinema/>
        </div>
    </section>
</template>



<style>
.section{
    padding: 36px 0;
}
.section_content{
    max-width: 1240px;
    margin: 0 auto;
    padding: 36px 0;
    font-family: Open Sans, sans-serif;
}
.section_content1{
    max-width: 1240px;
    margin: 0 auto;
    padding: 36px 0;
    font-family: Open Sans, sans-serif;
}
.section_content2{
    max-width: 1240px;
    margin: 0 auto;
    padding: 36px 0;
    font-family: Open Sans, sans-serif;
}
.section_header{
    max-width: 1240px;
    margin: 0 auto;
    display: flex;
    font-family:Open Sans,sans-serif;

}

.header_text{
    font-size: 36px;
    font-weight: 700;
    margin-right: 20px;
    cursor: pointer;
}
.header_text2{
    color: rgb(140, 141, 147);
    font-weight: 400;
    font-size: 36px;
    border-left-color:rgb(195, 29, 40);
    border-left-style:solid;
    border-left-width:1.6px;
    padding-left:20px;
    cursor: pointer;
}
.ml-auto{
    margin-left: auto;
    font-size: 13px;
    font-weight: 400;
}
.under-header{
    background-color:#3e454b;
    align-items: center;
    height: 82px;
    color: rgb(14,14,14);
    display: flex;
    margin-top:64px;
}
.advertising-slider-wrapper{
    width:1440px;
    height:320px;
    margin: auto;
    background:url(https://i.ibb.co/vvzHj1sh/1440x320-kb-kopi.jpg);
}
</style>