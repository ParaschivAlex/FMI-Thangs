function myFunction()
{

	var question1 = document.quiz.question1.value;
	var question2 = document.quiz.question2.value;
    var question3 = document.quiz.question3.value;
    var question4 = document.quiz.question4.value;
    var question5 = document.quiz.question5.value;
    var question6 = document.quiz.question6.value;
	var correct = 0;


	if (question1 == "Ronaldo Nazário") {
		correct++;
}
	if (question2 == "18") {
		correct++;
}	
	if (question3 == "Franta") {
		correct++;
    }
    
    if (question4 == "Da") {
		correct++;
    }
    if (question5 == "Argentina") {
		correct++;
    }
    if (question6 == "Corect") {
		correct++;
	}
	
	var pictures = ["img/win.gif", "img/meh.gif", "img/lose.gif"];
	var messages = ["Bravo!", "Mmm..Mediu!", "Poti mai bine."];
	var score;

	if (correct <=1) {
		score = 2;
	}

	if (correct > 1 && correct < 3) {
		score = 1;
	}

	if (correct >= 3) {
		score = 0;
	}
    
	document.getElementById("after_submit").style.visibility = "visible";
    if (typeof(Storage) !== "undefined") {
        if (localStorage.count) {
          localStorage.count = Number(localStorage.count)+1;
        } else {
          localStorage.count = 1;
        }
        document.getElementById("message").innerHTML = messages[score] + " Ai facut testul de " + localStorage.count + " ori";

    }
    document.getElementById("number_correct").innerHTML = "Ai raspuns la " + correct + " intrebari corect.";
	document.getElementById("picture").src = pictures[score];
    
    
}

function timeout()
{
    setTimeout(function(){ alert("RONALDO MARCHEAZA!"); }, 500);
}

function interval() 
{
    setInterval(function(){ alert("REPLAY LA INFINIT"); }, 4000);
}


