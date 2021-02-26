function varsta(){
    setInterval(executa,1000);
}

function executa(){
var x = document.getElementById("myText").value;
var luna;
var zi;

switch(x.substring(3,5)){
    case "01":
        luna = "January";
        break;
    case "02":
        luna = "February";
        break;
    case "03":
        luna = "March";
        break;
    case "04":
        luna = "April";
        break;
    case "05":
        luna = "May";
        break;
    case "06":
        luna = "June";
        break;
    case "07":
        luna = "July";
        break;
    case "08":
        luna = "August";
        break;
    case "09":
        luna = "September";
        break;
    case "10":
        luna = "Octomber";
        break;
    case "11":
        luna = "November";
        break;
    case "12":
        luna = "December";
}

switch(x.substring(0,2)){
    case "01":
        zi="1";
        break;
    case "02":
        zi="2";
        break;
    case "03":
        zi="3";
        break;
    case "04":
        zi="4";
        break;
    case "05":
        zi="5";
        break;
    case "06":
        zi="6";
        break;
    case "07":
        zi="7";
        break;
    case "08":
        zi="8";
        break;
    case "09":
        zi="9";
}
var DOB = luna + " " + zi + ", " + x.substring(6);

var millisecondsBetweenDOBAnd1970 = Date.parse(DOB);
var millisecondsBetweenNowAnd1970 = Date.now();
var ageInMilliseconds = millisecondsBetweenNowAnd1970-millisecondsBetweenDOBAnd1970;

  var milliseconds = ageInMilliseconds;

var years = Math.floor(milliseconds/(1000 * 60 * 60 * 24 * 30 * 12));
var months = Math.floor((milliseconds % (1000 * 60 * 60 * 24 * 30 * 12))/(1000 * 60 * 60 * 24 * 30));//NU IES PERFECT FORMULELE LA (LUNA, ZI)
var days= Math.floor((milliseconds % (1000 * 60 * 60 * 24 * 30)) / (1000 * 60 * 60 * 24));
var hours=Math.floor((milliseconds%(1000*60*60*24))/(1000*60*60));
var minutes=Math.floor((milliseconds%(1000*60*60))/(1000*60));
var seconds=Math.floor((milliseconds% (1000 * 60)) / 1000);
var message = years+ " ani " + months + " luni " + days + " zile " + hours + " ore " + minutes + " minute " + seconds + " secunde.";
document.getElementById('placeholder').innerHTML = message;

}

//TASK 1 NIVEL 2

/*function varsta() {
    var x = document.getElementById("myText").value;

    var now = new Date();
    var today = new Date(now.getYear(),now.getMonth(),now.getDate(), now.getHours(), now.getMinutes(), now.getSeconds());
    var yearNow = now.getYear();
    var monthNow = now.getMonth();
    var dateNow = now.getDate();
    var hourNow = now.getHours();
    var minNow = now.getMinutes();
    var secNow = now.getSeconds();

    var dob = new Date(x.substring(0,2),
        x.substring(3,5),
        x.substring(6,10));
    
    var dateDob = dob.getDate();
    var monthDob = dob.getMonth();
    var yearDob = dob.getYear();
    var hourDob = dob.getHours();
    var minDob = dob.getMinutes();
    var secDob = dob.getSeconds();
    
    console.log(secDob);
    console.log(hourDob);
    console.log(monthDob);

}*/