// Variable Declarations
const muscle_quiz_btn = document.querySelector("#muscle-quiz-btn");
const muscle_container = document.querySelector(".muscle-groups");
const quiz_container = document.querySelector(".quiz-container");
const muscle_goback_btn = document.querySelector("#muscle-goback");
const muscle_submit_btn = document.querySelector("#muscle-submit");
const muscle_check = document.querySelector("#muscle-check");

// Event Listeners
muscle_quiz_btn.addEventListener('click', function(){
    muscle_container.classList.remove("show");
    quiz_container.classList.add("show");
});

muscle_goback_btn.addEventListener('click', function(){
    quiz_container.classList.remove("show");
    muscle_container.classList.add("show");
});

muscle_submit_btn.addEventListener('click', function(){
    var x = 0;
    const q1 = document.quiz.q1.value;
    const q2 = document.quiz.q2.value;
    const q3 = document.quiz.q3.value;
    const q4 = document.quiz.q4.value;
    if (q1 == "Rectus Femoris") {
        x++;
    }
    if (q2 == "Scapula Elevation") {
        x++;
    }
    if (q3 == "latissimus Dorsi") {
        x++;
    }
    if (q4 == "External Rotation of arms") {
        x++;
    }
    if (x==4){
        document.getElementById("muscle-check").checked = true;
    }
});