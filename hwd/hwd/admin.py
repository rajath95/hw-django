from django.contrib import admin
from .models import Books,Feedback

class BooksAdmin(admin.ModelAdmin):
    list_display=[ field.name for field in Books._meta.get_fields() ]
    list_display.remove('price_currency')


admin.site.register(Books,BooksAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=[ field.name for field in Feedback._meta.get_fields() ]


admin.site.register(Feedback,FeedbackAdmin)
