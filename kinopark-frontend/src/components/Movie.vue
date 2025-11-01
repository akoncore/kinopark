

<script>
export default{
  data(){
    return{
      movies:[
        {
          id:1,
          name:"Сыныптас",
          ganre:['драма','комедия'],
          pictures:"https://i.ibb.co/Y76XZ5BV/Whats-App-2025-10-13-15-11-25-c8f72724.webp",
          age:"18+"
        }
      ]
    }
  }
}
</script>

<template>
  <div class="left-router">
    <p><a href="/">Главная /</a></p>
    <p><a href=""> Сегодня в кино</a></p>
  </div>
  <div class="h1">
    <h1>Сегодня в кино</h1>
  </div>
  <div class="movies-list" v-for="movie in movies"
  :key="movie.id">
    <img :src="movie.pictures" alt="">
    <p>{{movie.name }}</p>
   
  </div>
</template>


<style>

.left-router{
  display: flex;
}
.movies-list{
  display: flex;

}
.movies-list img{
  width:17%;
}
</style>
