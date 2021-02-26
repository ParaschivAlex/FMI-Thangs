/*var wordsInPost = wordCount(document.getElementsByClassName(".highlight"))

function wordCount(words) {
	var count = 0
	for (var i = 0; i < words.length; i++) {
		count += words[i].textContent.split(' ').length

	}
	return count
}
//console.log(wordsInPost)
document.getElementById("footer").innerHTML = "Pe aceasta pagina sunt " + wordsInPost + " cuvinte";*/

var final_timp=new Date("Nov 21, 2022 16:00:00").getTime();//setez data de final
var update = setInterval(function() { //se schimba numaratoarea la fiecare secunda
var prezent=new Date().getTime();//setez data de inceput adica prezentul
var timp=final_timp - prezent;//fac diferenta dintre final si inceput
//console.log(timp)
var zile= Math.floor(timp / (1000 * 60 * 60 * 24));//formule luate de pe geeksforgeeks
zile=zile*24; //nu am nevoie de zile. trebuie sa transpun zilele in ore.
var ore=((Math.floor((timp%(1000*60*60*24))/(1000*60*60)))-1)+zile;//numarul de ore + zilele transformate in ore
var minute=Math.floor((timp%(1000*60*60))/(1000*60));
var secunde=Math.floor((timp% (1000 * 60)) / 1000);
document.getElementById("countdown").innerHTML="Mai sunt "+ore+" ore "+minute+ " minute "+secunde+" secunde pana incepe Campionatul Mondial!";//afisez
if(timp<0)//cand numaratoarea e gata
{
    clearInterval(update);//sterg
    document.getElementById("countdown").innerHTML="Asteptam urmatorul Campionat Mondial!";}//si afisez textul
},1000);


//TASK 6 NIVEL 1