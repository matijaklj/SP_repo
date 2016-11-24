document.addEventListener("DOMContentLoaded", function() {
	document.getElementById("check").addEventListener("click", checkTemperature);
	document.getElementById("wsCheck").addEventListener("click", checkWsTemperature);
});
window.addEventListener("beforeunload", checkLeave);

function checkLeave(e) {
  e.returnValue = "Warning!";
  return "Warning!";
}

function checkTemperature(event) {
	filename=document.getElementById("datum").value;
	
	var oReq = new XMLHttpRequest();
//	oReq.addEventListener("load", measureHandler);
	oReq.addEventListener("load", measureHandlerJson);
//	oReq.open("GET", filename+".txt");
	oReq.open("GET", filename+".json");
	oReq.responseType = "text";
	oReq.send();
	
	event.preventDefault();
}

function measureHandler(event) {
	document.getElementById("result").innerHTML = this.responseText;
}

function measureHandlerJson(event) {
	measures = JSON.parse(this.responseText);
	document.getElementById("temperature").innerHTML = measures["temperature"];
	document.getElementById("humidity").innerHTML = measures["humidity"];
}

var wsHost = "193.2.76.41:1234"; // vedi streznik v LUSY
function checkWsTemperature(event) {
	var tempSocket = new WebSocket("ws://"+wsHost);
	tempSocket.binaryType = 'arraybuffer';
	tempSocket.addEventListener("message", wsMeasureHandler);
	tempSocket.addEventListener("error", wsMeasureError);
}

function wsMeasureHandler(event) {
	measures = JSON.parse(event.data);
	document.getElementById("wsTemperature").innerHTML = measures["temperature"];
	document.getElementById("wsHumidity").innerHTML = measures["humidity"];
}

function wsMeasureError(event) {
	document.getElementById("wsResult").innerHTML = "ERROR: Cannot connect to websocket server "+wsHost;
}