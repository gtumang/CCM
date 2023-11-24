// document.addEventListener('DOMContentLoaded', function() {

//     as = document.querySelectorAll('input')

//     for (a of as) {

//         a.addEventListener('click', function(event) {

//             // Obtém o elemento que foi clicado. Não podemos
//             // usar a variável "a" diretamente aqui dentro,
//             // pois o valor dela muda ao longo do loop.
//             t = event.currentTarget

//             value = t.querySelector('.block__item value')
//             localStorage.setItem('valor', value.innerHTML)

//         })

//     }

// })

document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById('Btn_enable');
    var enable;
    function mudatexto(){
        if(localStorage.getItem('enable')!=null){
            enable = !(localStorage.getItem('enable'));
        }else{
            enable = true;
        }
        localStorage.setItem('enable',enable);

        console.log(enable);
        localStorage.setItem('btn',btn)
        if(enable = false){
            localStorage.setItem('continua', enable)
            btn.value = 'EN';
        }else{
            localStorage.setItem('pum', enable)
            btn.value = "DIS";
        }
        // btn.addEventListener('click', function handleClick() {
        //     if(btn=="EN"){
        //         btn.textContent = 'DIS';
        //     }
        //     if(btn=="HO"){
        //         btn.textContent = 'AH';
        //     }
        // })
    };
});
