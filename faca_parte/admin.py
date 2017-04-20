from django.contrib import admin
from models import Person, Role, Schooling


admin.site.register(Role)
admin.site.register(Schooling)

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['full_name', 'email', 'birth', 'schooling', 'zipcode', 'street', 'district', 'city', 'state',
                       'select_role', 'note']
        }),
    )
    search_fields = ['full_name', 'email']
    list_display = ('full_name', 'email', 'select_role')
    list_display_links = ('full_name', )

admin.site.register(Person, PersonAdmin)
