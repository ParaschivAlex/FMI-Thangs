function anime(){
    var ctx = document.getElementById("canvas").getContext("2d"),
        x = 245,//x si y de plecare
        y = 90,
        unghi = 0,
        velX = 0,
        velY = 0,
        raza = 3;

    var img = new Image;
    img.src="css/minge.jpg";//voiam o minge care se misca pe teren dar arata foarte urat

    function draw(){
        velX = Math.cos(unghi * Math.PI / 180) * raza;//formule matematice
        velY = Math.sin(unghi * Math.PI / 180) * raza;
        x += velX;
        y += velY;
        unghi+=2;//schimba pozitia
        //ctx.drawImage(img,x,y); nu merge poza peste poza
        ctx.fillStyle = "red";
        ctx.clearRect(0,0,520,358);//sterg afisarea de pe pozitia veche
        ctx.beginPath();//incepem sa punem o noua afisare
        ctx.rect(x, y, 10, 10);//afisam elementul
        ctx.closePath();
        ctx.fill();//umplem interiorul elementului
        setTimeout(function(){draw()}, 30);//functia apare la 30 milisecunde
        }
        draw();
    };
    
//TASK 1 NIVEL 3