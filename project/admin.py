from django.contrib import admin

# Register your models here.

#AGREGAR MODELOS DE APP project
from .models import Project, Role, ProjectMember, ProjectPermit

admin.site.register(Project)

#Hacer que projectmember tenga un selector de roles en el admin
class ProjectMemberAdmin(admin.ModelAdmin):
    search_fields = ('userId',)
    ordering = ('userId',)

admin.site.register(ProjectMember, ProjectMemberAdmin)
admin.site.register(ProjectPermit)

# Agregar filter horizontal a role con projectpermit

class RoleAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('projectPermit',)
admin.site.register(Role, RoleAdmin)

