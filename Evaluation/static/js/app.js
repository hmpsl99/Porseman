const app = Vue.createApp({
  template: `<div class="container-md border border-info mt-3 mb-3 rounded">
  <form>
      <div class="container-md text-md-center mt-4 ">
          *لطفا در فرم زیر ابتدا فرد مورد ارزیابی و سپس نسبت خود با فرد مورد ارزیابی مشخص نمایید*
      </div>
      <div class="row m-3">
          <div class="col">
              <select @change="reviewee_setter($event)" class="form-select" aria-label="Default select example">
                  <option value=0>فرد مورد ارزیابی را انتخاب کنید</option>
                  <option v-for="employee in employees" :value="employee.id">{{employee.first_name}}
                      {{employee.last_name}}</option>
              </select>

          </div>
          <div class="col">
              <select @change="relationship_setter($event)" class="form-select" aria-label="Default select example">
                  <option value=0>نسبت خود را مشخص کنید</option>
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
              <div class="m-4 w-25  text-md-center border border-dark rounded-pill bg-info ">
                  <i class="bi bi-card-checklist"></i>
                  {{category.category_title}} :
              </div>
              <div v-for="question in category.questions" class="mt-5 mb-5 align-middle">
                  <i class="bi bi-question bg-warning border border rounded"></i>
                  {{ question.question_text}} :
                      <div v-for="answer in question.answers" class="mt-3 mb-3" style="display: flex; flex-direction: row; margin-bottom: 10px;" required>
                          <div st>
                              <input  :value="answer.answer_id" :name ="question.question_id" class="form-check-input" type="radio" v-model="this.answers[question.question_id]" required>
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
      <div class="container text-danger text-center" v-if="errors.length">
          <div v-for="error in errors" class="container text-danger">
              {{error}}
          </div>
      </div>
      <div class="container text-center text-danger" v-if="request_error.length">
          <div v-for="er in request_error" class="container text-danger">
              {{er}}
          </div>
      </div>
      <div class="container text-center">
          <button @click ="submit" type="button" class="btn btn-outline-primary text-center m-5">ثبت پاسخ</button>

      </div>
</div>
</form>
</div>`,
  data() {
    return {
      request_error: [],
      errors: [],
      qa: [],
      employees: [],
      relationships: [],
      reviewee_id: 0,
      relationship_with_reviewee: 0,
      answers: [],
    };
  },
  methods: {
    reviewee_setter(event) {
      this.reviewee_id = event.target.value;
    },
    relationship_setter(event) {
      this.relationship_with_reviewee = event.target.value;
    },
    answers_final_object(qa) {
      final_object = {};
      qa.forEach((category) => {
        q = category.questions;
        q.forEach((question) => {
          final_object[question.question_id] = 0;
        });
      });
      return final_object;
    },
    getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    },
    async submit() {
      base_url = "http://127.0.0.1:8000";
      this.errors = [];
      this.request_error = [];
      if (this.reviewee_id == 0) {
        this.errors.push("**لطفا فرد ارزیابی شونده را انتخاب کنید**");
      }
      if (this.relationship_with_reviewee == 0) {
        this.errors.push(
          "**لطفا نسبت خودتان با فرد ارزیابی شونده را مشخص کنید**"
        );
      }
      if (Object.values(this.answers).indexOf(0) > -1) {
        this.errors.push("**لطفا به تمامی سؤالات پاسخ دهید**");
      }
      if (this.errors.length == 0) {
        data = JSON.stringify({
          reviewee_id: this.reviewee_id,
          relationship_id: this.relationship_with_reviewee,
          answers: this.answers,
        });
        const rawResponse = await fetch(base_url + "/evaluation/qa_new", {
          method: "POST",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
          },
          mode : 'same-origin',
          body: data,
        });
        if (rawResponse.status == 200) {
          window.location.href = base_url + "/evaluation/success";
        } else {
          this.request_error.push(
            "متأسفانه ارزیابی ثبت نشد، لطفا دوباره تلاش کنید"
          );
        }
      }
    },
  },
  async created() {
    const base_url = "http://127.0.0.1:8000";
    const response_qa = await fetch(base_url + "/evaluation/qa_new");
    const data_qa = await response_qa.json();
    this.qa = data_qa;
    this.answers = this.answers_final_object(data_qa);
    const response_employees = await fetch(base_url + "/evaluation/employees");
    const data_employee = await response_employees.json();
    this.employees = data_employee;
    const response_relationships = await fetch(
      base_url + "/evaluation/relationships"
    );
    const data_relationships = await response_relationships.json();
    this.relationships = data_relationships;
  },
});

app.mount("#app");
