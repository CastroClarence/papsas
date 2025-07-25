/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

/*===== MENU SHOW =====*/
/* Validate if constant exists */
if(navToggle){
    navToggle.addEventListener('click', () =>{
        navMenu.classList.add('show-menu')
    })
}

/*===== MENU HIDDEN =====*/
/* Validate if constant exists */
if(navClose){
    navClose.addEventListener('click', () =>{
        navMenu.classList.remove('show-menu')
    })
}

/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    // When we click on each nav__link, we remove the show-menu class
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    distance: '90px',
    duration: 3000,
})

sr.reveal(`.home__data`, {origin: 'top', delay: 400})
sr.reveal(`.feature-img`, {origin: 'top', delay: 400})
sr.reveal(`.officer_img`, {origin: 'top', delay: 400})
sr.reveal(`.resources`, {origin: 'top', delay: 400})
sr.reveal(`.memo`, {origin: 'top', delay: 400})
sr.reveal(`.services`, {origin: 'top', delay: 400})
sr.reveal(`.partners`, {origin: 'top', delay: 400})
sr.reveal(`.member-img`, {origin: 'top', delay: 400})
sr.reveal(`.membership`, {origin: 'top', delay: 400})
sr.reveal(`.video-papsas`, {origin: 'top', delay: 400})

