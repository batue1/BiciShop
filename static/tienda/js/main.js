import { contactAlert } from "./alerts.js"

//Variables.
const main = document.body;
const mainBars = document.querySelector('#mainBars'),
      menu = document.querySelector('#mainMenu'),
      lupa = document.querySelector('.lupa'),
      buscador = document.querySelector('.buscador');


//Menu principal
mainBars.addEventListener('click', () => {

//Al hacer click en las barras, se agrega una nueva clase y aparece el menu.
  menu.classList.add('menuShow');
  main.classList.add('newBody');
  mainBars.classList.remove('bars');
  main.style.overflow="hidden"
})


//Al hacer click en las cruz o en un link, se elimina la clase agregada y desaparece el menu.
const close = () => {
  menu.classList.remove('menuShow');
  main.classList.remove('newBody');
  mainBars.classList.add('bars');
  main.style.overflow="auto"
}
document.querySelector('#newBar').addEventListener('click', close)


menu.addEventListener('click', (e) => {
  if(e.target.tagName === 'A'){   //Al seleccionar un link del menu, este se cierra.
    close()
  } 
})


const contactSend = () => {

  document.querySelector('#contact').addEventListener('submit', (e) => {

    e.preventDefault()
    document.querySelector('.send-form').style.display = "none"
    document.querySelector('#contactLoader').style.display = "block"

    //Hacemos POST en la api de formulario
    fetch(`https://formsubmit.co/ajax/7e77fc1b7e4412f9635f9c5bdd658a0a`, {
      method: "POST",
      body: new FormData(e.target)
    })
    .then(res => res.ok? res.json : Promise.reject(res))
    .then (json => { 
      contactAlert()
      // setTimeout(() => { location.reload() }, 2000); 
    })
    .catch(console.warn)
    
  })

}
  

//Función de búsqueda
const finder = () => {

  document.querySelector('#input').addEventListener('keyup', (e) => {      
    
    //Si la palabra/letra del input no coincide con el inner del producto, lo desaparece.
    document.querySelectorAll('.store__products--item').forEach(el =>  

      (el.textContent.toLowerCase().includes(e.target.value.toLowerCase())) 
      ? el.setAttribute("style", "visibility:visible; transform: scale(1);  transition: 0.5s;")
      : el.setAttribute("style", "visibility:hidden; transform: scale(0); order:1; transition: 0.5s;") 

      ) 

  })
  
}


const responsiveFinder = () => {

  lupa.addEventListener('click', () => {

    buscador.classList.add('showFinder')
    
  })
  document.querySelector('#closeFinder').addEventListener ('click' , () => {

    buscador.classList.remove('showFinder')
    

  })
  
}

contactSend();
finder();
responsiveFinder();



