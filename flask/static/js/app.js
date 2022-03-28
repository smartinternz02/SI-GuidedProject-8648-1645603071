

/////////////////////////////




$(function(){
// JavaScript source code
var submitButton = d3.select("#predict");
// Use D3 `.on` to attach a click handler for the submit button
//var submitButton = $("#predict");
var dict = {};
//var obj = {};


submitButton.on("click", function() {
    

        
    })
});

/*
submitButton.on("click", function () {
    d3.event.preventDefault();

    //var input1 = d3.select("#input1");
    var diagnosis = $('#input1').val().trim();
    //var diagnosis = input1.property("value");
    // var input2 = d3.select("#input2");
    var fev = $('#input2').val().trim();
   // var fev = input2.property("value");
    //  var input3 = d3.select("#input3");
    var age = $('#input3').val().trim();
  //  var age = input3.property("value");
    //  var input4 = d3.select("#input4");
    var performance = $('#input4').val().trim();
  //  var performance = input4.property("value");
    //  var input5 = d3.select("#input5");
    var tnm = $('#input5').val().trim();
  //  var tnm = input5.property("value");
       
    var pain = document.getElementsByName("pain");
    //var pain = $('pain');
    //console.log(pain)
    for (var i = 0; i < pain.length; i++) {
        if (pain[i].checked) {
            //var painvalue = pain[i].value;
            dict.pain = pain[i].value;
            break;
        };
    };
    var hae = document.getElementsByName("hae");
    for (var i = 0; i < hae.length; i++) {
        if (hae[i].checked) {
            var haevalue = hae[i].value;
            dict.hae = haevalue;
            break;
        };
    };
    var dys = document.getElementsByName("dys");
    for (var i = 0; i < dys.length; i++) {
        if (dys[i].checked) {
            var dysvalue = dys[i].value;
            dict.dys = dysvalue;
            break;
        };
    };
    var cough = document.getElementsByName("cough");
    for (var i = 0; i < cough.length; i++) {
        if (cough[i].checked) {
            var coughvalue = cough[i].value;
            dict.cough = coughvalue;
            break;
        };
    };
    var weakness = document.getElementsByName("weakness");
    for (var i = 0; i < weakness.length; i++) {
        if (weakness[i].checked) {
            var weaknessvalue = weakness[i].value;
            dict.weakness = weaknessvalue;
            break;
        };
    };
    var dm = document.getElementsByName("dm");
    for (var i = 0; i < dm.length; i++) {
        if (dm[i].checked) {
            var dmvalue = dm[i].value;
            dict.dm = dmvalue;
            break;
        };
    };
    var mi = document.getElementsByName("mi");
    for (var i = 0; i < mi.length; i++) {
        if (mi[i].checked) {
            var mivalue = mi[i].value;
            dict.mi = mivalue;
            break;
        };
    };
    var pad = document.getElementsByName("pad");
    for (var i = 0; i < pad.length; i++) {
        if (pad[i].checked) {
            var padvalue = pad[i].value;
            dict.pad = padvalue;
            break;
        };
    };
    var smoking = document.getElementsByName("smoking");
    for (var i = 0; i < smoking.length; i++) {
        if (smoking[i].checked) {
            var smokingvalue = smoking[i].value;
            dict.smoking = smokingvalue;
            break;
        };
    };
    var asthma = document.getElementsByName("asthma");
    for (var i = 0; i < asthma.length; i++) {
        if (asthma[i].checked) {
            var asthmavalue = asthma[i].value;
            dict.asthma = asthmavalue;
            break;
        };
    };

    dict.diagnosis = diagnosis
    dict.fev = fev
    dict.age = age
    dict.performance = performance
    dict.tnm = tnm
    dict.pain = pain
    dict.hae = hae
    dict.dys = dys
    dict.cough = cough
    dict.weakness = weakness 
    dict.dm = dm
    dict.mi = mi
    dict.pad = pad
    dict.smoking = smoking
    dict.asthma = asthma
    //console.log(dict);
    var list = [diagnosis, fev, age, performance, tnm, pain, hae, dys, cough, weakness, dm, mi, pad, smoking, asthma];

    //var arrStr = encodeURIComponent(JSON.stringify(dict));
    //$('#myLink').attr({ href: '/result?array=' + arrStr });

    //window.location.href = 'http://localhost:5000/result'+'#'+dict;

    //console.log(dict);

    $.get(`/result/${list}`, function (res) {
        if (res){
            window.open("result.html");
        }
    })
    






});
});

*/