const app = Vue.createApp({
  template: `<div class="container-md border border-info mt-3 mb-3 rounded">
    <form>
        <div class="container-md text-md-center mt-4 ">
            *لطفا در فرم زیر ابتدا فرد مورد ارزیابی و سپس نسبت خود با فرد مورد ارزیابی مشخص نمایید*
        </div>
        <div class="row m-3">
            <div class="col">
                <select class="form-select" aria-label="Default select example">
                    <option v-for="employee in employees" :value="employee.id">{{employee.first_name}}
                        {{employee.last_name}}</option>
                </select>
            </div>
            <div class="col">
                <select class="form-select" aria-label="Default select example">
                    <option v-for="relationship in relationships" :value="relationship.id">
                        {{relationship.title}}</option>
                </select>
            </div>
        </div>
        <div class="container-sm text-md-center mt-4  ">
            لطفا سؤالات زیر را با دقت پاسخ دهید
        </div>
        <div class="container d-block">
            <div v-for="category in qa">
                <div class="m-5">
                    {{category.category_title}}
                </div>
                <div v-for="question in category.questions">
                    {{ question.question_text}}
                        <div v-for="answer in question.answers" style="display: flex; flex-direction: row; margin-bottom: 10px;" required>
                            <div st>
                                <input  :name ="question.question_id" class="form-check-input" type="radio">
                            </div>
                            <div class="container">
                                <label class="form-check-label" >
                                    {{answer.answer_text}}
                                  </label>
                            </div>
                            
                          </div>
                </div>

            </div>

        </div>
</div>

</form>
</div>`,
  data() {
    return {
      shit: "shit",
      qa: [
        {
          category_title: "shit",
          questions: [
            {
              question_id: 1,
              question_text: "آیا الفاظش مناسب است؟",
              answers: [
                { answer_id: 1, answer_text: "بله" },
                { answer_id: 2, answer_text: "خیر" },
              ],
            },
            {
              question_id: 1,
              question_text: "آیا الفاظش مناسب است؟",
              answers: [
                { answer_id: 1, answer_text: "بله" },
                { answer_id: 2, answer_text: "خیر" },
              ],
            },
          ],
        },
        {
          category_title: "اخلاقی",
          questions: [
            {
              question_id: 1,
              question_text: "آیا الفاظش مناسب است؟",
              answers: [
                { answer_id: 1, answer_text: "بله" },
                { answer_id: 2, answer_text: "خیر" },
              ],
            },
            {
              question_id: 1,
              question_text: "آیا الفاظش مناسب است؟",
              answers: [
                { answer_id: 1, answer_text: "بله" },
                { answer_id: 2, answer_text: "خیر" },
              ],
            },
          ],
        },
      ],
      employees: [
        { id: 5, first_name: "هومن", last_name: "فهیمی" },
        { id: 6, first_name: "حسین", last_name: "فلاح" },
        { id: 7, first_name: "حجت", last_name: "صادقی" },
      ],
      relationships: [
        { id: 1, title: "خودم", score_weight: 0 },
        { id: 2, title: "همکار مستقیم", score_weight: 2 },
      ],
    };
  },
  methods: {},
  // async created() {
  //     const response_qa = await fetch("http://127.0.0.1:8000/evaluation/qa_new");
  //     const data = await response_qa.json();
  //     this.qa = data;

  // }
});

app.mount("#app");
