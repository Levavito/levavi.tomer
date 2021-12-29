// wellcome haeder//

const d = new Date();
console.log(d);
var h = d.getHours();

if(h<12){
    greeting = "good morning";
}else if(h<17){
    greeting = "good afternoon";
} else{
    greeting = "good evening";
}; console.log(greeting);

function greet(){
    document.getElementById("wellcome").innerHTML=greeting;
};

// img cat//
function catpic(){    
    document.getElementById("item3").style.backgroundImage = "url('/static/EX2_pic.jpg')";
    document.getElementById("buttoncat").style.display = "none"
};


// -----------api iq---------//
function myFunction() {
    const inpObj = document.getElementById("iq");
    if (inpObj.value != 20) {
         document.getElementById("demo").innerHTML = "wrong input   ";
    } else {
        document.getElementById("demo").innerHTML = "Input OK";
    }
}

function getUrlParameter(sParam)
{
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++)
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam)
        {
            return sParameterName[1];
        }
    }
}

function change_acording_to_querry(){
    var header = getUrlParameter('p1');
    document.getElementById('userAction').innerHTML = header;
};