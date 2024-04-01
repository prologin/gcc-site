function copyPostalAddress(btn_id) {

    const btn = document.getElementById(btn_id)
    const form_modal = btn.getAttribute("data-modal");

    const application_form_modal = document.getElementById(form_modal)
    const form = application_form_modal.querySelector("form");
    if (form === null) {
        return;
    }

    const street = form.querySelector("input[id=id_street_applicant]")
    const comp = form.querySelector("input[id=id_complement_applicant]")
    const city = form.querySelector("input[id=id_city_applicant]")
    const zip_code = form.querySelector("input[id=id_zip_code_applicant]")
    const country = form.querySelector("input[id=id_country_applicant]")

    form.querySelector("input[id=id_street_applicant_resp]").value=street.value
    form.querySelector("input[id=id_complement_applicant_resp]").value=comp.value
    form.querySelector("input[id=id_city_applicant_resp]").value=city.value
    form.querySelector("input[id=id_zip_code_applicant_resp]").value=zip_code.value
    form.querySelector("input[id=id_country_applicant_resp]").value=country.value
    return

}
