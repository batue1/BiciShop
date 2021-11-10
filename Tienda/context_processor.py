def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if 'carro' in request.session:
        #if request.session["carrito"]:
            for key, value in request.session["carrito"].itemns():
                total += int(value["acumulado"])

    return {"total_carrito":total}

    