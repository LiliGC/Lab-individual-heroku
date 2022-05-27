from django.shortcuts import render, redirect, get_object_or_404

from labtienda.admin import OrdenItemInline
from .models import Client, Professional, Comentario, Producto, OrdenItem, Orden
from .forms import ClienteForm,ProfessionalForm, ComentarioForm, ProductoForm, OrdenCreateForm
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages 
from .carro import Carro
from .forms import CarroAddProductForm

# Create your views here.
def index(request):

    return render(request,'labtienda/index.html')

@staff_member_required
@login_required
def clientes(request):

    client=Client.objects.all()

    context = { 

    'clientes': client, 

    } 
    return render(request,'labtienda/clientes.html', context)

@staff_member_required
@login_required
def profesional(request):

    profesional=Professional.objects.all()

    context = { 

    'professionals': profesional, 

    } 
    return render(request,'labtienda/profesional.html', context)


@staff_member_required
@login_required
def registro_cliente(request):

    form=ClienteForm() 

    if request.method == 'POST': 

        form = ClienteForm(request.POST)

        if form.is_valid(): 
            cliente=Client()
            cliente.ci=form.cleaned_data["ci"]
            cliente.name=form.cleaned_data["name"]
            cliente.last_name=form.cleaned_data["last_name"]
            cliente.birth_date=form.cleaned_data["birth_date"]
            cliente.phone=form.cleaned_data["phone"]
            cliente.email=form.cleaned_data["email"]
            cliente.address=form.cleaned_data["address"]
            cliente.save()
            messages.success(request, 'Los datos han sido guardados satisfactoriamente') 
            return redirect('clientes') 

        else: messages.error(request,'Inválido') 

        return redirect('cliente_registro') 

    else: 

        form=ClienteForm()  

        return render(request, 'labtienda/cliente_registro.html', {"form":form}) 

@staff_member_required
@login_required
def registro_professional(request):

    form=ProfessionalForm() 

    if request.method == 'POST': 

        form = ProfessionalForm(request.POST)

        if form.is_valid(): 
            profesional=Professional()
            profesional.title=form.cleaned_data["title"]
            profesional.ci=form.cleaned_data["ci"]
            profesional.name=form.cleaned_data["name"]
            profesional.last_name=form.cleaned_data["last_name"]
            profesional.birth_date=form.cleaned_data["birth_date"]
            profesional.phone=form.cleaned_data["phone"]
            profesional.email=form.cleaned_data["email"]
            profesional.address=form.cleaned_data["address"]
            profesional.save()
            messages.success(request, 'Los datos han sido guardados satisfactoriamente') 
            return redirect('profesional') 

        else: messages.error(request,'Inválido') 

        return redirect('registro_profesional') 

    else: 

        form=ProfessionalForm()  

        return render(request, 'labtienda/registro_profesional.html', {"form":form}) 

@staff_member_required
@login_required
def profesional_edit(request,pk):
    profesional = get_object_or_404(Professional, pk=pk)
    if request.method == "POST":
        form = ProfessionalForm(request.POST, instance=profesional)
        if form.is_valid():
            profesional = form.save(commit=False)
            profesional.save()
            messages.success(request, 'El profesional se ha modificado con éxito')
            return redirect('profesional')
    else:
        form = ProfessionalForm(instance=profesional)
    return render(request, 'labtienda/profesional_edit.html', {'form': form})

@staff_member_required
@login_required
def profesional_delete(request,pk):
    profesional = get_object_or_404(Professional, pk=pk)
    profesional.delete()
    messages.success(request, 'El profesional se ha eliminado con exito')        
    return redirect('profesional')

@staff_member_required
@login_required
def cliente_edit(request,pk):
    cliente = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            messages.success(request, 'El cliente se ha modificado con éxito')
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'labtienda/cliente_edit.html', {'form': form})

@staff_member_required
@login_required
def cliente_delete(request,pk):
    cliente = get_object_or_404(Client, pk=pk)
    cliente.delete()
    messages.success(request, 'El cliente se ha eliminado con exito')        
    return redirect('clientes')


def register_user(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro exitoso." )
			return redirect('index')
		messages.error(request, "Registro no exitoso. Información no válida.")
	form = NewUserForm()
	return render (request, 'labtienda/register_user.html', context={"register_form":form})

def login_user(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Tu haz iniciado sesión como {username}.")
				return redirect('index')
			else:
				messages.error(request,"Nombre o contraseña no válidos.")
		else:
			messages.error(request,"Nombre o contraseña no válidos.")
	form = AuthenticationForm()
	return render(request, 'labtienda/login.html',context={"login_form":form})

@login_required
def logout_user(request):
	logout(request)
	messages.info(request, "Haz cerrado sesión exitosamente.") 
	return redirect('index')


def comentario(request):

    form=ComentarioForm()

    if request.method == 'POST':
		
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario=Comentario()
            comentario.nombre=form.cleaned_data["nombre"]
            comentario.correo_electronico=form.cleaned_data["correo_electronico"]
            comentario.tipo_consulta=form.cleaned_data["tipo_consulta"]
            comentario.mensaje=form.cleaned_data["mensaje"]
            comentario.save()
            messages.success(request, 'Su  mensaje ha sido enviado satisfactoriamente, nos pondremos en contacto con usted.')
        else: messages.error('Inválido')
        return redirect('index')
    else:
        form=ComentarioForm() 
        return render(request, 'labtienda/comentario.html', {"form":form}) 

@login_required
def listacomentarios(request):

    comentarios=Comentario.objects.all()

    context = { 

    'comentarios': comentarios, 

    } 
    return render(request,'labtienda/listacomentarios.html', context)

@login_required
def miscomentarios(request):

    email=request.user.email
    micomentario=Comentario.objects.filter(correo_electronico=email).all()

    context = { 

    'comentarios': micomentario, 

    } 
    return render(request,'labtienda/miscomentarios.html', context)

@login_required
def comentario_edit(request,pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.save()
            messages.success(request, 'Su mensaje se ha modificado con éxito')
            return redirect('listacomentarios')
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'labtienda/comentario_edit.html', {'form': form})

@login_required
def comentario_delete(request,pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.delete()
    messages.warning(request, 'Tu no podrás revertir esto!')        
    return redirect('listacomentarios')

@staff_member_required
@login_required
def registro_producto(request):

    form=ProductoForm() 

    if request.method == 'POST': 

        form = ProductoForm(request.POST, request.FILES)

        if form.is_valid(): 
            producto=Producto()
            producto.categoria=form.cleaned_data["categoria"]
            producto.nombre=form.cleaned_data["nombre"]
            producto.marca=form.cleaned_data["marca"]
            producto.imagen=form.cleaned_data["imagen"]
            producto.descripcion=form.cleaned_data["descripcion"]
            producto.precio=form.cleaned_data["precio"]
            producto.stock=form.cleaned_data["stock"]
            producto.save()
            messages.success(request, 'Los datos han sido guardados satisfactoriamente') 
            return redirect('productos') 

        else: messages.error(request,'Inválido') 

        return redirect('registro_productos') 

    else: 

        form=ProductoForm()  

        return render(request, 'labtienda/registro_productos.html', {"form":form}) 

@staff_member_required
@login_required
def productos_edit(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            messages.success(request, 'El producto se ha modificado con éxito')
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'labtienda/productos_edit.html', {'form': form})

@staff_member_required
@login_required
def productos_delete(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    messages.success(request, 'El producto se ha eliminado con exito')        
    return redirect('productos')

@staff_member_required
@login_required
def productos(request):

    producto=Producto.objects.all()

    context = { 

    'productos': producto, 

    } 
    return render(request,'labtienda/productos.html', context)

@login_required
def catalogo_productos(request):
    producto = Producto.objects.all()
    context = { 
    'productos': producto,  
    } 
    return render(request,'labtienda/catalogo_productos.html', context)

@login_required
def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    carro_producto_form = CarroAddProductForm()
    context = {
        'producto': producto,
        'carro_producto_form': carro_producto_form
    }
    return render(request, 'labtienda/producto_detalle.html', context)

@require_POST
def carro_agregar(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    form = CarroAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        carro.agregar(producto=producto, cantidad=cd['cantidad'], actualizar_cantidad=cd['actualizar'])
    return redirect('carro_detalle')

def carro_eliminar(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.eliminar(producto)
    return redirect('carro_detalle')

def carro_detalle(request):
    carro = Carro(request)
    for item in carro:
        item['actualizar_cantidad_form'] = CarroAddProductForm(initial={'cantidad': item['cantidad'], 'actualizar': True})
    return render(request, 'labtienda/carro_detalle.html', {'carro': carro})

def orden_creacion(request):
    carro= Carro(request)
    form = OrdenCreateForm()
    if request.method == 'POST':
        form = OrdenCreateForm(request.POST)
        if form.is_valid():
            orden= Orden()
            orden.nombre=form.cleaned_data["nombre"]
            orden.apellido=form.cleaned_data["apellido"]
            orden.email=form.cleaned_data["email"]
            orden.direccion=form.cleaned_data["direccion"]
            orden.ciudad=form.cleaned_data["ciudad"]
            orden.save()
            messages.success(request, 'La orden se ha creado con éxito')       
            for item in carro:
                OrdenItem.objects.create(
                    orden=orden,
                    producto=item['producto'],
                    precio=item['precio'],
                    cantidad=item['cantidad']
                )
            carro.limpiar()
            return render(request, 'labtienda/checkout.html', {'orden': orden})
    else:
        context = {
        'form': form,
        'carro': carro
    }
    return render(request, 'labtienda/orden_creacion.html', context)


