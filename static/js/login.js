$(document).ready(function() {
    var input = document.getElementById("password");
    var text = document.getElementById("caps_warning");
    input.addEventListener("keyup", function(event) {

    if (event.getModifierState("CapsLock")) {
        text.style.display = "block";
    } else {
        text.style.display = "none"
    }
    });
});