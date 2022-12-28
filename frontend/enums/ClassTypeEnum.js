// This is not translated since translating would make
// code less readable
// Numbered class name are prepended by an underscore because it's not a correct symbol otherwise
const ClassTypeEnum = {
  _6_EME: 0,
  _5_EME: 1,
  _4_EME: 2,
  _3_EME: 3,
  _2_NDE: 4,
  _1_ERE: 5,
  TERMINALE: 6,
  AUTRE: 7
};

ClassTypeEnum.Mixin = {
  created () {
    this.ClassTypeEnum = ClassTypeEnum
  },
}

export default ClassTypeEnum
