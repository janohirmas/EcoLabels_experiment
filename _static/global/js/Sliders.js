// General variables and constants
var iSlideIndex     = 0;                    // This variable is to know in which slide you are
var before          = new Date().getTime();
var now             = new Date().getTime();
var inputSlideSeq, inputSlideTim ;

// When page is loaded
document.addEventListener("DOMContentLoaded", function() {
    showSlides(iSlideIndex);                                            // show first slide
    // * Add here anything that needs to be added to the page when the rest of the content is already loaded
    TStart          = new Date().getTime();                             // Start Timer
    let slides      = document.getElementsByClassName("slide-item");
    adjustElem(slides[iSlideIndex]);                // adjust slide size   
    inputSlideSeq = document.getElementById('sSlideSequence');
    inputSlideTim = document.getElementById('sSlideTime');
});

// *********************************************************************
// * EVENT LISTENERS *
// *********************************************************************
window.addEventListener('resize', function() {
    let slides = document.getElementsByClassName("slide-item");
    adjustElem(slides[iSlideIndex]);                // adjust slide size
});

// Move slides with left and right arrows
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

// *********************************************************************
// * FUNCTIONS *
// *********************************************************************

// *********************************************************************
// * Please add here any constraints for the slides. 
// * For example: Participants do something special before they can move the slides again
// Function Name:   canMove
// Functionality:   
//                  1. Checks if slides can be passed
//
// input:           void
//
// returns:         boolean
// *********************************************************************

if (typeof canMove==='undefined') {
    function canMove(iSlideIndex) {
        return true;
    };
}


// *********************************************************************
// Function Name:   adjustElem
// Functionality:   
//                  1. resizes element until there is no overflow
//
// input:           elem: element, contains elements to resize
//
// returns:         void
// *********************************************************************

function adjustElem(elem) {
    let zoom = 1;  
    zoomChildren(elem,zoom);                                    // Set initial zoom as 100%
    let overflow = checkOverflow(elem);                         // boolean describing if element is overflown
    let iter = 0;                                               // max iteration in case something goes wrong
    // Iterate until there is no overflow
    while (overflow && iter<90) {
        zoom += -0.01;                                          // reduce zoom in 1%
        zoomChildren(elem,zoom);
        overflow = checkOverflow(elem);
        iter++;
    };
    if (iter==30) {console.log('problem resizing element')};   // notify in console if there is no convergence
};

// *********************************************************************
// Function Name:   zoomChildren
// Functionality:   
//                  1. zooms all children within an element
//
// input:           elem: element, contains elements to resize
//                  zoom: float, positive number denoting zoom (1 = 100%)
//
// returns:         void
// *********************************************************************

function zoomChildren(elem,zoom) {
    let children = elem.children;
    if (typeof children !=='undefined') {
        for (let i=0; i<children.length; i++) {
            if ('zoom' in children[i].style) {
                children[i].style.zoom = zoom;
            } else {
                mgH = children[i].offsetHeight*(zoom-1)/2;
                mgW = children[i].offsetWidth*(zoom-1)/2;
                children[i].style.margin = `${mgH}px ${mgW}px`;
                children[i].style.MozTransform = `scale(${zoom})`;
            }
        };
    };
};

// *********************************************************************
// Function Name:   checkOverflow
// Functionality:   
//                  1. hides text suggesting to press keys
//
// Source:          modified from: 
//                  https://www.codegrepper.com/code-examples/javascript/javascript+check+if+element+is+overflowing
//
// input:           elem, element to check if has overflow
//
// returns:         boolean, true if overflow
// *********************************************************************


function checkOverflow(elem) {
    let overflow = elem.clientWidth < elem.scrollWidth || elem.clientHeight < elem.scrollHeight;
    return overflow;
};


// *********************************************************************
// Function Name:   ArrowText
// Functionality:   
//                  1. hides text suggesting to press keys
//
// input:           void
//
// returns:         void
// *********************************************************************

function validateAnswers() {

    let lHints      = document.getElementsByClassName("hint");                          // make array of hints
    let lQuestions  = document.getElementsByClassName("ControlQuestions");              // make array of questions
    let iCorrect    = 0;                                                                // initialize counter for correct answers

    for (i = 0; i < lQuestions.length; i++) {                                           // iterate through answers
        if (lQuestions[i].value !== lSolutions[i] || lQuestions[i].value === null) {    // incorrect or empty field
            lHints[i].style.visibility = "visible";                                     // Show Hint
        } else {
            iCorrect +=1;                                                               // iCorrect: increase counter
            lHints[i].style.visibility = "hidden";                                      // Hide Hint
        }
    }
    if (iCorrect === lQuestions.length) {                                               // if all correct, Submit
        now = new Date().getTime(); 
        inputSlideSeq.value += iSlideIndex;
        inputSlideTim.value += now - before;
        document.getElementById('submit').click();
    }

}


// *********************************************************************
// Function Name:   ArrowText
// Functionality:   
//                  1. hides text suggesting to press keys
//
// input:           void
//
// returns:         void
// *********************************************************************
function ArrowText() {
    document.getElementById("nextKey").style.visibility = "hidden"
    document.getElementById("prevKey").style.visibility = "hidden";
};


// *********************************************************************
// Function Name:   plusSlides
// Functionality:   
//                  1. Changes slide index by adding n
//                  2. Shows slide SlideIndex+n 
//
// Source: https://www.w3schools.com/howto/howto_js_slideshow.asp
//
// input:           n: Number of slides to be skipped
//
// returns:         void
// *********************************************************************

function plusSlides(n) {
    if (canMove(iSlideIndex)) { 

        now = new Date().getTime(); 
        let dif = now - before
        inputSlideTim.value    += `${dif},`
        before = now;
        showSlides(iSlideIndex += n)
        inputSlideSeq.value += `${iSlideIndex},`;
    };
}

  // *********************************************************************
  // Function Name:   currentSlide
  // Functionality:   
  //                  1. Changes slide index to n
  //                  2. Shows slide n 
  //
  // Source: https://www.w3schools.com/howto/howto_js_slideshow.asp
  //
  // input:           n: Number of slides to be skipped
  //
  // returns:         void
  // *********************************************************************
  
  
  // Show current slide
function currentSlide(n) {
    if (canMove(iSlideIndex)) { showSlides(iSlideIndex = n)};
    
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
    let slides = document.getElementsByClassName("slide-item");
    let dots = document.getElementsByClassName("dot"); // get dots
    let nextDiv = document.getElementsByClassName('nextDiv')[0];
    let prevDiv = document.getElementsByClassName('prevDiv')[0];
    // let elemCont = document.getElementsByClassName("ContentContainer");
    // Avoid slide counter going out of bounds
    if (n <= 0) { iSlideIndex=0 };
    if (n >= slides.length ) { iSlideIndex=slides.length-1 };
    // Hide all slides
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";           // Hide slides
        dots[i].classList.remove("active");   // Deactivate dots
    }
    // Hide right arrows if last slide
    if (iSlideIndex == slides.length-1 ) {
        nextDiv.style.visibility = 'hidden';
    } else {
        nextDiv.style.visibility = 'visible';
    }
    // Hide right arrows if last slide
    if (iSlideIndex == 0 ) {
        prevDiv.style.visibility = 'hidden';
    } else {
        prevDiv.style.visibility = 'visible';
    }

    slides[iSlideIndex].style.display = "flex";     // Show displayed slide 
    dots[iSlideIndex].classList.add('active');      // Select active dot
    adjustElem(slides[iSlideIndex]);                // adjust slide size
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
  
