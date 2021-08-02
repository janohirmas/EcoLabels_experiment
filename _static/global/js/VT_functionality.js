
// ----------------------------------------------------- //

// Time and Click variables
var sPreviousPress  = 'Start';
var dPreviousTime   = new Date().getTime();
var now             = new Date().getTime();
var StartTime       = new Date().getTime();
var diff            = 0;

// ----------------------------------------------------- //



// ----------------------------------------------------- //
//  Function:       1. Creates inputs necessary for Visual Trace
// 
//  Inputs:
//    - btn      : Target button, where evenlistener will be added 
//    - sValue   : String, value
// ----------------------------------------------------- //
function InitializeVT(Body,sNameButtonClicks='sButtonClick',sNameTimeClicks='sTimeClick') {
  if (isEmpty(Body)) {
    Body = document.getElementsByTagName('body')[0];
  }
  // Create hidden input (Pressed Buttons)
  var sButtonClick        = document.createElement("input");
  sButtonClick.type       = 'hidden';
  sButtonClick.name       = sNameButtonClicks;
  sButtonClick.id         = sNameButtonClicks;
  sButtonClick.value      = '';

  // Create hidden input (Time Buttons)
  var sTimeClick   = document.createElement("input");
  sTimeClick.type  = 'hidden';
  sTimeClick.name  = sNameTimeClicks;
  sTimeClick.id    = sNameTimeClicks;
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
//    void
// ----------------------------------------------------- /
function ConvertButtons2VT(sButtonClass,sActivation='click', sDisplayClass) {
  lVTbtns = document.getElementsByClassName(sButtonClass);
  for (let j=0; j<lVTbtns.length; j++) {
    console.log(`${lVTbtns[j].id}:Added ${sActivation} to activate ${sDisplayClass}`);
    AddVisualTracer(lVTbtns[j],sActivation,sDisplayClass);
  };
}


// ----------------------------------------------------- //
//  Function:      1. Checks is string is empty and/or undefined
//  Inputs:
//    - str      : Target button, where evenlistener will be added 
//  Output: 
//    - Boolean, true if element is empty and/or undefined
// ----------------------------------------------------- //
function isEmpty(str) {
  return (!str || str.length === 0 );
};

// ----------------------------------------------------- //
//  Function:       1. Adds OnClick or Mouseover/Mouseout  
//                  2. Records Times and Clicks Accordingly
//  Inputs:
//    - btn             : Target button, where evenlistener will be added 
//    - sActivation     : String, activation method for button
//    - DisplayClass    : String, class combination that will be activated
// ----------------------------------------------------- //

function AddVisualTracer(btn,sActivation='click',sDisplayClass) { 

  btn.classList.add(btn.id);                                       // add ID as a class
  if (isEmpty(sDisplayClass)) { sDisplayClass = btn.id; }          // If there is no activation class, use self id. 

  if (sActivation=='click') {
    btn.addEventListener('click', function() {
      
      if (btn.id != sPreviousPress) {                              // Check it's not double click
          now = new Date().getTime();                              // Record new time
          
          hideEverything();                                        // display specific content and hide rest
          displayContent(sDisplayClass);
            
          if (sButtonClick.value) {                                // record button pressed
            sButtonClick.value = sButtonClick.value+';'+btn.id;
          } else {
            sButtonClick.value = btn.id;
          };
        sPreviousPress = btn.id;                                   // change previous to new
        if (typeof bCheckFocus !== 'undefined' &&                  // Check if there was lost of focus
        bCheckFocus==true && TBlur>=dPreviousTime) {
          // substract the blurred time
          diff = (now-dPreviousTime)-(TFocus-TBlur);
        } else {
          diff = (now-dPreviousTime);
        }
        // Add Time
        if (sTimeClick.value) {
          sTimeClick.value = sTimeClick.value+';'+ diff;
        } else {
          sTimeClick.value = diff;
        };
        // Replace previous time
        dPreviousTime = now;
      }
      //console.log(sTimeClick.value);  
    });
    
  } else if (sActivation=='mouseover') {
    // mouseover
    btn.addEventListener('mouseover', function() {
      // Check that new element is pressed
      if (btn.id != sPreviousPress) {
        // Record new time
        dPreviousTime = new Date().getTime();
        // display specific content and hide rest
        hideEverything();
        displayContent(sDisplayClass);
        
        // record button pressed  
        if (sButtonClick.value) {
          sButtonClick.value = sButtonClick.value+';'+btn.id;
        } else {
          sButtonClick.value = btn.id;
        };
        // change previous to new
        sPreviousPress = btn.id;
        //console.log(sButtonClick.value);
      }
    });
    // Mouseout
    btn.addEventListener('mouseout', function() {
      // Record Event Time
      now   = new Date().getTime();
      // Hide the content & Reset previous item
      sPreviousPress = ' ';
      hideEverything();
      // Check if there is focus checks
      if (typeof bCheckFocus !== 'undefined' && bCheckFocus==true && TBlur>=dPreviousTime) {
        // substract the blurred time
        diff = (now-dPreviousTime)-(TFocus-TBlur);
      } else {
        diff = (now-dPreviousTime);
      }
      // Add Time
      if (sTimeClick.value) {
        sTimeClick.value = sTimeClick.value+';'+ diff;
      } else {
        sTimeClick.value = diff;
      };
      //console.log(sTimeClick.value);  
  });
} else {
  console.log('"'+sActivation+'"'+' is not a valid Activation method')
}

};





// ----------------------------------------------------- //
//  Function:    Display Contents from a specific class  
//  Inputs:
//    - sClassName    : (string) classNames of buttons to be displayed
//    - sButtonClass  : (string) classNames of buttons that can be displayed 
// ----------------------------------------------------- //

function displayContent(sClassName, sButtonClass='btn-outcome') {
  // Hide everything before
  hideEverything();
  // Load relevant buttons
  let lBtnOutcome = document.getElementsByClassName(`${sClassName} ${sButtonClass}`);
  // Reveal their content
  for (let i=0; i<lBtnOutcome.length; i++) {
      let content = lBtnOutcome[i].getElementsByClassName('btn-content')[0];
      let hidden  = lBtnOutcome[i].getElementsByClassName('btn-hidden')[0];
      // hide content
      content.classList.add('active');
      content.classList.remove('inactive');
      // reveal hidden display
      hidden.classList.add('inactive');
      hidden.classList.remove('active');
  }
};

// ----------------------------------------------------- //
//  Function:     Hide all elements in the table  
// ----------------------------------------------------- //

function hideEverything() {
  // Load Content and Hidden Content divs
  let lContent = document.getElementsByClassName('btn-content');
  let lHidden  = document.getElementsByClassName('btn-hidden');
  // Check that the same amount of content and hidden divs are in the page
  if (lContent.length!==lHidden.length) {
      console.log("the number of 'btn-content' and 'btn-hidden' divs must be equal");
  } else {
      for (let i=0; i<lContent.length; i++ ) {
          // hide content
          lContent[i].classList.add('inactive');
          lContent[i].classList.remove('active');
          // reveal hidden display
          lHidden[i].classList.add('active');
          lHidden[i].classList.remove('inactive');
      };
  };
};
