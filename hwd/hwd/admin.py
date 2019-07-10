from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display=[ field.name for field in Books._meta.get_fields() ]
    list_display.remove('price_currency')


admin.site.register(Books,BooksAdmin)
