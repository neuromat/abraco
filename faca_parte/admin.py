from copy import deepcopy
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin, BlogCategoryAdmin
from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.forms.admin import FormAdmin
from mezzanine.forms.models import Form
from mezzanine.galleries.admin import GalleryAdmin
from mezzanine.galleries.models import Gallery
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import RichTextPage

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


# add fields "video" and "news" to blog subclasses in the admin
blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"] += ("video", "news")


class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets

admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)


class MyBlogCategoryAdmin(BlogCategoryAdmin):
    fieldsets = ((None, {"fields": ("title", "slug")}),)

admin.site.unregister(BlogCategory)
admin.site.register(BlogCategory, MyBlogCategoryAdmin)


# add the field "home" to page subclasses in the admin
page_fieldsets = deepcopy(PageAdmin.fieldsets)
page_fieldsets[0][1]["fields"] += ("home",)
PageAdmin.fieldsets = page_fieldsets
GalleryAdmin.fieldsets = page_fieldsets

form_fieldsets = deepcopy(FormAdmin.fieldsets)
form_fieldsets[0][1]["fields"] += ("home",)
FormAdmin.fieldsets = form_fieldsets

admin.site.unregister(Form)
admin.site.register(Form, FormAdmin)
admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)
admin.site.unregister(RichTextPage)
admin.site.register(RichTextPage, PageAdmin)
