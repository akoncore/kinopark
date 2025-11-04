
<script>

</script>

<template>
<div class="footer">
    <div class="footer-container">
        <div class="logo-kinopark">
                <div class="container-logo">
                    <div class="logo-in">
                        <img src="../assets/img/kinopark.svg" alt="kinopark">
                        <img src="../assets/img/kinoplexx.svg" alt="kinoplexx">
                    </div>
                    <p class="rgb1701">Скачайте приложение Kinopark</p>
                    <div class="install">
                        <img src="https://www.kinopark.kz/static/img/icons/appStore.svg" alt="">
                        <img src="https://www.kinopark.kz/static/img/icons/googlePlay.svg" alt="">
                    </div>
                </div>
                <div class="container-schulde">
                    <p class="rgb170">Расписание</p>
                    <div class="schulde">
                        <p>Сегодня в кино</p>
                        <p>Скоро на экранах</p>
                        <p>Эксклюзив</p>
                    </div>
                    <p class="rgb170">Технологии</p>
                    <div class="technology">
                        <p>IMAX</p>
                        <p>Dolby Atmos</p>
                        <p>Laser</p>
                    </div>
                </div>
                <div class="Company">
                    <p class="rgb1702">О компании</p>
                    <div class="companies">
                        <p>О нас</p>
                        <p>Кинотеатры</p>
                        <p>Для бизнеса</p>
                        <p>Партнеры</p>
                        <p>Новости</p>
                        <p>Контакты</p>
                    </div>
                </div>
                <div class="connect">
                    <div class="images">
                        
                    </div>
                </div>
        </div>
    </div>
    <div class="footer-line"></div>
    <div class="footer-end">
        <p class="rgb170">© Kinopark Theatres.Все права защищены</p>
        <p>Пользовательское соглашение</p>
    </div>
</div>
</template>

<style>
.footer{
    margin-top:100px;
    font-family: Open Sans,sans-serif;
}
.footer-container{
    max-width: 1240px;
    margin: 0 auto ;
}
.logo-kinopark{
    display: flex;
    justify-content: space-between;
    width:1240px;
    padding: 56px 0 ;
}
.container-logo{
    display: inline-block;
}
.rgb1701{
    margin-bottom: 16px;
    color: rgb(170,170,170);
}
.logo-in{
    display: flex;
    flex-direction: column;
}
.logo-in img{
    margin-bottom: 32px;
}
.container-schulde{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.schulde{
    margin:6px 0; 
}
.schulde p{
    font-size: 16px;
    padding: 4px 0;
    font-weight: 500;
    line-height: 28px;
}
.rgb170{
    color: rgb(170,170,170);
}
.technology{
    margin:6px 0;
    display: flex;
    justify-content: space-between;
    gap:6px;
}
.technology p{
    font-size: 16px;
    font-weight: 500;
    line-height: 28px;
}
.install{
    display: flex;
    justify-content: space-between;
    margin: 0 8px;
}
.footer-line{
    border:1px solid #4e4e4e;
}
.Company{
    
}
.rgb1702{
    color:rgb(170,170,170);
    margin-bottom:8px;
}
.companies{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.companies p{
    font-size: 16px;
    font-weight: 500;
    padding:8px 0;
}
.footer-end{
    max-width:1240px;
    margin:0 auto;
    display: flex;
    justify-content: space-between;
    padding: 16px 0;
}
</style>
