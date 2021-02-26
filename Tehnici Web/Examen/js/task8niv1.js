let i=-1;
function myFunction()
{
    var images = document.getElementsByTagName('img');
    i=-i;
    if(i==-1){
        for (k = 0; k < images.length;k++ ) {
            images[k].style.visibility = "hidden";
        }
        
        document.getElementById("button").innerHTML = "Afiseaza imagini";}
    else{
        for (k = 0; k < images.length;k++ ) {
            images[k].style.visibility = "visible";
        }
        
        document.getElementById("button").innerHTML = "Ascunde imagini";}
}


//TASK 8 NIVEL 1