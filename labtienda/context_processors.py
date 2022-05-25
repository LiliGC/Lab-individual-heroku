from .carro import Carro

def carro(request):
	return {'carro': Carro(request)}