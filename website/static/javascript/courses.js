// Variable Declarations
const muscleContainer = document.querySelector("#muscle-container");
const moreMuscle = document.querySelector("#more-muscle");
const strengthContainer = document.querySelector("#strength-container");
const moreStrength = document.querySelector("#more-strength");
const weightContainer = document.querySelector("#weight-container");
const moreWeight = document.querySelector("#more-weight");

const backButton = document.querySelectorAll("a.back-btn");

// Event Listeners
muscleContainer.addEventListener('click', function(){
    moreMuscle.classList.add('more-muscle');
});
strengthContainer.addEventListener('click', function(){
    moreStrength.classList.add('more-strength');
});
weightContainer.addEventListener('click', function(){
    moreWeight.classList.add('more-weight');
});

backButton.forEach(
    function(i){
        i.addEventListener('click', function(){
            setTimeout(function(){
                if (moreMuscle.classList.contains('more-muscle')){
                    moreMuscle.classList.remove('more-muscle');
                } else if (moreStrength.classList.contains('more-strength')){
                    moreStrength.classList.remove('more-strength');
                } else if (moreWeight.classList.contains('more-weight')){
                    moreWeight.classList.remove('more-weight');
                }
            }, 1000);     
        });
    }
);