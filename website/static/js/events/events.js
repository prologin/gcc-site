var next_click = document.querySelectorAll("#button-id-next");
console.log(next_click)
var back_click = document.querySelectorAll("#button-id-back");
var finish_click = document.querySelector("#finish-click");
var main_form = document.querySelectorAll(".tab");
let formnumber = 0;

next_click.forEach(function (next_page) {
    next_page.addEventListener("click", function () {
        if (!validateform()) {
            console.log("INVALID FORM")
            return false;
        }
        formnumber++;
        updateform();
        progress_forward();
    });
});

back_click.forEach(function (back_page) {
    back_page.addEventListener("click", function () {
        formnumber--;
        updateform();
    });
});

function updateform() {
    main_form.forEach(function (main_number) {
        main_number.classList.remove("active");
    });
    main_form[formnumber].classList.add("active");
}

/*
 * Check if the fields in the active tab are filled.
 */
function validateform() {
    validate = true;
    var active_tab = document.querySelector(".tab.active");
    var fields = active_tab.querySelectorAll("input");
    fields.forEach(function (val) {
        val.classList.remove("is-invalid");
        if (val.hasAttribute("required")) {
            if (val.type === "checkbox" && val.checked === false) {
                validate = false
                val.classList.add("is-invalid")
            }
            if (val.value.length == 0) {
                validate = false;
                val.classList.add("is-invalid");
            }
        }
    });
    return validate;
}
