const QuestionsTypeEnum = {
  TITLE: 'TITLE',
  TEXT: 'TEXT',
  LONG_TEXT: 'LONG_TEXT',
  SINGLE_CHOICE: 'SINGLE_CHOICE',
  MULTIPLE_CHOICES: 'MULTIPLE_CHOICES'
}

QuestionsTypeEnum.Mixin = {
  created () {
    this.QuestionsTypeEnum = QuestionsTypeEnum
  }
}

export default QuestionsTypeEnum
