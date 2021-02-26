/*var secunda = 0 
function incrementSeconds() {
    secunda +=1
    if(secunda>localStorage.alpha)
        document.getElementById('task4').innerHTML = Math.round(secunda/60)+":"+secunda%60;
    else
        {
            localStorage.alpha+=secunda;
            document.getElementById('task4').innerHTML = Math.round(secunda/60)+":"+secunda%60;
        }
}

var cancel = setInterval(incrementSeconds, 1000);*/

setInterval(() => {
    if (typeof(Storage) !== "undefined") {
        if (localStorage.ti) {
          localStorage.ti= Number(localStorage.ti)+1;
        } else {
          localStorage.ti = 0;
        }
        document.getElementById("task4").innerHTML = "Ai stat " + Math.round(localStorage.ti/60) + " minute si " + localStorage.ti%60 + " secunde pe aceasta pagina in total.";
    }
}, 1000);


//TASK 4 NIVEL 2