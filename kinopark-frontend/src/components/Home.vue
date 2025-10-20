<script>
import { reactive } from 'vue';
import Cinema from './Cinema.vue';

export default {
    data(){
        return{
            movie:"Фильмы",
            headercinema:"Кинотеатры",
            food:"Еда и напитки",
            mykinopark:"Мой Kinopark",

            todayInKino:"Сегодня в кино",
            pre_sales:"Предпродажи",
            soon:"Скоро",
            isMovieVisiable:false,

            ShowCatalog:false,
            selectCity:"Алматы",
            cities:["Алматы","Астана","Шымкент","Нарынқол"],
            select:false,

            ShowCinema:false,
            selectCinema:"Выберите кинотеатр",
            cinemas:["KinoPark","KinoPark","KinoPark"],
            select1:false,

            ShowMoviee:false,
            selectMovie:"Выберите фильм",
            movies:["Ыстық ұя","Әменгер","Таптым-ау сені","Сен"],
            selectedMovies:[],
            select2:false,

            
        }
    },
    methods:{
        toggleCityList(){
            this.ShowCatalog = !this.ShowCatalog
            this.ShowCinema = false,
            this.ShowMoviee = false
        },
        toggleCinemaList(){
            this.ShowCinema = !this.ShowCinema
            this.ShowCatalog=false
            this.ShowMoviee = false
        },
        toggleMovieList(){
            this.ShowMoviee = !this.ShowMoviee
            this.ShowCatalog=false,
            this.ShowCinema = false
        },
        selectCity(city){
            this.selectCity = city,
            this.ShowCatalog = false
        },
        selectCinema(cinema){
            this.selectCinema = cinema,
            this.ShowCinema = false
        },
        selectMovie(movie){
           if(this.selectedMovies.includes(movie)){
            this.selectedMovies = this.selectedMovies.filter(c=>c!== movie)
           }
           else{
            this.selectedMovies.push(movie)
           }
        },
        selectMovieLength(){
            if(this.selectedMovies.length == 0){
                return selectMovie
            }
        },
        checkedClose(city){
            this.selectCity = city,
            this.ShowCatalog = false
        },
        checkedCloseCinema(cinema){
            this.selectCinema=cinema,
            this.ShowCinema = false
        },
        checkedCloseMovie(movie){
            this.selectMovie = movie,
            this.ShowMoviee = false
        },
        ShowMovie(){
            this.isMovieVisiable = true
        },
        HidenMovie(){
            this.isMovieVisiable = false
        }
    }
}
</script>
<template>
    <header>
        <div class = "header_part">
            <div class="container">
                <img src="https://www.kinopark.kz/static/img/logos.svg" alt="Kinopaark_logo">
                <div class="header">
                    <ul class="header_menu">
                        <li class="header_menu_item" @mouseenter="ShowMovie" @mouseleave="HidenMovie">
                            <span>{{movie}}</span>
                            <div class="movieMenu"v-if="isMovieVisiable">
                                <div class="movieSchedule">
                                    <a href="">
                                        <button class="movieVariant" >{{todayInKino}}</button>
                                    </a>
                                </div>
                                <div class="movieSchedule">
                                    <a href="">
                                        <button class="movieVariant">{{pre_sales}}</button>
                                    </a>
                                </div>
                                <div class="movieSchedule">
                                    <a href="">
                                        <button class="movieVariant">{{soon}}</button>
                                    </a>
                                </div>
                            </div>
                        </li>
                        <li class="header_menu_item"><span>{{headercinema}}</span></li>
                        <li class="header_menu_item"><span>{{food}}</span></li>
                        <li class="header_menu_item"><span>{{mykinopark}}</span></li>
                    </ul>
                    <div class="lan">
                        <div class="language">Рус</div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <div class="under-header">
        <div class="in-container">
            <div class="search">
                <button type="button" class="button" @click="toggleCityList">
                    <img src="https://www.kinopark.kz/static/img/icons/map-marker-alt.svg" alt="map-market">
                    <div class="in-button">
                        <p class="insearch">{{ selectCity }}</p>
                    </div>
                    <img src="https://www.kinopark.kz/static/img/icons/caretDownBlack.svg" alt="Downblack" class="left">
                </button>
                <ul v-if="ShowCatalog" class="Showcities">
                    <li class="cities">
                        <button v-for="city in cities"
                            :key="city"
                            @click="selectCity(city)" class="selectCity">  
                        <label class="checkbox">
                            <input type="checkbox" v-model="select" @change="checkedClose(city)">
                        </label>
                        {{ city }}
                        </button>
                    </li>
                </ul>
            </div>
            <div class="search">
                <button type="button" class="button" @click="toggleCinemaList">
                    <img src="https://www.kinopark.kz/static/img/icons/cinema.svg" alt="5" class="cinema">
                    <div class="in-button">
                        <p class="insearch">{{selectCinema}}</p>
                    </div>
                    <img src="https://www.kinopark.kz/static/img/icons/caretDownBlack.svg" alt="Downblack" class="left1">
                </button>
                <ul v-if="ShowCinema" class="Showcities">
                    <li class="cities">
                        <button v-for="cinema in cinemas"
                            :key="cinema"
                            @click="selectCinema(cinema)" class="selectCity">  
                        <label class="checkbox">
                            <input type="checkbox" v-model="select1" @change="checkedCloseCinema(cinema)">
                        </label>
                        {{ cinema }}
                        </button>
                    </li>
                </ul>
            </div>
            <div class="search">
                <button type="button" class="button" @click="toggleMovieList">
                    <img src="https://www.kinopark.kz/static/img/icons/cinema.svg" alt="5">
                    <div class="in-button">
                        <p v-if="selectedMovies.length === 0" class="insearch">{{selectMovie}}</p>
                        <p v-else class="insearch">Выбрано фильмов ({{selectedMovies.length}})</p>
                    </div>
                    <img src="https://www.kinopark.kz/static/img/icons/caretDownBlack.svg" alt="Downblack" class="left2">
                </button>
                <ul v-if="ShowMoviee" class="Showcities">
                    <li class="cities">
                        <button v-for="(movie,i) in movies"
                            :key="i"
                            @click="selectMovie(i)" class="selectCity">  
                        <label class="checkbox">
                            <input type="checkbox" :value="movie" v-model="selectedMovies" @change="checkedCloseMovie">
                        </label>
                        {{ movie }}
                        </button>
                    </li>
                </ul>
            </div>
            <a href="">
                <div class="buyticket">Купить билеты</div>
            </a>
        </div>
    </div>
    <div class="advertising-slider-wrapper">

    </div>
</template>



<style>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body{
    margin: 0;
    padding: 0;
    font-family: Open Snas, sans-serif;
}
.header_part{
    background-color: #fff;
    position:static;
    top:0;
    width:100%;
    z-index:101;
    padding-left:0;
    padding-right: 0;
}
.container{
    height:64px;
    display: flex;
    justify-content: space-between;
    max-width: 1240px;
    margin-left: auto;
    margin-right: auto;
    align-items: center;

}
.container img{
    margin-top: 8px !important;
    display: inline-block;
    font-weight: 700;
    text-align: center;
    white-space: nowrap;
    width:120px;
}
.header{
    width:75%;
    justify-content: space-between;
    display: flex;
    align-items: center;
    height: 100%;
    position: static;
}
.header_menu{
    display: flex !important;
    height: 64px;
    padding: 0;
}
.header_menu_item{
    padding: 0 12px;
    cursor: pointer;
    margin-bottom: 2px;
}
.header ul{
    font-size: 1rem;
    font-weight: 500;
    margin-block-start: 1em;
    margin-block-end: 1em;
    padding-inline-start: 40px;
    unicode-bidi: isolate;
    list-style: none;
}
li {
    display: list-item;
    text-align: -webkit-match-parent;
    unicode-bidi: isolate;
}
li span{
    font-weight: 700;
    font-size: 1rem;
    color:#0e0e0e;
    line-height: 64px;
    padding-bottom: 21px;
    font-size: 16px;

}
li span:hover{
    color: #f96060;
    text-decoration:underline;
    text-underline-offset:25px;
}
.lan{
    margin-left: 3rem !important;
    align-items: center;
}
.language{
    font-weight: 700;
    font-size: 1rem;
}
.under-header{
    background-color:#3e454b;
    align-items: center;
    height: 82px;
    color: rgb(14,14,14);
    display: flex;
}
.in-container{
    align-items: center;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 1240px;
    margin-left: auto;
    margin-right: auto;
    padding-top: 20px;
    padding-bottom: 20px;
    gap: 20px;
}
.search{
    width:100%;
    display: block;
    box-sizing: border-box;
    flex-basis: 19%;
    position: relative;
    flex-grow: 0;
    flex-shrink: 0;
    font-size: 16px;
    font-weight: 700;
    align-items: center;
}

.button{
    white-space: nowrap;
    align-items: center;
    background-clip: border-box;
    background-position-x: 0;
    background-position-y: 50%;
    display: flex;
    cursor: pointer;
    font-weight: 700;
    padding: 12px;
    border-radius: 3px;
    font-size: 16px;
    flex: 30%;
    border: 0;
}
.button:hover{
    background-color: #aaa;
}
.button img{
    margin-right:8px;
    width:16px;
    height: 16px;
}
.in-button{
    flex: 1;
    margin-right: 40px;

    
}
.left{
    margin-left: auto;
    width:12px;
    height:12px;
    margin-left: 60px;
}
.left1{
    margin-left: 90px;
    width:12px;
    height: 12px;
}
.left2{
    margin-left: 127px;
}
.buyticket{
    font-size: .8125rem;
    font-weight:700;
    line-height: 18px;
    background-color: #c31d28;
    color: #fff;
    padding: 12px 28px;
}
a{
    text-decoration: none;
}
.Showcities{
    max-width:404px;
    overflow-y:auto;
    width:100%;
    position: absolute;
    background-color: #fff;
    border-radius:3px;
    margin-top: 5px;
    z-index: 6;
    font-weight: 500;
    font-size: 1rem;
    font-family: Open Sans,sans-serif;
    display: block;

}
.Showcities ul{
    padding: 0px;
}
.cities button{
    border-bottom: 1px solid #ddd;
}
.selectCity{
    display: block;
    padding:0px 8px;
    width:100%;
    padding: 8px 16px 8px 7px;
    text-align: left;
    align-items: center;
    border-left: 5px solid #c31d28;
    line-height: 28px;

}

input:checked+ .mark{
    background-color: #c31d28;
}
.checkbox{
    position: relative;
    padding-left: 15px;
    cursor: pointer;
    font-size: 20px;
    padding-right: 3px;
}
.box::after{
    color: #c31d28;
}
.movieMenu{
    position: absolute;
    margin-left: -48px;
    z-index:999;
    display: block;
    background-color: #fff;
    opacity:1;
    box-shadow: 0 2px 8px rgba(0,0,0,.32);
    border-radius: 3px;
    
}
.movieSchedule{
    width:220px;
    height:100%;
    padding:8px 16px;
    cursor: pointer;
}
.movieVariant{
    border-radius:0;
    border:0;
    display: inline-block;
    font-weight: 500;
    text-align: center;
    white-space: nowrap;
    padding: 8px 16px;
    cursor: pointer;
    font-size:1rem;
}
.advertising-slider-wrapper{
    width:1440px;
    height:320px;
    margin: auto;
    background:url(https://i.ibb.co/vvzHj1sh/1440x320-kb-kopi.jpg);
}
</style>