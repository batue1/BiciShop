//Responsive menu 
$('#nav__hamburger').click(function () {
  $('.store__category').slideToggle(); //Se desplaza el menu
  
  if($('#ham').attr('class') == 'uil uil-bars'){     //Cambia icono al pulsar el boton
    $('#ham').removeClass('uil uil-bars').addClass('uil uil-arrow-up');
  } else {
    $('#ham').removeClass('uil uil-arrow-up').addClass('uil uil-bars');
  } 
  
  
  $('.store__category--item').click(function(){
    $('.store__category').slideUp();
    $('#ham').removeClass('uil uil-bars').addClass('uil uil-arrow-up'); //Cambia icono y cierra el menu al pulsar el link
    $('#ham').removeClass('uil uil-arrow-up').addClass('uil uil-bars');
  })
})

//Eventos de links
const queryFunction = () => {

  const item = $('.store__category--item');
  const products = $('.store__products--item');
  const showAll = $('.store__category--item[category="all"]');

  showAll.addClass('active');

  item.click(function(){
    let catProduct = $(this).attr('category');

    //Cambia color de los links.
    item.removeClass('active');
    $(this).addClass('active');

    //Oculta todos los productos.
    products.hide();
    products.css('transform', 'scale(0)');
    
    //Muestra cada producto. 
    $(`.store__products--item[category=${catProduct}]`).show();
    $(`.store__products--item[category=${catProduct}]`).css('transform', 'scale(1)');  
  })

  //Muestra todos los productos.
  showAll.click(function(){ 
    products.show();
    products.css('transform', 'scale(1)');  
  })

}

export {
  queryFunction
}



