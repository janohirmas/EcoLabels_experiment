// Dynamic variables
var slideIndex = 0;
// Constants and Scales
const countries = ["My country is not listed", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Anguilla", "Antigua & Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia & Herzegovina", "Botswana", "Brazil", "British Virgin Islands", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central Arfrican Republic", "Chad", "Chile", "China", "Colombia", "Congo", "Cook Islands", "Costa Rica", "Cote D Ivoire", "Croatia", "Cuba", "Curacao", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands", "Faroe Islands", "Fiji", "Finland", "France", "French Polynesia", "French West Indies", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea Bissau", "Guyana", "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauro", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russia", "Rwanda", "Saint Pierre & Miquelon", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "St Kitts & Nevis", "St Lucia", "St Vincent", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor L'Este", "Togo", "Tonga", "Trinidad & Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks & Caicos", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Virgin Islands (US)", "Yemen", "Zambia", "Zimbabwe"];
const likertScale = [ 'Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'];
const likertValues = [1,2,3,4,5];
const height = 70;
const width = 80;
const BackButtonProps = [
    {
        sName: 'type',
        sProperty: 'button',
    },
    {
        sName: 'class',
        sProperty: 'button QT-Back',
    },
    {
        sName: 'onclick',
        sProperty: `backSlide()`,
    },
];
const NextButtonProps = [
    {
        sName: 'type',
        sProperty: 'button',
    },
    {
        sName: 'class',
        sProperty: 'button QT-Back',
    },
];

const myQuestions = [ 
    {
        question: "Which gender do you identify the most with?",
        name: "D2",
        type: "radio",
        values: [1,2,3,4],
        labels: [
            "Female",
            "Male",
            "Other",
            "Prefer not to say"
        ]
    },
    {
        question: "What country do you live in?",
        name: "D3",
        type: "autocomplete",
        list: countries,
    },
    {question: "Reducing water consumption is necessary for sustainable development.",
    name: "QT1",
    type: "radioH",
    values: likertValues,
    labels: likertScale,
    },
    // {
    //     question: "During the experiment, did you use any specific strategy or rule of thumb when deciding which of the two products to purchase? If so, describe it shortly.",
    //     name: "D7",
    //     type: "longOpen",
    // },
    {
        question: "What is your age?",
        name: "D1",
        type: "shortOpen",
    },
];
const maxQ  = myQuestions.length;


// Initialize
document.addEventListener("DOMContentLoaded", function() {

    // Create Slides
    let divAnswers = document.getElementById('final-answers');
    let counter = 0;
    myQuestions.forEach(question => { 
        // Create slide
        let slide = new QuestionSlide(counter,question);
        counter++;
        slide.printSlide();
        // Create input
        let input   = document.createElement('input');
        input.type  = 'hidden';
        input.value = '';
        input.name  = question.name;
        input.id    = question.name;
        divAnswers.appendChild(input);
        // Add autocomplete if necessary
        if (question.type==='autocomplete') {
                autocomplete(document.getElementById(`answer-${question.name}`), question.list);
        }
    });
    // prevent submitting the questionnaire if user click "Enter"
    $(document).ready(function () {
        $(window).keydown(function (event) {
            if (event.keyCode == 13) {
                event.preventDefault();
                return false;
            }
        });
    });
    // Add eventListener to advance with Enter
    // document.addEventListener('keydown', (event) => {
    //     let keypress = event.key;
    //     if (keypress === 'Enter' && checkAnswer(false)) { 
    //         hideEnter(); // hide all (Press enter indications)
    //         plusSlides(1); // click 'Enter' = next slide
    //     }; 
    // });
    
    // Create submit hidden button


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
    slideQuestion.className = 'question-slide fade';
    slideQuestion.id = `slide-${this.Question.name}`;
    // Create Question
    let pQuestion = document.createElement('p');
    pQuestion.className = 'question';
    pQuestion.innerHTML = this.Question.question;
    slideQuestion.appendChild(pQuestion);
    // Depending on input type, create inputs accordingly
    if (this.Question.type==='radio' || this.Question.type==='radioH') {
        // 1. Radio or RadioHorizontal
        // Create div for inputs
        let div = document.createElement('div');
        div.className = `div-input-${this.Question.type}`;
        // Check if labels for the values exist
        let labels = [];
        if (typeof this.Question.labels === 'undefined' || this.Question.labels === null) {
            labels = this.Question.values; 
        } else {
            labels = this.Question.labels;
        }
        let values = this.Question.values;
        // Check that labels and values have the same length
        if (labels.length != values.length) {
            console.log(`Question ${this.Question.name}: Dimensions of labels and values do not match`)
        };
        // Write inputs within div
        for (let i=0; i<values.length; i++) {
            // create input (for some reason I could not add the onclick command via js, so I input this as html)
            let input = `<label class="QT-${this.Question.type}"> ${labels[i]}
            <input type="radio" class="answer-${this.Question.name}" id="answer-${this.Question.name}-${i}" onclick="nextSlide('${this.Question.name}', '${values[i]}')"> 
             </label>`;
            div.innerHTML +=input;
        }
        // append question
        slideQuestion.appendChild(div);
    } else if (this.Question.type==='longOpen') {
        // Div container for input and Next Button
        let div     = document.createElement('div');
        div.className = 'div-input-text';
        // Create input
        let input   = document.createElement('textarea');
        input.rows  = '5';
        input.type  = 'text';
        input.className = 'input-text';
        input.name  = `answer-${this.Question.name}`;
        input.id    = `answer-${this.Question.name}`;
        input.cols  = '50';
        // Create next button
        var lProp       = NextButtonProps
        lProp.push( {sName: 'onclick', sProperty: `nextSlide('${this.Question.name}')`} );
        let NextButton = writeTag('button','Next',lProp);
        // Nest elements and append them to html
        div.appendChild(input);
        div.innerHTML += NextButton;
        slideQuestion.appendChild(div);
    
    } else if ( this.Question.type==='shortOpen' || this.Question.type==='autocomplete') {
        // Div container for input and Next Button
        let div     = document.createElement('div');
        div.className = 'div-input-text';
        // Create input
        let input   = document.createElement('input');
        input.type  = 'text';
        input.name  = `answer-${this.Question.name}`;
        input.id    = `answer-${this.Question.name}`;
        input.className = 'input-text';
        input.rows = '1';
        input.cols  = '50';
        input.placeholder = 'Type here...'
        // Add autocomplete
        if (this.Question.type ==='autocomplete') {
            input.className = 'autocomplete';
        }
        // Create wrapping form
        let form   = document.createElement('form');
        form.autocomplete  = 'off';
        form.action  = '/action_page.php';
        // Create next button
        let lProp       = NextButtonProps
        lProp.push( {sName: 'onclick', sProperty: `nextSlide('${this.Question.name}')`} );
        let NextButton = writeTag('button','Next',lProp);
        // Nest elements and append them to html
        form.appendChild(input);
        div.appendChild(form);
        div.innerHTML += NextButton;
        slideQuestion.appendChild(div);
    } 

    // Create back button

    let BackButton = writeTag('button','Back',BackButtonProps);
    // let BackButton = `<button type="button" class="button QT-Back" onclick="backSlide()" > Back </button>`
    // Create progress bar
    let progBar = writeProgBar(this.iSlideNumber)
    // Add Button and ProgressBar
    if (this.iSlideNumber>0) {slideQuestion.innerHTML+=BackButton};
    slideQuestion.innerHTML+= progBar;
    container = document.getElementsByClassName('element-container')[0];
    container.appendChild(slideQuestion);

};

// *********************************************************************
// Function Name:   writeProgBar()
// Functionality:
//                  1. writes a Tag with the specified requirements
//
// input:           sTag: Tag for the input (default: div)
//                  sInnerHTML: content inside (default: "")
//                  lAttr : list of object with all attributes. 
//                      - sName: string with the name of the attribute
//                      - sProperty: string with properties
//                  
// returns:         string with the html line
// ********************************************************************
function writeProgBar(slide) {
    return `<div class="pbar-container"> <label> 0% </label>
    <progress class="progress-bar" min="0" max="${maxQ}" value="${slide+1}"></progress>
                        <label> 100% </label> </div>`
}

// *********************************************************************
// Function Name:   writeTag()
// Functionality:
//                  1. writes a Tag with the specified requirements
//
// input:           sTag: Tag for the input (default: div)
//                  sInnerHTML: content inside (default: "")
//                  lAttr : list of object with all attributes. 
//                      - sName: string with the name of the attribute
//                      - sProperty: string with properties
//                  
// returns:         string with the html line
// ********************************************************************
function writeTag(sTag,sInnerHTML,lAttr) {
    str = `<${sTag}`;
    lAttr.forEach(elem => {
        str += ` ${elem.sName}="${elem.sProperty}"`;
    }); 
    str += `> ${sInnerHTML} </${sTag}>`;
    return str;
}

// *********************************************************************
// Function Name:   backSlide
// Functionality:
//                  1. Checks if question is answered, clears it
//                  2. Goes to the previous slide
//
// input:           null
// returns:         void
// ********************************************************************

function backSlide() {
    // uncheck answer
    checkAnswer(true);
    // go to previous slide
    plusSlides(-1);
}



// *********************************************************************
// Function Name:   nextSlide
// Functionality:
//                  1. Checks if question is answered
//                      and adds it to the inputs
//                  2. Goes to next slide
//
// input:           sQuestionName : name of the question
//                  sValue: (default="")
// returns:         void
// ********************************************************************

function nextSlide(sQuestionName,sValue="") {

    // Check that there is an answer
    
    if (checkAnswer()) {
        let input = document.getElementById(sQuestionName);
        if (sValue==="") {
            // Retrieve answer from forms
            let answer = document.getElementById(`answer-${sQuestionName}`).value;
            input.value =  answer;
        } else {
            input.value = sValue;
        }
    // go to next slide
    plusSlides(1);
}

}

// *********************************************************************
// Function Name:   checkAnswer
// Functionality:
//                  1. Checks if question is answered
//                  2. In case it's needed, cleans it
//
// input:           iSlideNumber:   slide number from myQuestions
//                  bClean:         Boolean, empties answer if true
// returns:         true, if questions has been answered
//                  false, if question is empty
// ********************************************************************

function checkAnswer(bClean=false) {
    let Question = myQuestions[slideIndex];
    let qType = Question.type;
    if (qType==='radio' || qType==='radioH' ) {
        let inputs = document.getElementsByClassName(`answer-${Question.name}`);
        if (bClean) { 
            console.log(`Question ${Question.name} cleared`);
            for (let i = 0; i<Question.values.length; i++) {
                inputs[i].checked = false;
            }
            return false
        } else {
            let bAnswered = false;
            for (let i = 0; i<Question.values.length; i++) {
                if (inputs[i].checked == true) {bAnswered=true}
            }
            return bAnswered;
        };
    } else if (qType === 'longOpen'|| qType === 'shortOpen'|| qType === 'autocomplete') {
        let input = document.getElementById(`answer-${Question.name}`);
        if (bClean) {
            console.log(`Question ${Question.name} cleaned`);
            input.value = ""
        }
        return (input.value!='');
    }
}

// Functions to move slides

// If Enter is clicked, hide text under Next button
function hideEnter() {
    document.getElementById("buttonText").style.visibility = "hidden"
};
// Advance a slide
function plusSlides(n) {
  showSlides(slideIndex += n);
}
// Show current slide
function currentSlide(n) {
  showSlides(slideIndex = n);
}
// *********************************************************************
// Function Name:   showSlides
// Functionality:   Display current slide, hide the rest
// Source: https://www.w3schools.com/howto/howto_js_slideshow.asp
//
// input:           n: Slide number to be shown
// returns:         void
// ********************************************************************
function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("question-slide");
    // Go back when reaching the end
    if (n >= slides.length) {
        document.getElementsByClassName('next_button')[0].click();
    } 
    // Avoid negative slide counter
    if (n < 1) {0};
  
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slides[slideIndex].style.display = "flex";  
  
  }
// *********************************************************************
// Function Name:   autocomplete
// Functionality:   Create autocomplete for text inputs
// Source: https://www.w3schools.com/howto/howto_js_autocomplete.asp
// input:           inp: HTML object, input that needs autocomplete
//                  arr: array of autocomplete options
// returns:         void
// ********************************************************************

  function autocomplete(inp, arr) {
    /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/
    var currentFocus;
    /*execute a function when someone writes in the text field:*/
    inp.addEventListener("input", function (e) {
        var a, b, i, val = this.value;
        /*close any already open lists of autocompleted values*/
        closeAllLists();
        if (!val) { return false; }
        currentFocus = -1;
        /*create a DIV element that will contain the items (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(a);
        /*for each item in the array...*/
        for (i = 0; i < arr.length; i++) {
            /*check if the item starts with the same letters as the text field value:*/
            if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
                /*create a DIV element for each matching element:*/
                b = document.createElement("DIV");
                /*make the matching letters bold:*/
                b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
                b.innerHTML += arr[i].substr(val.length);
                /*insert a input field that will hold the current array item's value:*/
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                /*execute a function when someone clicks on the item value (DIV element):*/
                b.addEventListener("click", function (e) {
                    /*insert the value for the autocomplete text field:*/
                    inp.value = this.getElementsByTagName("input")[0].value;
                    /*close the list of autocompleted values,
                    (or any other open lists of autocompleted values:*/
                    closeAllLists();
                });
                a.appendChild(b);
            }
        }
    });
    /*execute a function presses a key on the keyboard:*/
    inp.addEventListener("keydown", function (e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
            /*If the arrow DOWN key is pressed,
            increase the currentFocus variable:*/
            currentFocus++;
            /*and and make the current item more visible:*/
            addActive(x);
        } else if (e.keyCode == 38) { //up
            /*If the arrow UP key is pressed,
            decrease the currentFocus variable:*/
            currentFocus--;
            /*and and make the current item more visible:*/
            addActive(x);
        } else if (e.keyCode == 13) {
            /*If the ENTER key is pressed, prevent the form from being submitted,*/
            e.preventDefault();
            if (currentFocus > -1) {
                /*and simulate a click on the "active" item:*/
                if (x) x[currentFocus].click();
            }
        }
    });
    function addActive(x) {
        /*a function to classify an item as "active":*/
        if (!x) return false;
        /*start by removing the "active" class on all items:*/
        removeActive(x);
        if (currentFocus >= x.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = (x.length - 1);
        /*add class "autocomplete-active":*/
        x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
        /*a function to remove the "active" class from all autocomplete items:*/
        for (var i = 0; i < x.length; i++) {
            x[i].classList.remove("autocomplete-active");
        }
    }
    function closeAllLists(elmnt) {
        /*close all autocomplete lists in the document,
        except the one passed as an argument:*/
        var x = document.getElementsByClassName("autocomplete-items");
        for (var i = 0; i < x.length; i++) {
            if (elmnt != x[i] && elmnt != inp) {
                x[i].parentNode.removeChild(x[i]);
            }
        }
    }
    /*execute a function when someone clicks in the document:*/
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
}



