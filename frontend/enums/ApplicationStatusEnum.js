const ApplicationStatusEnum = {
  ACCEPTED_AND_VALIDATED: 'ACCEPTED_AND_VALIDATED',
  ACCEPTED_WAITING_VALIDATION: 'ACCEPTED_WAITING_VALIDATION',
  REJECTED: 'REJECTED',
  COMPLETE: 'COMPLETE',
  ONGOING: 'ONGOING',
}

ApplicationStatusEnum.Mixin = {
  created () {
    this.ApplicationStatusEnum = ApplicationStatusEnum
  },
}

export default ApplicationStatusEnum
