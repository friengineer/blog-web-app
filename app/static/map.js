var map = document.getElementById("map");

function getLocation() {

  if (navigator.geolocation) {

    navigator.geolocation.getCurrentPosition(showPosition);
  }
  else {

    map.innerHTML = "Geolocation is not supported by this browser.";
  }

  resized();
}

function showPosition(position) {

  var location = position.coords.latitude + "," + position.coords.longitude;
  var img_url = "http://maps.googleapis.com/maps/api/staticmap?center=" + location + "&zoom=14&size=600x450";
  document.getElementById("map").innerHTML = "<img src='" + img_url + "' alt='Map of your current location'>";
}

$(document).ready(getLocation);
