
function get_location() {

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        //x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    document.getElementById("location_lat").value = position.coords.latitude;
    document.getElementById("location_lon").value = position.coords.longitude;
}
