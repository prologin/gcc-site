const axios = require('axios');

window.addEventListener('load', () => {
    
    const length = document.querySelector("table").getAttribute("data-length")

    for (let index = 1; index <= length; index++) {
        const table_form = document.getElementById("status-form-"+index)
        table_form.addEventListener('change', () => {
            const table_head = document.getElementById("status-head-"+index)
            table_head.innerHTML = table_form.options[table_form.selectedIndex].text
        })
    }
})

function submitMultipleStatus() {
    const length = document.querySelector("table").getAttribute("data-length")

    for (let index = 1; index <= length; index++) {
        const table_form = document.getElementById("status-form-"+index)
        const table_head = document.getElementById("status-head-"+index)
        if (table_form.options[table_form.selectedIndex].getAttribute("data-initial") == null) {
            axios.post('/update-status-applicant', {
                year: document.getElementsByName("event-year")[0].value,
                event: document.getElementsByName("event-id")[0].value,
                status: table_form.options[table_form.selectedIndex].value
            })
        }
    }
}