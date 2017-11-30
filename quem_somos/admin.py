from django.contrib import admin

from models import Person


class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['name', 'bio', 'lattes', 'photo', 'coordination']
        }),
    )
    search_fields = ['name',]
    list_display = ('name', 'bio', 'lattes',)
    list_display_links = ('name', )

admin.site.register(Person, PersonAdmin)
