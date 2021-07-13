var slideIndex = 0;
let likertScale = [
    'Strongly Disagree',
    'Disagree',
    'Neutral',
    'Agree',
    'Strongly Agree'
];
myQuestions = [ 
    {
        question: "Which gender do you identify the most with?",
        name: "D2",
        type: "radioHorizontal",
        answers: [
            "Female",
            "Male",
            "Other",
            "Prefer not to say"
        ]
        
    },
    {
        question: "What is your age?",
        name: "D1",
        type: "open",
    },
];

// Initialize
document.addEventListener("DOMContentLoaded", function() {

    // Create Slides
    let counter = 0;
    myQuestions.forEach(question => { 
        let slide = new QuestionSlide(counter,question);
        slide.printSlide();
    });

    // Show first slide
    showSlides(slideIndex);
});

// Define Class: QuestionSlides
function QuestionSlide(iNumber, jsonQuestion) {
        this.iSlideNumber = iNumber;
        this.Question = jsonQuestion;
};

QuestionSlide.prototype.printSlide = function() {
    // Create Slide
    let slideQuestion = document.createElement('div');
    slideQuestion.className = 'question-slide';
    // Create Question
    let pQuestion = document.createElement('p');
    pQuestion.className = 'question';
    pQuestion.innerHTML = this.Question.question;
    slideQuestion.appendChild(pQuestion);
    // Depending on input type, create inputs accordingly
    // 1. Radio
    if (this.Question.type==='radio') {
        
        this.Question.answers.forEach(elem => {
            // create input
            let input = document.createElement('input');
            input.type = 'radio';
            input.value = elem;
            input.name = this.Question.name;
            input.addEventListener('click', function() { 
                showSlides(slideIndex += 1) 
            });

            // create label
            let label = document.createElement('label');
            label.className = 'QT-radio';
            label.appendChild(input);
            label.innerHTML +=" "+elem;
            slideQuestion.appendChild(label);
        })
    } else if (this.Question.type==='radioHorizontal') {
        let div = document.createElement('div');
        this.Question.answers.forEach(elem => {
            // create input
            let input = document.createElement('input');
            input.type = 'radio';
            input.className = 'QT-radioH'
            input.value = elem;
            input.name = this.Question.name;
            input.addEventListener('click', function() { 
                showSlides(slideIndex += 1) 
            });
            // create label
            let label = document.createElement('label');
            label.className = 'QT-label';
            label.appendChild(input);
            label.innerHTML +=" "+elem;
            // Add it to the div
            div.appendChild(label);
        });
        slideQuestion.appendChild(div);
    };
    // Creare back button
    let qName = this.Question.name;
    let BackButton = document.createElement('button');
    BackButton.type = 'button';
    BackButton.className = 'button QT-button';
    BackButton.innerHTML = 'Back'
    BackButton.onclick = function() {
        plusSlides(-1);
        // Reset answered input
        let inputs = document.getElementsByName(qName);
        inputs.forEach(elem => elem.checked = false);
    };
    slideQuestion.appendChild(BackButton);
    container = document.getElementsByClassName('element-container')[0];
    container.appendChild(slideQuestion);

};




// Functions to move slides

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("question-slide");
    // Go back when reaching the end
    if (n > slides.length) {slideIndex = slides.length}    
    // Avoid negative slide counter
    if (n < 1) {0};
  
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slides[slideIndex].style.display = "block";  
  
  }

