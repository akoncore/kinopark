
<template>
      <div class="movie">
        <div class="movies-list" v-for="movie in movies2":key="movie.id">
          <div class="img-movie">
            <img :src="movie.pictures" alt="" @click="$emit('toggle-detail1')"/>
          </div>
          <div class="name-movie">
            <p>{{movie.name }}</p>
          </div>
          <div class="genre-age">
            <p>{{movie.ganre.join(', ')}}</p>
            <div class="sticker">
              <div class="in-sticker">
                <p class="age">{{movie.age}}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
</template>

<script>
export default {
    data(){
        return{
            movies2:[
                {
                id:5,
                name:"Ыстық ұя",
                ganre:['драма'],
                pictures:"https://i.ibb.co/84d7TmnB/100-70.webp",
                age:"14+"
                },
                {
                id:6,
                name:"Бақыт құшағында",
                ganre:['мюзикл', 'романтическая ','комедия'],
                pictures:"https://i.ibb.co/84GnqxJ8/Whats-App-2025-10-01-11-24-14-cca049fa.webp",
                age:"14+"
                },
                {
                id:7,
                name:"Болған оқиға",
                ganre:['драма','комедия'],
                pictures:"https://i.ibb.co/JF5BbMmB/image.png",
                age:"14+"
                },
                {
                id:8,
                name:"Трон Арес",
                ganre:['фантастика','боевик'],
                pictures:"https://i.ibb.co/QjpNSfKV/Whats-App-2025-10-06-11-00-10-e0a59b8b.webp",
                age:"18+"
                },
            ],
        }
    },
}
</script>

<style>
.movies-list{
  margin-bottom: 48px;
  display: flex;
  flex-direction:column;
  justify-content: center;
}
.name-movie{
  margin-top: 8px;
  font-size: 16px;
  font-weight: 700;
}
.genre-age{
  display: flex;
  margin-bottom: 16px;
  font-size: 13px;
  font-weight: 400;
}

.stciker{
  position: relative;
  min-width:24px;
  height: 24px;
  margin-left: 8px;
}
.in-sticker{
  position: absolute;
  width: 16px;
  height:16px;
  background:#ffd362;
  border-radius:2px;
  transform: rotate(45deg);
}
.age{
  transform: rotate(-45deg);
  font-size: .625rem;
  font-weight: 700;
}

.genre-age p{
  margin-top: 4px;
  width:75%;
}
</style>
