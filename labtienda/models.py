from django.db import models
import datetime
from django.utils.text import slugify



# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=25, verbose_name='Nombre')
    last_name=models.CharField(max_length=25, verbose_name='Apellido')
    birth_date=models.DateField(verbose_name='Fecha de nacimiento', help_text = "Usa el siguiente formato: <em>YYYY-MM-DD</em>.")
    phone=models.IntegerField(verbose_name='Teléfono')
    email=models.EmailField(max_length=254,unique=True, verbose_name='Email')
    address=models.CharField(max_length=100, verbose_name='Dirección', help_text = "Usa el siguiente formato: <em>Calle,número,Población,Comuna</em>.")

    class Meta:
        abstract:True

    def __str__(self):
        return '%s %s'% (self.name, self.last_name)

class Client(User):
    ci=models.CharField(max_length=10, unique=True, verbose_name= 'Run o Rut', help_text = "Usa el siguiente formato: <em>xxxxxxxx-x o xxxxxxxx-x</em>.")
    
class Professional(User):
    title=models.CharField(max_length=50,verbose_name= 'Título')
    ci=models.CharField(max_length=10, unique=True, verbose_name= 'Run')
    registration_date=models.DateField(default=datetime.date.today, verbose_name= 'Fecha de registro')
    

consultas=[
    [0, 'consulta'],
    [1, 'reclamo'],
    [2, 'sugerencia'],
    [3, 'felicitaciones']
]

class Comentario(models.Model):
    nombre= models.CharField(max_length=30)
    correo_electronico=models.EmailField(max_length=30)
    tipo_consulta=models.IntegerField(choices=consultas)
    mensaje=models.TextField()

    def __str__(self): 
        return self.nombre

class Marca(models.Model):
    nombre= models.CharField(max_length=30)

    def __str__(self): 
        return self.nombre

class Categoria(models.Model):
    nombre=models.CharField(max_length=50, db_index=True)
    slug=models.SlugField(max_length=50, db_index=True, unique=True)

    class Meta:
        ordering=('nombre',)
        verbose_name='categoría'
        verbose_name_plural='categorías'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self): 
        return self.nombre

class Producto(models.Model):
    categoria=models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50, db_index=True)
    slug=models.SlugField(max_length=50, db_index=True, unique=True)
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen=models.ImageField(upload_to='productos')
    descripción=models.TextField(blank=True)
    precio=models.IntegerField()
    stock=models.PositiveIntegerField()
    disponible=models.BooleanField(default=True)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('nombre',)
        index_together=(('id', 'slug'),)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.nombre)
        super(Producto, self).save(*args, **kwargs)

    def __str__(self): 
        return self.nombre
