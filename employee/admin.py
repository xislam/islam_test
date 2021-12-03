from django.contrib import admin

# Register your models here.
from employee.models import Employers, Department, ProgrammingLanguage

admin.site.register(Employers)
admin.site.register(Department)
admin.site.register(ProgrammingLanguage)