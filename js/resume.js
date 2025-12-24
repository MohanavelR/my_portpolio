/**================================ typing animaition================================================ */
var typed=new Typed(".typing",{
    strings:["Web developer"],
    typeSpeed:100,
    BackSpeed:100,
    backDelay:1000,
    loop:true
});

/*=================================== theme colors ================================= */
const alternateStyle=document.querySelectorAll('.alternate-style');
function setActiveStyle(color){
    alternateStyle.forEach((style) =>{
        if(color===style.getAttribute("title")){
            style.removeAttribute("disabled")
        }
        else{
            style.setAttribute("disabled","true");
        }

    })

}
/*=================================== theme light and dark  colors ================================= */
const dayNight=document.querySelector('.day-night');
dayNight.addEventListener('click',() =>{
    dayNight.querySelector("i").classList.toggle('fa-sun');
    dayNight.querySelector("i").classList.toggle('fa-moon');
    document.body.classList.toggle('dark')
})
window.addEventListener("load",() =>{
    if(document.body.classList.contains("dark")){
        dayNight.querySelector("i").classList.add("fa-moon")
    }
    else{
        dayNight.querySelector("i").classList.add("fa-sun")

    }
})

document.addEventListener("DOMContentLoaded", () => {
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
       if (entry.isIntersecting) {
      entry.target.classList.add('show');
    }
   
  });
}, {
//   threshold: 0.1,          // Trigger when 10% visible
//   rootMargin: "0px 0px -50px 0px" // Adjust detection region
});


  document.querySelectorAll('.hidden').forEach(
    el => observer.observe(el)
);
});

