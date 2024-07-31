function resizedContact() {

  $(".leftHome").css("margin-right", 0);

  if (window.innerWidth > 900) {

    $(".leftHome").css("margin-right", 20);
  }

  resized();
}

$(document).ready(resizedContact);

// resize content window since it's limited by the size of the mainContent element for the map text and image
