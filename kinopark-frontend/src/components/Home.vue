
<template>
    <header>
        <div class = "header_part">
            <div class="container">
                <img src="https://www.kinopark.kz/static/img/logos.svg" alt="Kinopaark_logo">
                <div class="header">
                    <ul class="header_menu">
                        <li class="header_menu_item"><span>Фильмы</span></li>
                        <li class="header_menu_item"><span>Кинотеатры</span></li>
                        <li class="header_menu_item"><span>Еда и напитки</span></li>
                        <li class="header_menu_item"><span>Мой Kinopark</span></li>
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
                <button type="button" class="button">
                    <img src="https://www.kinopark.kz/static/img/icons/map-marker-alt.svg" alt="map-market">
                    <div class="in-button">
                        <p class="insearch">Алматы</p>
                    </div>
                    <img src="https://www.kinopark.kz/static/img/icons/caretDownBlack.svg" alt="Downblack" class="left">
                </button>
            </div>
            <div class="search">
                <button type="button" class="button">
                    <img src="https://www.kinopark.kz/static/img/icons/cinema.svg" alt="5" class="cinema">
                    <div class="in-button">
                        <p class="insearch">Выберите кинотеатр</p>
                    </div>
                    <img src="https://www.kinopark.kz/static/img/icons/caretDownBlack.svg" alt="Downblack" class="left1">
                </button>
            </div>
            <div class="search">
                <button type="button" class="button">
                    <img src="https://www.kinopark.kz/static/img/icons/cinema.svg" alt="5">
                    <div class="in-button">
                        <p class="insearch">Выберите фильм</p>
                    </div>
                    <img src="https://www.kinopark.kz/static/img/icons/caretDownBlack.svg" alt="Downblack" class="left2">
                </button>
            </div>
            <a href="">
                <div class="buyticket">Купить билеты</div>
            </a>
        </div>
    </div>
</template>

<script>

</script>

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
ul{
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
    margin-left: 45px;
}
.left1{
    margin-left: 90px;
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
</style>