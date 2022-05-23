from django import forms
from .models import Client, Professional, Comentario, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = ('ci','name','last_name', 'birth_date', 'phone', 'email', 'address')

class ProfessionalForm(forms.ModelForm):

	class Meta:
		model = Professional
		fields=('title','name', 'last_name', 'ci', 'birth_date', 'phone', 'email', 'address', 'registration_date')


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class ComentarioForm(forms.ModelForm):
    class Meta:
        model=Comentario
        fields=['nombre', 'correo_electronico', 'tipo_consulta', 'mensaje']    

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['categoria', 'nombre', 'marca', 'imagen', 'descripción','precio', 'stock']   