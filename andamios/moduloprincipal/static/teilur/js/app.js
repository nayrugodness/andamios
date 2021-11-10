let btnmenu = document.querySelector('.btn-menu');
let menu = document.querySelector('.list-container');
let containermenu = document.querySelector('.menu');
let activador = true;

btnmenu.addEventListener('click', ()=>{
    btnmenu.classList.toggle('fa-times');
    if(activador){
        menu.style.left = '0%';
        menu.style.transition = '0.5s';
        activador = false;

    }else{
         activador = false;
        menu.style.left = '-100%';
        menu.style.transition = '0.5s';
        activador = true;
        

    };
});

let enlaces = document.querySelectorAll('.lists li a');

enlaces.forEach((element) =>{
    element.addEventListener('click', ()=>{
        enlaces.forEach((link)=>{
            link.classList.remove('activo');
        });
        event.target.classList.add('activo');
    });
});

let prevScrollPos = window.pageYOffset;
let goTop = document.querySelector('.go-top');

window.onscroll = ()=>{

    let currentScrollpos = window.pageYOffset;

    if(prevScrollPos > currentScrollpos){
        containermenu.style.top = "0";
        containermenu.style.transition = "0.5s";
    }else{
        containermenu.style.top = "-60px";
        containermenu.style.transition = "0.5s";
    };
    prevScrollPos = currentScrollpos;

    let arriba = window.pageYOffset;

    if (arriba <= 600){
        containermenu.style.borderBottom = "none";
        goTop.style.right = "-100%";
    }else{
        containermenu.style.borderBottom = "2px solid #ff2e63";
        goTop.style.right = "0";
        goTop.style.transition = "0.5s";
    }

}

goTop.addEventListener('click', () => {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
});

let verAbajo = document.querySelector('#abajo');

verAbajo.addEventListener('click', ()=>{
    document.body.scrollTop = 600;
    document.documentElement.scrollTop = 600;
});