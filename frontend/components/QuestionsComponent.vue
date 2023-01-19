<template>
  <b-container fluid>
    <b-col>
      <div v-for="(question, i) in questions" :key="i">
        <b-row>
          <h2 v-if="question.type == QuestionsTypeEnum.TITLE">
            {{ question.text }}
          </h2>
        </b-row>

        <b-row>
          <h3 v-if="question.type != QuestionsTypeEnum.TITLE">
            {{ question.text }}
          </h3>
          <b-form-input
            v-if="question.type == QuestionsTypeEnum.TEXT"
            :id="'input-question' + i"
            v-model="answers[i]"
            :placeholder="question.placeholder"
            :required="question.mandatory"
          />
          <b-form-textarea
            v-if="question.type == QuestionsTypeEnum.LONG_TEXT"
            :id="'input-question' + i"
            v-model="answers[i]"
            :placeholder="question.placeholder"
            :required="question.mandatory"
          />
        </b-row>

        <b-row>
          <b-form-group
            v-if="question.type == QuestionsTypeEnum.SINGLE_CHOICE"
            v-slot="{ ariaDescribedBy }"
          >
            <b-form-radio-group
              :id="'input-question' + i"
              v-model="answers[i]"
              :required="question.mandatory"
              :options="question.possible_answers"
              :aria-describedby="ariaDescribedBy"
            />
          </b-form-group>
        </b-row>

        <b-row>
          <b-form-group
            v-if="question.type == QuestionsTypeEnum.MULTIPLE_CHOICES"
            v-slot="{ ariaDescribedBy }"
          >
            <b-form-checkbox-group
              :id="'input-question' + i"
              v-model="answers[i]"
              :options="question.possible_answers"
              :required="question.mandatory"
              :aria-describedby="ariaDescribedBy"
              :name="question.text"
            />
          </b-form-group>
        </b-row>
      </div>
    </b-col>
  </b-container>
</template>

<script>
import Vue from 'vue';
import QuestionsTypeEnum from '@/enums/QuestionsTypeEnum.js';

export default Vue.extend({
  name: 'QuestionsComponent',
  mixins: [QuestionsTypeEnum.Mixin],
  data: () => {
    return {
      /* TODO: adapt answer for API */
      questions: [
        {
          id: 2,
          order: 2,
          text: "This is a text",
          type: "TITLE",
          placeholder: "second placeholder",
          mandatory: true,
          possible_answers: [],
        },
        {
          id: 1,
          order: 1,
          text: "This is another text",
          type: "TEXT",
          placeholder: "first placeholder",
          mandatory: false,
          possible_answers: [],
        },
        {
          id: 3,
          order: 3,
          text: "This is yet another text",
          type: "LONG_TEXT",
          placeholder: "3 placeholder",
          mandatory: true,
          possible_answers: [],
        },
        {
          id: 4,
          order: 4,
          text: "This is yet yet yet another text",
          type: "SINGLE_CHOICE",
          placeholder: "4 placeholder",
          mandatory: true,
          possible_answers: [
            { value: 1, text: "first" },
            { value: 2, text: "second" },
          ],
        },
        {
          id: 5,
          order: 5,
          text: "This is yet yet another text",
          type: "MULTIPLE_CHOICES",
          placeholder: "5 placeholder",
          mandatory: true,
          possible_answers: [
            { value: 1, text: "first" },
            { value: 2, text: "second" },
          ],
        }
      ],
      answers: [],
    };
  },
  created() {
    /* Sort questions to have them in order of appearance in the questions array */
    this.questions.sort(function (a, b) {
      return a.order - b.order;
    })

    /* Creates an equally sized array answers to have questions[i] -> answers[i] */
    for (let i = 0; i < this.questions.length; i++) {
      if (this.questions[i].type === QuestionsTypeEnum.MULTIPLE_CHOICES) {
        this.answers.push([]);
      }

      this.answers.push("");
    }
  },
})
</script>
