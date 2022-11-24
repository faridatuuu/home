let body = document.querySelector('body')
let fazzy = document.querySelector('.fazzy')
let icon = document.querySelector('.bi-moon-stars-fill')

fazzy.addEventListener('click', ()=>{
    body.classList.toggle('dark')
    if(body.classList.contains('dark')){
        icon.classList.replace('bi-moon-stars-fill','bi-brightness-high-fill')
    }
    else{
        icon.classList.replace('bi-brightness-high-fill','bi-moon-stars-fill')
    }
})


