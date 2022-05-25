from decimal import Decimal
from django.conf import settings
from .models import Producto
from proyecto1.settings import CARRO_SESSION_ID

# Create your models here.

class Carro(object):
    def __init__(self, request):
        self.request=request
        self.session = request.session
        carro = self.session.get(settings.CARRO_SESSION_ID)
        if not carro:
            carro = self.session[settings.CARRO_SESSION_ID] = {}
        self.carro = carro

    def agregar(self, producto, cantidad=1, actualizar_cantidad=False):
        producto_id = str(producto.id)
        if producto_id not in self.carro:
            self.carro[producto_id] = {'cantidad': 0, 'precio': str(producto.precio)}
        if actualizar_cantidad:
            self.carro[producto_id]['cantidad'] = cantidad
        else:
            self.carro[producto_id]['cantidad'] += cantidad
        self.save()

    def save(self):
        self.session[settings.CARRO_SESSION_ID] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.save()

    def __iter__(self):
        producto_ids = self.carro.keys()
        productos = Producto.objects.filter(id__in=producto_ids)
        for producto in productos:
            self.carro[str(producto.id)]['producto'] = producto

        for item in self.carro.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        return sum(item['cantidad'] for item in self.carro.values())

    def get_precio_total(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carro.values())

    def limpiar(self):
        del self.session[settings.CARRO_SESSION_ID]
        self.session.modified = True