// General variables and constants
var slideIndex = 0;

document.addEventListener("DOMContentLoaded", function() {
    showSlides(slideIndex);
});


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

// Advance a slide
function plusSlides(n) {
    showSlides(slideIndex += n);
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
      let slides = document.getElementsByClassName("slide-item");
      // Go back when reaching the end
      if (n >= slides.length) {
          document.getElementById('final-button').click();
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
  
