console.log(getCookie("token"))

const testData = {
    questions: [
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Ухаживать за животными",
                "Обслуживать машины и приборы (следить, регулировать)"
            ],
            categories: ["nature", "tech"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Помогать больным",
                "Составлять схемы, программы для вычислительных машин"
            ],
            categories: ["human", "sign_system"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Следить за качеством книжных иллюстраций, плакатов, картин",
                "Следить за состоянием, развитием растений"
            ],
            categories: ["image", "nature"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Работать с материалами (дерево, ткань, глина)",
                "Доводить товары до потребителя (реклама, продажа)"
            ],
            categories: ["tech", "human"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Обсуждать научно-популярные труды",
                "Обсуждать художественные книги (фильмы, пьесы, концерты)"
            ],
            categories: ["sign_system", "image"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Выращивать и ухаживать за животными",
                "Тренировать взрослых или детей какому-либо навыку (трудовому, учебному, спортивному)"
            ],
            categories: ["nature", "human"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Копировать рисунки, картины, изображения",
                "Управлять каким либо грузовым, подъемным или транспортным средством"
            ],
            categories: ["image", "tech"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Сообщать, доносить людям какую либо информацию",
                "Оформлять выставки, картины, витрины (подготавливать декорации)"
            ],
            categories: ["human", "image"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Ремонтировать вещи, изделия, технику, квартиры",
                "Искать и исправлять ошибки в текстах, программах"
            ],
            categories: ["tech", "sign_system"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Лечить животных",
                "Выполнять вычисления, расчёты"
            ],
            categories: ["nature", "sign_system"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Выводить новые сорта растений",
                "Конструировать, создавать новые технологии, проектировать дома, машины"
            ],
            categories: ["nature", "tech"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Разбирать ссоры между людьми, доказывать, пояснять, разнимать",
                "Проверять, уточнять чертежи, схемы, таблицы"
            ],
            categories: ["human", "sign_system"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Наблюдать, участвовать в работе кружков, художественной самодеятельности",
                "Наблюдать, изучать микроорганизмы"
            ],
            categories: ["image", "nature"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Обслуживать, налаживать медицинские приборы, аппараты",
                "Оказывать мед. помощь больным людям при ранениях, ушибах и т.д."
            ],
            categories: ["tech", "human"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Художественно, литературно описывать происходившие или выдуманные события",
                "Составлять отчёты о наблюдаемых явлениях, событиях, данных"
            ],
            categories: ["image", "sign_system"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Делать лабораторные анализы",
                "Принимать пациентов, выслушивать проблемы, назначать лечение"
            ],
            categories: ["nature", "human"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Красить или расписывать стены помещений, заниматься дизайном",
                "Осуществлять монтаж или сборку машин, приборов, техники"
            ],
            categories: ["image", "tech"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Организовывать экскурсии, представления, мероприятия",
                "Выступать на сцене, принимать участие в концертах"
            ],
            categories: ["human", "image"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Изготовлять по чертежам детали, одежду, изделия",
                "Заниматься черчением, копировать схемы, карты"
            ],
            categories: ["tech", "sign_system"]
        },
        {
            text: "Что вы выберете, если у вас будет лишь два варианта?",
            options: [
                "Вести борьбу с вредителями леса, сада, огорода",
                "Работать с клавиатурой (писать тексты, печатать, копировать, редактировать)"
            ],
            categories: ["nature", "sign_system"]
        }
    ],
    categories: {
        "nature": "Человек-природа",
        "tech": "Человек-техника",
        "human": "Человек-человек",
        "sign_system": "Человек-знаковая система",
        "image": "Человек-художественный образ"
    }
};

let currentQuestion = 0;
let answers = [];
let scores = {
    "nature": 0,
    "tech": 0,
    "human": 0,
    "sign_system": 0,
    "image": 0
};

// Инициализация теста
document.addEventListener('DOMContentLoaded', function () {
    renderQuestion();
    document.getElementById('submit-btn').addEventListener('click', showResults);
});

function renderQuestion() {
    const container = document.getElementById('questions-container');
    container.innerHTML = '';

    const question = testData.questions[currentQuestion];
    const questionElement = document.createElement('div');
    questionElement.className = 'question';

    const questionText = document.createElement('div');
    questionText.className = 'question-text';
    questionText.textContent = question.text;
    questionElement.appendChild(questionText);

    const optionsContainer = document.createElement('div');
    optionsContainer.className = 'options';

    question.options.forEach((option, index) => {
        const optionElement = document.createElement('div');
        optionElement.className = 'option';
        optionElement.textContent = option;
        optionElement.dataset.index = index;

        if (answers[currentQuestion] === index) {
            optionElement.classList.add('selected');
        }

        optionElement.addEventListener('click', function () {
            document.querySelectorAll('.option').forEach(opt => {
                opt.classList.remove('selected');
            });
            this.classList.add('selected');
            answers[currentQuestion] = parseInt(this.dataset.index);
            updateNavigation();
        });

        optionsContainer.appendChild(optionElement);
    });

    questionElement.appendChild(optionsContainer);
    container.appendChild(questionElement);
    updateProgress();
}

function updateProgress() {
    const progress = ((currentQuestion + 1) / testData.questions.length) * 100;
    document.getElementById('progress-bar').style.width = `${progress}%`;
    document.getElementById('progress-text').textContent =
        `Вопрос ${currentQuestion + 1} из ${testData.questions.length}`;
}

function updateNavigation() {
    const submitBtn = document.getElementById('submit-btn');
    // Check if all questions have been answered
    const allAnswered = testData.questions.every((_, idx) => answers[idx] !== undefined);

    submitBtn.textContent = 'Получить результаты';
    submitBtn.disabled = !allAnswered;
}

function showResults() {
    calculateResults();

    const resultsContainer = document.getElementById('results-content');
    resultsContainer.innerHTML = '';

    Object.keys(scores).forEach(categoryKey => {
        if (scores[categoryKey] > 0) {
            const categoryElement = document.createElement('div');
            categoryElement.className = 'result-category';

            const title = document.createElement('h3');
            title.textContent = `${testData.categories[categoryKey]} - ${scores[categoryKey]} баллов`;
            categoryElement.appendChild(title);

            resultsContainer.appendChild(categoryElement);
        }
    });

    sendResultsToServer(scores);
    document.getElementById('results').style.display = 'block';
    document.querySelector('.test-container').style.display = 'none';
}

function calculateResults() {
    Object.keys(scores).forEach(key => {
        scores[key] = 0;
    });

    answers.forEach((answerIndex, questionIndex) => {
        const question = testData.questions[questionIndex];
        const category = question.categories[answerIndex];
        scores[category]++;
    });
    //fetch("/api/send_results")
}
/* --- Existing code above remains unchanged --- */

// Add navigation buttons dynamically
/* --- Update renderNavigation function to hide Next button when Submit is visible --- */
function renderNavigation() {
    const navContainer = document.getElementById('navigation-container');
    navContainer.innerHTML = '';

    // Previous button
    const prevBtn = document.createElement('button');
    prevBtn.id = 'prev-btn';
    prevBtn.textContent = 'Назад';
    prevBtn.disabled = currentQuestion === 0;
    prevBtn.addEventListener('click', function () {
        if (currentQuestion > 0) {
            currentQuestion--;
            renderQuestion();
        }
    });
    navContainer.appendChild(prevBtn);

    // Next button
    const nextBtn = document.createElement('button');
    nextBtn.id = 'next-btn';
    nextBtn.textContent = 'Вперёд';
    nextBtn.disabled = (
        currentQuestion === testData.questions.length - 1 ||
        answers[currentQuestion] === undefined
    );
    nextBtn.addEventListener('click', function () {
        if (currentQuestion < testData.questions.length - 1 && answers[currentQuestion] !== undefined) {
            currentQuestion++;
            renderQuestion();
        }
    });

    // Determine if submit button is visible
    const submitBtn = document.getElementById('submit-btn');
    const isSubmitVisible = submitBtn && submitBtn.style.display !== 'none';

    // Only append Next button if submit is not visible
    if (!isSubmitVisible) {
        navContainer.appendChild(nextBtn);
    }
}

function renderQuestion() {
    const container = document.getElementById('questions-container');
    container.innerHTML = '';

    const question = testData.questions[currentQuestion];
    const questionElement = document.createElement('div');
    questionElement.className = 'question';

    const questionText = document.createElement('div');
    questionText.className = 'question-text';
    questionText.textContent = question.text;
    questionElement.appendChild(questionText);

    const optionsContainer = document.createElement('div');
    optionsContainer.className = 'options';

    question.options.forEach((option, index) => {
        const optionElement = document.createElement('div');
        optionElement.className = 'option';
        optionElement.textContent = option;
        optionElement.dataset.index = index;

        if (answers[currentQuestion] === index) {
            optionElement.classList.add('selected');
        }

        optionElement.addEventListener('click', function () {
            document.querySelectorAll('.option').forEach(opt => {
                opt.classList.remove('selected');
            });
            this.classList.add('selected');
            answers[currentQuestion] = parseInt(this.dataset.index);
            updateNavigation();
            renderNavigation(); // Update navigation button states
        });

        optionsContainer.appendChild(optionElement);
    });

    questionElement.appendChild(optionsContainer);
    container.appendChild(questionElement);
    updateProgress();
    renderNavigation(); // Render navigation buttons for each question
}

function updateNavigation() {
    const submitBtn = document.getElementById('submit-btn');
    const allAnswered = testData.questions.every((_, idx) => answers[idx] !== undefined);

    if (currentQuestion === testData.questions.length - 1) {
        // Only show the button on the last question and if all are answered
        showSubmitBtn(allAnswered);
        submitBtn.textContent = 'Получить результаты';
        submitBtn.disabled = !allAnswered;
    } else {
        // Hide the button on all other questions
        showSubmitBtn(false);
    }
}

// Initialization: Add navigation container and render first question
document.addEventListener('DOMContentLoaded', function () {
    // Add navigation container if not present
    if (!document.getElementById('navigation-container')) {
        const navDiv = document.createElement('div');
        navDiv.id = 'navigation-container';
        navDiv.style.marginTop = '20px';
        document.getElementById('questions-container').after(navDiv);
    }
    // Hide the submit button initially
    showSubmitBtn(false);
    renderQuestion();
    document.getElementById('submit-btn').addEventListener('click', showResults);
});

function createCookie(name, value, days) {
    var expires;
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    }
    else {
        expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) {
                c_end = document.cookie.length;
            }
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}

/**
 * Sends the test results to the server via POST request.
 * @param {Object} results - The scores object to send.
 * @returns {Promise<Response>} The fetch response promise.
 */
function sendResultsToServer(results) {
    return fetch('/api/send_results', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            //'Authorization': 'Bearer'
            // If you need to send a token, you can add it here:
            'Authorization': 'Bearer ' + getCookie('token')
        },
        body: JSON.stringify({ "results": results })
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to send results');
            }
            return response.json();
        })
        .catch(error => {
            console.error('Error sending results:', error);
        });
}


/* --- Add this utility function --- */
function showSubmitBtn(show) {
    const submitBtn = document.getElementById('submit-btn');
    if (show) {
        submitBtn.style.display = '';
    } else {
        submitBtn.style.display = 'none';
    }
}