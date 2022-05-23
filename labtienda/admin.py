from django.contrib import admin
from .models import Client, Professional, Comentario, Marca, Categoria, Producto

# Register your models here.

admin.site.register(Client)
admin.site.register(Professional)
admin.site.register(Comentario)
admin.site.register(Marca)

class CategoriaAdmin(admin.ModelAdmin):
    list_display=['nombre', 'slug']
    prepopulated_fields={'slug': ('nombre',)}

admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre','categoria', 'marca', 'precio', 'stock','disponible', 'creado', 'actualizado']
    list_filter=['marca','categoria']
    list_editable=['precio', 'stock']
    search_fields=['nombre']
    prepopulated_fields={'slug': ('nombre',)}


admin.site.register(Producto, ProductoAdmin)

