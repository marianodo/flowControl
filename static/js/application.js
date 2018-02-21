$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server
    socket.on('tapFlow', function(msg) {
       document.getElementById("tap1").innerHTML =msg["taps"][1].liters;
       document.getElementById("tap2").innerHTML =msg["taps"][2].liters;
       document.getElementById("tap3").innerHTML =msg["taps"][3].liters;
       document.getElementById("tap4").innerHTML =msg["taps"][4].liters;
       document.getElementById("tap5").innerHTML =msg["taps"][5].liters;
    });

});