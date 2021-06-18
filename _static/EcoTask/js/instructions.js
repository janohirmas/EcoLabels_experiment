const GameBody = document.getElementsByClassName('otree-body container')[0];

// Initialize slide index //
let slideIndex = 1;
showSlides(slideIndex);


// Next/previous controls: activate showSlides functions if arrows and arrow keys pressed. Stops the slides from going in "carousel" + slide 5 & 6 enabled after hovering a button on slide 4. 
function plusSlides(n) {
    if (n === 1 && slideIndex === 5 && conditionSlide4 === false) {
        return;
    } else if (n === (-1) && slideIndex === 1) {
        return;
    } else if (n === 1 && slideIndex === 7) {
        return;
    } else {
        showSlides(slideIndex += n);
    }
};

// Thumbnail image controls (slide 5 & 6 enabled after hovering a button on slide 4)
function currentSlide(n) {
    if (n === 6 && slideIndex <= 5 && conditionSlide4 === false) {
        return;
    } else if (n === 7 && slideIndex <= 5 && conditionSlide4 === false) {
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
    } else if (keypress === 'ArrowRight') {
        plusSlides(1);
    }
});

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

document.addEventListener("DOMContentLoaded", function (debug = true) {
    InitializeVT(document.getElementsByClassName('otree-body')[0]);
    // Convert all buttons with the class 'clickable' into click VT buttons
    ConvertButtons2VT('clickable', sActivation = 'click');
    // Convert all buttons with the class 'mousy' into mouseover VT buttons
    ConvertButtons2VT('mousy', sActivation = 'mouseover');
    // Convert all buttons with the class 'row' into click VT buttons that activate outcome-buttons with the class 'r1'
    ConvertButtons2VT('row', sActivation = 'click', 'r1');
});

// ----------------------------------------------------- //

// Time and Click variables
var sPreviousPress = 'Start';
var dPreviousTime = new Date().getTime();
var now = new Date().getTime();
var StartTime = new Date().getTime();
var diff = 0;

// ----------------------------------------------------- //



// ----------------------------------------------------- //
//  Function:       1. Creates inputs necessary for Visual Trace
// 
//  Inputs:
//    - btn      : Target button, where evenlistener will be added 
//    - sValue   : String, value
// ----------------------------------------------------- //
function InitializeVT(Body, sNameButtonClicks = 'sButtonClick', sNameTimeClicks = 'sTimeClick') {
    if (isEmpty(Body)) {
        Body = document.getElementsByTagName('body')[0];
    }
    // Create hidden input (Pressed Buttons)
    var sButtonClick = document.createElement("input");
    sButtonClick.type = 'hidden';
    sButtonClick.name = sNameButtonClicks;
    sButtonClick.id = sNameButtonClicks;
    sButtonClick.value = '';

    // Create hidden input (Time Buttons)
    var sTimeClick = document.createElement("input");
    sTimeClick.type = 'hidden';
    sTimeClick.name = sNameTimeClicks;
    sTimeClick.id = sNameTimeClicks;
    sTimeClick.value = '';

    // Append Inputs
    Body.appendChild(sButtonClick);
    Body.appendChild(sTimeClick);
}


// ----------------------------------------------------- //
//  Function:       1.  scans all buttons with specific class 
//                      and converts them to Visual-Tracing Buttons 
//  Inputs:
//    - sButtonClass      : class that encompases buttons to add event listener
//    - sActivation       : Target button, where evenlistener will be added 
//    - sDisplayClass     : string with classes that should be activated.
//                          If empty, then activates itself
//  Outputs:
//    - vVT_Buttons : array with all buttons with Visual-Tracing certain visual tracing class
// ----------------------------------------------------- /
function ConvertButtons2VT(sButtonClass, sActivation = 'click', sDisplayClass) {
    vVT_Buttons = document.getElementsByClassName(sButtonClass);
    console.log(vVT_Buttons);
    for (let j = 0; j < vVT_Buttons.length; j++) {
        console.log('Added ' + sActivation + ' to activate ' + sDisplayClass);
        AddVisualTracer(vVT_Buttons[j], sActivation, sDisplayClass);
    };
    return vVT_Buttons;
}

// ----------------------------------------------------- //
//  Function:       1. Looks at string value and detects form "img:Name"  
//                  2. In case of image, replaces value for image Tag
//                  3. Adds cleaned value to button 
//  Inputs:
//    - btn      : Target button, where evenlistener will be added 
//    - sValue   : String, value
// ----------------------------------------------------- //
function CheckImage(btn, sValue) {
    // Check if Image:

    if (sValue.substring(0, 4) == 'img:') {
        //console.log(btn.id+' is image')
        let ButtonImage = document.createElement('img');
        ButtonImage.src = '/static/EcoLabels/' + sValue.substring(4);
        ButtonImage.className = 'button-img'
        btn.appendChild(ButtonImage);
        return
    } else {
        //console.log(btn.id+' is other')
        btn.innerHTML = sValue;
    }

};
// ----------------------------------------------------- //
//  Function:      1. Checks is string is empty and/or undefined
//  Inputs:
//    - str      : Target button, where evenlistener will be added 
//  Output: 
//    - Boolean, true if element is empty and/or undefined
// ----------------------------------------------------- //
function isEmpty(str) {
    return (!str || str.length === 0);
};

// ----------------------------------------------------- //
//  Function:       1. Adds OnClick or Mouseover/Mouseout  
//                  2. Records Times and Clicks Accordingly
//  Inputs:
//    - btn             : Target button, where evenlistener will be added 
//    - sActivation     : String, activation method for button
//    - DisplayClass    : String, class combination that will be activated
// ----------------------------------------------------- //

function AddVisualTracer(btn, sActivation = 'click', sDisplayClass) {
    // add ID as a class
    btn.classList += ' ' + btn.id;
    // If there is no activation class, use self id. 
    if (isEmpty(sDisplayClass)) {
        sDisplayClass = btn.id;
    }

    if (sActivation == 'click') {
        // If click
        btn.addEventListener('click', function () {
            // Check it's not double click
            if (btn.id != sPreviousPress) {
                // Record new time
                now = new Date().getTime();
                // display specific content and hide rest
                HideEverything();
                DisplayContent(sDisplayClass);
                // record button pressed  
                if (sButtonClick.value) {
                    sButtonClick.value = sButtonClick.value + ';' + btn.id;
                } else {
                    sButtonClick.value = btn.id;
                };
                // change previous to new
                sPreviousPress = btn.id;
                //console.log(sButtonClick.value);

                // Check if there was lost of focus
                if (typeof bCheckFocus !== 'undefined' && bCheckFocus == true && TBlur >= dPreviousTime) {
                    // substract the blurred time
                    diff = (now - dPreviousTime) - (TFocus - TBlur);
                } else {
                    diff = (now - dPreviousTime);
                }
                // Add Time
                if (sTimeClick.value) {
                    sTimeClick.value = sTimeClick.value + ';' + diff;
                } else {
                    sTimeClick.value = diff;
                };
                // Replace previous time
                dPreviousTime = now;
            }
            //console.log(sTimeClick.value);  
        });

    } else if (sActivation == 'mouseover') {
        // mouseover
        btn.addEventListener('mouseover', function () {
            // Check that new element is pressed
            if (btn.id != sPreviousPress) {
                // Record new time
                dPreviousTime = new Date().getTime();
                // display specific content and hide rest
                HideEverything();
                DisplayContent(sDisplayClass);

                // record button pressed  
                if (sButtonClick.value) {
                    sButtonClick.value = sButtonClick.value + ';' + btn.id;
                } else {
                    sButtonClick.value = btn.id;
                };
                // change previous to new
                sPreviousPress = btn.id;
                //console.log(sButtonClick.value);
            }
        });
        // Mouseout
        btn.addEventListener('mouseout', function () {
            // Record Event Time
            now = new Date().getTime();
            // Hide the content & Reset previous item
            sPreviousPress = ' ';
            HideEverything();
            // Check if there is focus checks
            if (typeof bCheckFocus !== 'undefined' && bCheckFocus == true && TBlur >= dPreviousTime) {
                // substract the blurred time
                diff = (now - dPreviousTime) - (TFocus - TBlur);
            } else {
                diff = (now - dPreviousTime);
            }
            // Add Time
            if (sTimeClick.value) {
                sTimeClick.value = sTimeClick.value + ';' + diff;
            } else {
                sTimeClick.value = diff;
            };
            //console.log(sTimeClick.value);  
        });
    } else {
        console.log('"' + sActivation + '"' + ' is not a valid Activation method')
    }

};

// ----------------------------------------------------- //
//  Function:    Display Contents from a specific class  
//  Inputs:
//    - DisplayClass    : String, class combination that will be activated
// ----------------------------------------------------- //

function DisplayContent(DisplayClass) {
    let x = document.getElementsByClassName(DisplayClass);
    for (let i = 0; i < x.length; i++) {
        x[i].classList.remove('hidden');
        x[i].classList.add('non-hidden');
    }
};

// ----------------------------------------------------- //
//  Function:     Hide all elements in the table  
// ----------------------------------------------------- //

function HideEverything() {
    let x = document.getElementsByClassName("button-outcome");
    // console.log(x);
    for (let i = 0; i < x.length; i++) {
        x[i].classList.remove('non-hidden');
        x[i].classList.add('hidden');
    }
};