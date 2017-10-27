from django.contrib import admin

# Register your models here.
from .models import employees, project, projectEmployee

admin.site.register(employees)
admin.site.register(project)
admin.site.register(projectEmployee)
