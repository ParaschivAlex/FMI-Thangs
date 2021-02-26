function salut() {
    let x = document.getElementsByTagName("title")[0].text;//iau titlul ca sa il reinitializez mai tarziu
    let sign = prompt("Cum te numesti?");
    document.title = "Salut, " + sign + "!";
    //alert(x);
    setTimeout(function(){ document.title = x; }, 2000);
}
//TASK 16 NIVEL 1