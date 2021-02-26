var str = "Campionatul Mondial de Fotbal sau Cupa Mondială FIFA (în engleză FIFA World Cup) ";
var cuvinte = str.split(" ");
var str2= "Brazilienii au construit cel mai mare stadion al lumii, Maracanã, fiind determinați să organizeze Campionatul Mondial în ediția 1950. Totuși, visul lor de a deveni campioni mondiali s-a năruit chiar pe acest stadion, Uruguay câștigând cel de-al doilea titlu în fața a 175.000 de oameni uluiți. Nu a fost singura surpriză a turneului deoarece, debutanta Anglia, a fost învinsă de Statele Unite cu 1-0.";
var cuvinte2= str2.split(" ");
//console.log(cuvinte);

var intervalID = setInterval(function(){
    if(cuvinte.length==0 && cuvinte2.length==0)
        return clearInterval(intervalID)
    else if(cuvinte.length!=0)
        document.getElementById("task2").innerHTML += " " + cuvinte.shift();
    else 
        document.getElementById("task2.1").innerHTML += " " + cuvinte2.shift();
},333);
/*
var intervalID = setInterval(function(){
    if(cuvinte.length==0 && cuvinte2.length==0 )
        return clearInterval(intervalID)
    else if(cuvinte.length!=0)
        document.getElementById("task2").innerHTML += " " + cuvinte.shift();
    if(cuvinte.length==0 && cuvinte2.length==0 )
        return clearInterval(intervalID)
    else if(cuvinte2.length!=0)
        document.getElementById("task2.1").innerHTML += " " + cuvinte2.shift();

},333);//AMANDOUA SIMULTAN*/

//TASK 2 NIVEL 2