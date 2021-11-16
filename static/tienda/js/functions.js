import { addAlert, cantAlert } from './alerts.js'

//Variables.
const store = document.querySelector('.store__products'),
      carScreen = document.querySelector('#carScreen'),
      counter = document.querySelector('#counter'),
      modal = document.querySelector('.modal__container')
let carrito = [];  


//Mostrar carrito
const showCar = () => {
  document.querySelector('#car').addEventListener('click', () => {

  carScreen.classList.toggle('carShow');
  
  if(carScreen.classList.contains('carShow')) {
    document.body.style.overflowY = "hidden"
  } else {
    document.body.style.overflowY = "auto"
  }
})
}


//Function  que muestra el modal.
const modalCar = () => {
  
  document.querySelector('.checkout-class').addEventListener ('click', (e) => {
  
    
      carScreen.classList.remove('carShow');  //Cerramos el carrito al abrir el modal.
      modal.classList.add('modalShow') 
    

    document.querySelector('#modalClose').addEventListener('click', () => { 
      modal.classList.remove('modalShow')
      document.body.style.overflowY = "auto"
   })
  
  })
  
}


//Formulario de compra.
const formSend = () => {

  const inputNombre = formulario.nombre
  const inputEmail = formulario.email

  document.querySelector('#formulario').addEventListener('submit', (e) => {

    e.preventDefault()
    document.querySelector('.total-button').style.display = "none"
    document.querySelector('#dataLoader').classList.add('loader-show') 

    //Hacemos POST en la api de formulario
    fetch(`https://formsubmit.co/ajax/7e77fc1b7e4412f9635f9c5bdd658a0a`, {
      method: "POST",
      body: new FormData(e.target)
    })
    .then(res => res.ok? res.json : Promise.reject(res))
    .then(json => { 
      message(inputNombre, inputEmail)   
    })
    .catch(console.warn)
    
  })

}


//Mensaje de compra.
const message = (inputNombre, inputEmail) => {
  
  //Aparece el mensaje de compra.
  const checkoutModal = document.querySelector('.checkout-modal')
  const template = document.querySelector('#template').content
  const fragment = document.createDocumentFragment()

  template.querySelector('#nameSpan').textContent = inputNombre.value
  template.querySelector('#emailSpan').textContent = inputEmail.value

  //Creamos un fragmento con el conenido del template(mensaje de compra).
  let clone = document.importNode(template, true) 
  fragment.appendChild(clone)

  //Intercambiamos el contenido del formulario por el del mensaje.
  checkoutModal.innerHTML = ""
  checkoutModal.appendChild(fragment)

  setTimeout(() => {
    document.querySelector('.checked').style.opacity = 1
  },500)

  document.querySelector('#formClose').addEventListener('click' , () => {
    location.reload()
  })

}


const loadhtml = () => {
  let cartItems =  JSON.parse(sessionStorage.getItem('productsInCart'));
  let cartCost = parseInt(sessionStorage.getItem("totalCost"))

  //Hace aparecer a los productos seleccionados en el carrito.
  if (cartItems && carScreen) {
    carScreen.innerHTML = ` 
                              <h2>Agregue productos aquí...</h2>
                              <div class="checkout-class">
                                <button id="s" style="border: none; cursor: pointer">
                                  <h3 style="color: rgb(243, 237, 237)">Ir al checkout</h3>
                                </button>
                              </div>
                              <h3 id="total" style="color: black">Total: $0</h3>
                              <hr />
                          `

    Object.values(cartItems).map(item => {
      
      carScreen.innerHTML +=  `
                                <div class = "carrito-div">
                                  <img class= "carrito-img" src="./assets/images/products/${item.id}.jpg" alt="">
                                  <p class = "carrito-p">${item.name}
                                    <br />
                                    $${item.price}
                                    x${item.inCart}
                                    <br />
                                    <span class = "carrito-price">$${item.inCart * item.price}<span>       
                                    <br />
                                  <p>                                           
                                  <button><i id = "${item.price}" class="fas fa-times-circle fa-2x removeIcon"></i></button>              
                                </div>
                                `
                                
      document.querySelector('.checkout-class').style.display = "block" 
      
      //Dibujamos el total.
      document.querySelector('#total').textContent = `Total: $${ cartCost  }`   //Pintamos el total en el carrito y en el modal del checkout.                       
      document.querySelector('#formTotal').textContent = `Total: $${ cartCost  }` 
                                
    })

  }
}


//Función que dibuja el total.
const totalCalc = (dt) => { 
  let cartItems = JSON.parse(sessionStorage.getItem('productsInCart'));
  let cart = sessionStorage.getItem("totalCost");

  if(cart != null) {
    
    cart = parseInt(cart);
    sessionStorage.setItem("totalCost", cart + cartItems[dt.id].price);
    
  } else {
    sessionStorage.setItem("totalCost", cartItems[dt.id].price);
  }

formSend()
}


//Guardamos los artículos agregados al storage.
const cartStorage = (dt) => {
  
  let cartItems = JSON.parse(sessionStorage.getItem('productsInCart'))
        
  if(cartItems != null) {

      cartItems = {
        ...cartItems,
        [dt.id]: dt
      }
    
    cartItems[dt.id].inCart += 1

  } else {

    dt.inCart = 1
    cartItems = {
      [dt.id]: dt
    }

  }

  sessionStorage.setItem('productsInCart', JSON.stringify(cartItems))

}


//Función para eliminar artículos del carrito.
const removeItem = (dt) => {

  carScreen.addEventListener('click', (e) => {
    let element = e.target.parentElement.parentElement.parentElement
    let cartItems =  JSON.parse(sessionStorage.getItem('productsInCart'));

    cartItems = {
        ...cartItems,
        [dt.id]: dt
      }

    if(e.target.id == dt.price) {
  
      for ( let i = 0; i < carrito.length; i++) {

        //Detectamos que el id del target sea igual al precio del array del carrito y eliminamos ese precio.
        if (e.target.id == carrito[i]  ) {
          carrito.splice(i , 1)
          
          sessionStorage.setItem('cart', carrito.length);
          let productNumbers = parseInt(sessionStorage.getItem("cart"));
          counter.textContent = productNumbers 

          let total = carrito.reduce((a, b) => a + b, 0) //Calculamos de vuelta el total despues de eliminar un producto.
          
          sessionStorage.setItem('totalCost', total)
          let cartCost = JSON.parse(sessionStorage.getItem('totalCost'))
          
          document.querySelector('#total').textContent = `Total: $${ cartCost  }`  
          document.querySelector('#formTotal').textContent = `Total: $${ cartCost  }`
        }

        if(carrito.length == 0) {
          document.querySelector('.checkout-class').style.display = "none" 
        }

      }      
      cartItems[dt.id].inCart = 0
      delete cartItems[dt.id]   
      sessionStorage.setItem('productsInCart', JSON.stringify(cartItems))

    }
    carScreen.removeChild(element) //Finalmente desaparecemos el producto.

  })

}


const addCartFunction = () => {
  
  let productNumbers = parseInt(sessionStorage.getItem("cart"));  //Almacenamos el valor del storage. 

  if(productNumbers){
    sessionStorage.setItem('cart', productNumbers + 1); //Si ya existe el valor, al hacer click, se suma uno.
    counter.textContent = productNumbers + 1
  } else{
    sessionStorage.setItem('cart', 1);  //Obtenemos del storage la cantidad 1 en el carrito al crear el storage.
    counter.textContent = 1;
  }
}
  

//Función que restan el stock del producto.
    
const stockSub = (dt) => {
  let cartItems =  JSON.parse(sessionStorage.getItem('productsInCart'));

    cartItems = {
        ...cartItems,
        [dt.id]: dt
      }
  cartItems[dt.id].stock -= 1
  sessionStorage.setItem('productsInCart', JSON.stringify(cartItems))
}; 


//Agrega al carrito al hacer click.
const buyEvent = (dt) => {
  
  
  store.addEventListener('click', (e) =>{
    if(e.target.id == dt.id){ 
      
      if (dt.stock > 0) {
        carrito.push(dt.price)
        sessionStorage.setItem('carrito', JSON.stringify(carrito))
        
        addAlert(dt.name);
        stockSub(dt)  
        cartStorage(dt)
        addCartFunction(dt) 
        removeItem(dt)
        totalCalc(dt)
        loadhtml(dt)
        modalCar()
        
      } else {
        cantAlert();
        throw 'No hay mas stock!';
      } 
      
    } 
  })
  
}
     

  export {
    showCar, 
    buyEvent,
  }