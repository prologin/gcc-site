import { MultiTabForm } from "./form.js"

/// Take the modal id in argument
/// Add an event listener to the modal to reset the form upon opening.
/// Take the form HTML element as argument
function setupProfileCreationFormModal(form)  {
    let multitabform = new MultiTabForm(form);
}

setupProfileCreationFormModal(document.querySelector("form"));
