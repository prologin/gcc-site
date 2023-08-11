const INVALID_CLS = "is-invalid";
var next_click = document.querySelectorAll("#button-id-next");
var back_click = document.querySelectorAll("#button-id-back");
var main_form = document.querySelectorAll(".tab");
var progress_bar = document.querySelector(".progress .progress-bar");

let formnumber = 0;
const MAX_FORMNUMBER = 2;

next_click.forEach(function (next_page) {
    next_page.addEventListener("click", function () {
        if (!validateform()) {
            return false;
        }
        formnumber++;
        updateForm();
        updateProgressBar();
    });
});

back_click.forEach(function (back_page) {
    back_page.addEventListener("click", function () {
        formnumber--;
        updateForm();
        updateProgressBar();
    });
});

function updateProgressBar() {
    const percentage_progress = ((formnumber + 1) * 100) / MAX_FORMNUMBER;
    progress_bar.style.width = percentage_progress.toString() + "%";
    console.log(progress_bar);
}

function updateForm() {
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
    var fields = active_tab.querySelectorAll("input, select");
    fields.forEach(function (val) {
        val.classList.remove(INVALID_CLS);

        if (val.hasAttribute("required")) {
            if (val.type === "checkbox" || val.type === "radio") {
                if (!val.checked) {
                    validate = false;
                    val.classList.add(INVALID_CLS);
                }
            } else if (val.tagName === "select") {
                // Handle select elements (dropdowns)
                if (val.value === "") {
                    validate = false;
                    val.classList.add(INVALID_CLS);
                }
            } else if (val.value.length == 0) {
                validate = false;
                val.classList.add(INVALID_CLS);
            }
        }
    });
    return validate;
}

function initForm() {
    // The form activates the first tab containing errors.
    formnumber = 0;
    tabs = document.querySelectorAll(".tab");

    for ([i, tab] of tabs.entries()) {
        inputs = tab.querySelectorAll("input");
        for (input of inputs) {
            if (input.classList.contains(INVALID_CLS)) {
                formnumber = i;
                break;
            }
        }
    }
    updateForm();
    updateProgressBar();
}

initForm();
