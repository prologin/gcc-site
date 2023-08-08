document.addEventListener("DOMContentLoaded", function() {
  // Hide navbar initially
  if (document.querySelector(".home-banner") != undefined) {
    var navbar = document.querySelector(".navbar-brand");
    navbar.style.transition = "opacity 0.5s ease";

    if (window.pageYOffset < 400) {
      navbar.style.opacity = "0"
    }
    // Fade in/out navbar on scroll
    window.addEventListener("scroll", function() {
      if (window.pageYOffset > 400) {
        navbar.style.opacity = "1";

      } else {
        navbar.style.opacity = "0";
      }
    });
  } else {
    var navbar = document.querySelector(".navbar-brand");
    navbar.style.opacity = "1";
  }
});
