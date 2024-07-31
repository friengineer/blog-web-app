function adjustSidebarHeight() {

  if (window.innerWidth > 900) {

    $(".socialContainer").css("height", $(document).height() - $(".socialContainer").offset().top);
  }

  $(document).scroll(function() {

    var scrollableArea = $(".socialContainer");
    var socials = $(".social");

    var offsetTop = - scrollableArea.offset().top + $(window).scrollTop();
    var offsetBottom = scrollableArea.offset().top - $(window).scrollTop() + scrollableArea.outerHeight() - socials.outerHeight()

    if (offsetBottom > 0 && offsetTop < 0) {

      socials.css({
        "top": 0
      });
    } else if (offsetBottom > 0 && offsetTop > 0) {

       socials.css({
        "top": offsetTop + "px"
      });
    } else {

      socials.offset({
        "top": $(window).scrollTop() + offsetBottom
      });
    }
  });
}

function resized() {

  $(".socialContainer").css("height", "");
  adjustSidebarHeight();
}

$(document).ready(adjustSidebarHeight);
