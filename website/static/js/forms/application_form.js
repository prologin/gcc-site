import { MultiTabForm } from "./form.js"

/// Take the modal id in argument
/// Add an event listener to the modal to reset the form upon opening.
function setupApplicationFormModal(modal_id) {

    const application_form_modal = document.getElementById(modal_id);

    // If the user is not authenticated, form will be null.
    // We will have nothing to do
    const form = application_form_modal.querySelector("form");
    if (form === null) {
        return;
    }

    let multitabform = new MultiTabForm(form);

    // Add event effects on modal opening.
    // - Update event_id
    // - Reset form if id is changed
    application_form_modal.addEventListener("show.bs.modal", js_event => {

        // When the modal appears, find the id of the event related
        // to the button that was pressed.
        const button = js_event.relatedTarget;
        const event_id = button.getAttribute("data-bs-event-id");
        console.log("Opening application modal for event ID #" + event_id);

        // Get the existing elements
        let profil = document.querySelector("#div_id_profile");
        let label = document.querySelector(".form-label");
        let choice = document.querySelector("#id_profile");

        label.classList.add('col');

        // Create a new div for the column
        const columnDiv = document.createElement('div');
        columnDiv.className = 'row';

        // Append the label to the column div
        columnDiv.appendChild(label);

        // Create the "Créer un nouveau profil" button
        const createProfileButton = document.createElement('button');
        createProfileButton.innerText = 'Créer un nouveau profil !';
        createProfileButton.className = 'btn btn-block btn-light mb-2 col';

        // Add an onclick event to the button
        createProfileButton.onclick = function () {
            window.open(window.location.origin + "/profiles/create/", "_blank");
        };

        // Append the button to the column div
        columnDiv.appendChild(createProfileButton);

        // Replace the existing label with the new column div
        profil.insertBefore(columnDiv, choice);

        // Update the form's event id, and reset its content.
        // Check current form id. if new event ID, reset its content.
        let event_it_input = form.querySelector("#event-id-input");
        const previous_id = event_it_input.getAttribute("value");

        if (previous_id != null && previous_id != event_id) {
            multitabform.reset();
        }
        event_it_input.setAttribute("value", event_id);
    });
}

setupApplicationFormModal("application-form-modal");
