const ScheduleTypeEnum = {
  WEEK: 'WEEK',
  WEEKEND: 'WEEKEND',
  OTHER: 'OTHER',
}

ScheduleTypeEnum.Mixin = {
  created () {
    this.ScheduleTypeEnum = ScheduleTypeEnum
  }
};

export default ScheduleTypeEnum
