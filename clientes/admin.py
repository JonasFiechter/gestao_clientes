from django.contrib import admin
from .models import Person, Documento, Venda, Produto

class PersonAdmin(admin.ModelAdmin):
    # fields = ('first_name', 'last_name', 'salary', 'bio', 'photo')
    fieldsets = (
        ('Personal data:', {'fields': ('first_name', 'last_name')}),
        ('Other data:', {'fields': ('age', 'salary', 'photo')}),
    )
    list_display = ('first_name', 'last_name', 'salary', 'bio', 'photo')
    list_filter = ('first_name')

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
