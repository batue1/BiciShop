import  {showCar, buyEvent} from './functions.js'
import { queryFunction } from './query.js'


//Creamos los elementos que iran adentro de la tienda.
const create = (dt) => {

  let html =  `
                        <div class="store__products--item" id="${dt.id}" category="${dt.cat}">
                          <img class="imgClass" src="./assets/images/products/${dt.id}.jpg">
                          <p class="product-name"> <span>${dt.name}</span> <br> <span class = "price">$${dt.price}</span></p>
                          <div class="card-container">${dt.desc}
                            <hr>
                            <i class="addCart fas fa-cart-plus fa-3x" id="${dt.id}"></i>
                          </div>
                        </div>
                      ` 

  document.querySelector('.store__products').innerHTML += html

 buyEvent(dt)
 
}


//Crear un nuevo producto.
const getALL = async () => {
  const URLJSON  = "https://my-json-server.typicode.com/nicojoaquin/fakeAPI/articulos"
  
  //Create
  const createApi = () => {
    let options = {
      method: 'POST',
      body: JSON.stringify({
        id: 'redragon',
        name: 'Headset Redragon',
        price: 5400,
        cat: 'headsets',
        stock: 7,
        desc: "Auriculares ecónomicos de excelente calidad.",
      }),
      headers: {
      'Content-type': 'application/json; charset=UTF-8',
      }
    }
  
    fetch(URLJSON, options)
    .then((resp) => resp.json())
    .then( data => {
      create(data)
      queryFunction()   
    
    });

  }


//Llamando a mi "API" de productos.
  //Read
  try {

    await fetch(URLJSON)
    .then(async resp => await  resp.json())
    .then( data => {
      createApi()
      data.map(dt => {
        create(dt)      
      }) 
    })
    
  }
  catch (error) {
    console.warn(error)
  }
}


document.addEventListener('DOMContentLoaded', getALL)
showCar();

window.onbeforeunload = (e) => {
  sessionStorage.clear()
};
