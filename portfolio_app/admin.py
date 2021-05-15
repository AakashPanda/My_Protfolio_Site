from django.contrib import admin

# Register your models here.

from . models import projects,certificate,Contacts,Blogs

class adminpage(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
    list_filter = ('title',)

admin.site.register (projects, adminpage)
admin.site.register(certificate)
admin.site.register(Contacts)
admin.site.register (Blogs)