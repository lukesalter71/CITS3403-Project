// Variable Declarations
const muscleContainer = document.querySelector("#muscle-container");
const strengthContainer = document.querySelector("#strength-container");
const weightContainer = document.querySelector("#weight-container");
const muscleImg = document.querySelector("#muscle-img");
const strengthImg = document.querySelector("#strength-img");
const weightImg = document.querySelector("#weight-img");

// Event Listeners
muscleContainer.addEventListener('mouseover', function(){
    muscleImg.classList.toggle('hover');
});
muscleContainer.addEventListener('mouseout', function(){
    muscleImg.classList.toggle('hover');
});
strengthContainer.addEventListener('mouseover', function(){
    strengthImg.classList.toggle('hover');
});
strengthContainer.addEventListener('mouseout', function(){
    strengthImg.classList.toggle('hover');
});
weightContainer.addEventListener('mouseover', function(){
    weightImg.classList.toggle('hover');
});
weightContainer.addEventListener('mouseout', function(){
    weightImg.classList.toggle('hover');
});


