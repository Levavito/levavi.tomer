// -----console js exsample----//
var txt = "abcdefg";
var txt2 = "come visit microsoft"
var txt3 = txt2.replace("microsoft","bgu");
var text_length = txt.length;
var txtSlice = txt.slice(0,3);
console.log(text_length);
console.log(txtSlice);
console.log(txt3);


// -----Method----//
var person = {
    FirstName : "tomer",
    LastName : "levavi",
    FullName : function(){
        var Full = this.FirstName + " " + this.LastName;
        return Full;
    }
}
console.log(person.FullName());

const d = new Date();
console.log(d);
var h = d.getHours();
console.log(h);

if(h<12){
    greeting = "good morning";
}else if(h<17){
    greeting = "good afternoon";
} else{
    greeting = "good evening";
}; console.log(greeting);

function greet(){
    document.getElementById("P").innerHTML=greeting;
};

var cars = ["BMW","Ferari","Lamborgini"];
for (var i=0; i<cars.length; i++){
    console.log(cars[i]);
}

var imgsarr = [
    "pics/cart_glass.jpg",
    "pics/EX2_pic.jpg",
    "pics/cart_glass.jpg",
    "pics/EX2_pic.jpg",
    "pics/cart_glass.jpg",
    "pics/EX2_pic.jpg",
    "pics/cart_glass.jpg",
    "pics/EX2_pic.jpg"
];

var i=0; 
function play(){
        setTimeout(function(){
            document.getElementById("img").src= imgsarr[i] ;  
            i++;
            if(i<imgsarr.length){
                play()
            }else{
                i=0;
            };
        }, 500);
}



// -----------api---------//
function myFunction() {
    const inpObj = document.getElementById("id1");
    if (!inpObj.checkValidity()) {
         document.getElementById("demo").innerHTML = inpObj.validationMessage;
    } else {
        document.getElementById("demo").innerHTML = "Input OK";
    }
}


// -----------geolocation---------//
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}
function showPosition(position) {
    document.getElementById("demo1").innerHTML = "Latitude: " + position.coords.latitude +
     "<br>Longitude: " + position.coords.longitude;
}

// -------------Storage-------------//
localStorage.setItem("name", "John Doe");
localStorage.getItem("name");
