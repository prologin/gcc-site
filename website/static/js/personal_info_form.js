let toActiveOnClickPersonalInfo = document.getElementsByClassName('on_change_active_personal_info');
let formPersonalInfo = document.getElementsByClassName('personal_info_form')[0].getElementsByClassName("textinput");

let modifyPersonalInfo = true;

function activeFormPersonalInfo() {
  modifyPersonalInfo = !modifyPersonalInfo;
  for (let i = 0; i < toActiveOnClickPersonalInfo.length; i++) {
    toActiveOnClickPersonalInfo[i].style.display = modifyPersonalInfo ? 'block' : 'none';
  };

  document.getElementById('submit-id-submit-personal_info').style.display = modifyPersonalInfo ? 'block' : 'none';
  document.getElementById('active_personal_info').style.display = modifyPersonalInfo ? 'none' : 'block';

  for (let i = 0; i < formPersonalInfo.length; i++) {
    if (modifyPersonalInfo)
    formPersonalInfo[i].removeAttribute('disabled');
    else
    formPersonalInfo[i].setAttribute('disabled', '');
  }
}

let toActiveOnClickEmail= document.getElementsByClassName('on_change_active_email');
let formEmail = document.getElementsByClassName('email_form')[0].getElementsByClassName("emailinput");

let modifyEmail = true;

function activeFormEmail() {
  modifyEmail = !modifyEmail;
  for (let i = 0; i < toActiveOnClickEmail.length; i++) {
    toActiveOnClickEmail[i].style.display = modifyEmail ? 'block' : 'none';
  };

  document.getElementById('submit-id-submit-email').style.display = modifyEmail ? 'block' : 'none';
  document.getElementById('active_email').style.display = modifyEmail ? 'none' : 'block';

  for (let i = 0; i < formEmail.length; i++) {
    if (modifyEmail)
      formEmail[i].removeAttribute('disabled');
    else
      formEmail[i].setAttribute('disabled', '');
  }
}

activeFormPersonalInfo();
activeFormEmail();
