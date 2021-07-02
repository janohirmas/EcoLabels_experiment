
// Initialize slide index //
let slideIndex = 1;
showSlides(slideIndex);


// Next/previous controls: activate showSlides functions if arrows and arrow keys pressed. Stops the slides from going in "carousel" + slide 5 & 6 enabled after hovering a button on slide 4. 
function plusSlides(n) {
    if (n === 1 && slideIndex === 4 && conditionSlide4 === false) {
        return;
    } else if (n === (-1) && slideIndex === 1) {
        return;
    } else if (n === 1 && slideIndex === 6) {
        return;
    } else {
        showSlides(slideIndex += n);
    }
};

// Thumbnail image controls (slide 5 & 6 enabled after hovering a button on slide 4)
function currentSlide(n) {
    if (n === 5 && slideIndex <= 4 && conditionSlide4 === false) {
        return;
    } else if (n === 6 && slideIndex <= 4 && conditionSlide4 === false) {
        return;
    } else {
        showSlides(slideIndex = n);
    };
};

// User needs to hover over button on slide 4 to be able to go forward. Reveals text under button after hovering. 
let conditionSlide4 = false;

document.getElementById("b3").addEventListener("mouseover", (event) => {
    conditionSlide4 = true;
    document.getElementById("reveal").style.visibility = "visible";
});

// Next/previous keypress controls //

document.addEventListener('keydown', (event) => {
    let keypress = event.key;
    if (keypress === 'ArrowLeft') {
        plusSlides(-1);
        ArrowText();       
    } else if (keypress === 'ArrowRight') {
        plusSlides(1);
        ArrowText();
    }
});

// Hide text under arrows when user clicks left or right arrow button
function ArrowText() {
    document.getElementById("nextKey").style.display = "none"
    document.getElementById("prevKey").style.display = "none";
};

// Slide switch function //
function showSlides(n) {
    let i; // slide count
    let slides = document.getElementsByClassName("mySlides"); // get slides
    let dots = document.getElementsByClassName("dot"); // get dots
    let arrowLeft = document.querySelector("#leftArrow"); // get left arrow
    let arrowRight = document.querySelector("#rightArrow"); // get right arrow

    for (i = 0; i < slides.length; i++) { // hide slides by default
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) { // change dot color based on dot count
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block"; // show slide
    dots[slideIndex - 1].className += " active"; // change dot color 

    if (n === 1) {
        arrowLeft.style.display = "none" // make left arrow invisible on 1st slide
    } else if (n > 1) {
        arrowLeft.style.display = "block"
    }

    if (n >= slides.length) {
        arrowRight.style.display = "none" // make right arrow invisible on 4th slide
    } else if (n < slides.length) {
        arrowRight.style.display = "block"
    }

    if (n === 1) {
        document.getElementById("prevKey").style.display = "none";
    } else {
        document.getElementById("prevKey").style.display = "block";
    };
    if (n === slides.length) {
        document.getElementById("nextKey").style.display = "none";
    };

}


// QUESTIONS SLIDE //

// This function runs when "Submit" button is clicked. It compares all the inputs to question with solutions; if input is incorrect or empty, hint appears next to it. If the answer is correct, the function makes hint invisible again. If all inputs are correct, "Next" button will become visible. 

let submitButton = document.getElementById("submitAnswer"); // get submit button
let nextButton = document.getElementById("submit"); // get Next button

nextButton.style.display = "none" // Hide Next button

function validateAnswers() {

    let solutions = ['1', 'b', 'c']; // solutions
    let hints = document.getElementsByClassName("hint"); // make array of hints

    // get answer fields
    let A1 = document.getElementById("Q1");
    let A2 = document.getElementById("Q2");
    let A3 = document.getElementById("Q3");

    let answerList = [A1, A2, A3]; // create an array out of the answers
    let correct = 0; // initialize counter for correct answers

    for (i = 0; i < answerList.length; i++) { // iterate through answers
        if (answerList[i] !== null) { // check for empty fields
            answerList[i] = answerList[i].value; // get value if not empty
        }
        if (answerList[i] !== solutions[i] || answerList[i] === null) { // incorrect or empty field: show hint
            hints[i].style.visibility = "visible";
        } else {
            correct = correct + 1; // correct: increase counter, hide hint
            hints[i].style.visibility = "hidden";

        }
    }
    if (correct === answerList.length) { // if all correct, hide Submit button and show Next button
        submitButton.style.display = "none"
        nextButton.style.display = "block"
    }

}

// For the hover button on slide 4
document.addEventListener("DOMContentLoaded", function (debug = true) {
    InitializeVT(document.getElementsByClassName('otree-body')[0]);
    // Convert all buttons with the class 'mousy' into mouseover VT buttons
    ConvertButtons2VT('mousy', sActivation = 'mouseover');
});
