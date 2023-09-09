// Must be the same as events/forms.py:PHONE_REGEX
const PHONE_REGEX = /^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}$/;

const INVALID_CLASS = "is-invalid";
const TAB_ACTIVE_CLASS = "active";

/// Take a form HTML element and a positive integer as arguments.
/// Add display: none to all the disabled tabs.
function formDisplayNthTab(form, n) {
    form.querySelectorAll(".tab")
        .forEach((tab, index) => {
            if (index === n) {
                tab.classList.add(TAB_ACTIVE_CLASS);
            } else {
                tab.classList.remove(TAB_ACTIVE_CLASS);
            }
        });
}

/// Take the form HTML element as argument.
/// @return true if the current form tab is correctly filled.
function validateForm(form) {
    let valid = true;
    let active_tab = form.querySelector(".tab.active");
    let fields = active_tab.querySelectorAll("input, select");
    fields.forEach(function (val) {
        val.classList.remove(INVALID_CLASS);

        if (val.hasAttribute("required")) {
            if (val.type === "checkbox" || val.type === "radio") {
                if (!val.checked) {
                    valid = false;
                    val.classList.add(INVALID_CLASS);
                }
            } else if (val.tagName === "select") {
                // Handle select elements (dropdowns)
                if (val.value === "") {
                    valid = false;
                    val.classList.add(INVALID_CLASS);
                }
            } else if (val.value.length == 0) {
                valid = false;
                val.classList.add(INVALID_CLASS);
            } else if (val.type === "tel") {
                // Handle phone validation
                if (!PHONE_REGEX.test(val.value)) {
                    valid = false;
                    val.classList.add(INVALID_CLASS);
                }
            }
        }
    });
    return valid;
}

export {
    PHONE_REGEX,
    INVALID_CLASS,
    formDisplayNthTab,
    validateForm
};
