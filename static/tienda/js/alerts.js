//Alertas personalizadas.
  
//Se ejecuta cuando agregamos un producto.
function addAlert(articulo) {
    Swal.fire({
      title: "Agregado!",
      html: `Has agregado el artículo: <strong>${articulo}</strong>`,
      icon: "success",
      confirmButtonText: 'Aceptar',
      customClass: {
        htmlContainer: 'htmlContainer-class'
       },
      confirmButtonColor: 'blue'
     })
  }
      
  //Se ejecuta cuando no hay mas stock.
  function cantAlert() {
    swal.fire({
      title: "No hay mas stock!",
       text: "Por favor, elija otro artículo.",
       icon: "error",
       confirmButtonText: 'Aceptar',
       customClass: {
           htmlContainer: 'htmlContainer-class'
       },
      confirmButtonColor: 'blue'
    })
  } 

  function contactAlert() {
    Swal.fire({
      title: "Muchas gracias!",
      text: `Hemos enviado tus datos.`,
      confirmButtonText: 'Aceptar',
      customClass: {
        htmlContainer: 'htmlContainer-class'
    },
      confirmButtonColor: 'blue'
     }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          location.reload()
        )
      }
    })
  }

  export {
    addAlert, cantAlert, contactAlert
  }