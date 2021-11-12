class  Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        #carrito = self.session.get["carrito"]
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito=carrito
    def agregar (self, producto):
        #id = str(producto.id)
        id = str(producto.producto)
        if id not in self.carrito.keys():
            self.carrito[id]={
                #ID y nombre no existen en la BD
                #"producto_id" : producto.id,
                #"nombre": producto.nombre,
                "producto_id" : producto.producto,
                "nombre": producto.tipo.__str__(),
                #"acumulado": producto.precio,
                "acumulado": float(producto.precio),
                "cantidad":1,
            }
            self.guardar_carrito()
        else:
            self.carrito[id]["cantidad"] += 1
            #self.carrito[id] ["acumulado"] += producto.precio
            self.carrito[id] ["acumulado"] += float(producto.precio)
            self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        #id = str(producto.id)
        id = str(producto.producto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        #id = str(producto.id)
        id = str(producto.producto)
        if id in self.carrito.keys():
            #elf.carrito["cantidad"] -= 1
            #self.carrito["acumulado"] -= producto.precio
            self.carrito[id]["cantidad"] -= 1
            #self.carrito[id]["acumulado"] -= producto.precio
            self.carrito[id]["acumulado"] -= float(producto.precio)
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar (self):
        self.session["carrito"] = {}
        self.session.modified = True






        