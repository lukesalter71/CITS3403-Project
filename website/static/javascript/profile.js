// Variable Declarations
const profile = document.querySelector(".profile");
const profile_menu = document.querySelector(".profile-menu");
const username = document.getElementById('username');
const average= document.getElementById('average');
const submissions = document.getElementById('submissions');

let jsondata = "";

async function getJson() {
    let response = await fetch('/quiz-history');
    let data = await response.json()
    return data;
}

async function main() {
    // Get stats from database
    jsondata = await getJson()
    console.log(jsondata);
    username.innerText = jsondata['name'] + "'s quiz history";
    average.innerText = "Your average mark for the quiz is  " + Math.ceil(jsondata['average']/10) + "/26";
    submissions.innerText = "You have attempted the quiz " + jsondata['submissions'] + " times";
}
 main();

// Event Listeners
profile.addEventListener('click', function(){
    if (profile_menu.classList.contains("show")){
        profile_menu.classList.remove("show");
    } else {
        profile_menu.classList.add("show");
    }
});