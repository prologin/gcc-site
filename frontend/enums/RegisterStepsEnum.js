const RegisterStepsEnum = {
  ACCOUNT: 0,
  PERSONAL_INFORMATIONS: 1,
  COMPLETED: 2
}

RegisterStepsEnum.Mixin = {
  created () {
    this.RegisterStepsEnum = RegisterStepsEnum
  }
}

export default RegisterStepsEnum
