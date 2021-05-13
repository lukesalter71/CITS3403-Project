// Variable Declarations
const profile = document.querySelector(".profile");
const profile_menu = document.querySelector(".profile-menu");

// Event Listeners
profile.addEventListener('click', function(){
    if (profile_menu.classList.contains("show")){
        profile_menu.classList.remove("show");
    } else {
        profile_menu.classList.add("show");
    }
});