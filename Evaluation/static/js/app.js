const app = Vue.createApp({
    template: `<div v-for="category in datas">
                    #{{category.category_title}}
                    <div v-for="question in category.questions">
                    ---{{question.question_text}}
                    <div v-for="answer in question.answers">
                    *******{{answer.answer_text}}
                    </div>
                    </div>
                </div>`,
    data() {
        return {
            datas : []
        }
    },
    methods: {

    },
    async created() {
        const response = await fetch("http://127.0.0.1:8000/evaluation/qa_new");
        const data = await response.json();
        this.datas = data;
    }

})

app.mount('#app')