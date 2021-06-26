THIS TEXT FILE IS FOR KEEPING RECORD OF CURRENT BUGS AND SUGGESTED IMPROVEMENTS


# To Do:

    ## CSS 

    - Change the font-sizes to em not vw or vh. 
        * em is a flexible property that depends on the users preference.
        * Careful: The property em inherits the parents' size. (if div1 has font-size 1.5em and div2 (inside div1) has size 2em, then the font size in div2 will be 1.5*2em) 
    
    ## Introduction

    - Add UvA Logo to introduction page. 

    ## Instructions

    - (AH) Change AvgDur, NN trials and Max Bonus in constants for lay-out
    - (AH) Add Overall Iddle Time-out
    - Write down Left(Right) arrow button: "(or press 'Left(right) arrow symbol')". Once any of them is pressed, the parenthesis should dissappear.
    - In the first slide, add the image of the company. Use Vars_for_template to load the image, so we can change it easier. 
    - Add "correct" symbol if answers were correct
    - Make "next"button more visible after it appear (animation or bordering)

    ## Practice Trials
    - (AH) Add Practice trials

    ## Decision

    - (AH) Choose prices
    - Change lay-out of button in Between.html

    ## Infographics
    - Change the order of first slide depending on what is presented first and after. (i.e. if order is leaves and stars, the first slide says stars and leaves. This can be confusing.)
    - Add check-up questions in infographic (don't record them). 
        1. If you get a product with 3 leaves (symbol), what is the maximum amount of trees that can be planted?
        2. If you get a product with 2 stars, what is the minimum amount of points you can get?
    - Add a page, now we are going to proceed with the experiment. (and next button)

    ## Questionnaire

    - Write down below button (or press 'Enter'). Once it's pressed, the parenthesis should dissappear. 
    - (AH) Add end-page with payment
    - (AH) If we use PlantOneTree, we can let them choose where to plant the trees and how many in each place :)

    ## Others (Are these still issues?)

    - Questionnaire: previous button (nextSlide function need to be changed for this to work)

    - Instructions: get slide texts, questions, dots from object instead of hardcoded

    - input fields and radiobuttons sizing is a little bit off with big screen.  

# BUGS 

> Instructions: there is still more slides than the current ones. Your function should look how many slides there are and act according to that. That should not be a value. But don't worry, change it manually now, I will fix it for the future. 

> Now the arrows don't appear until a couple of slides.

> Instructions: Size of the screen is more than 100vw, then when I press left or right the whole page moves. This can be a bit distracting.

(Are these still an issue?)

> Questionnaire: progress bar moves together with autocomplete dropdown menu. It should flow over it without the progress bar moving anywhere

> Instructions: slide 7 (questions) "jumps" down. Something wrong with container placement

> Infographic: when Next button appears on Slide 3, the dots stop working (cannot switch slide with them anymore). Probably something to do with the placing of the button. 