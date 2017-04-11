from django.contrib import admin
from models import Interest, Person, Schooling


admin.site.register(Interest)
admin.site.register(Schooling)

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['full_name', 'email', 'birth', 'schooling', 'zipcode', 'street', 'district', 'city', 'state',
                       'select_interest', 'note']
        }),
    )
    search_fields = ['full_name', 'email']
    list_display = ('full_name', 'email', 'select_interest')
    list_display_links = ('full_name', )

admin.site.register(Person, PersonAdmin)
