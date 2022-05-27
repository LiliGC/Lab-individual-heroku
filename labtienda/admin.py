from django.contrib import admin
from .models import Client, Professional, Comentario, Marca, Categoria, Producto, Orden, OrdenItem


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

class OrdenItemInline(admin.TabularInline):
    model = OrdenItem
    raw_id_fields = ['producto']

admin.site.register(OrdenItem)

class OrdenAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido','direccion','ciudad', 'pagada', 'creada',
                    'actualizada']
    list_filter = ['pagada', 'creada', 'actualizada']
    inlines = [OrdenItemInline]


admin.site.register(Orden, OrdenAdmin)