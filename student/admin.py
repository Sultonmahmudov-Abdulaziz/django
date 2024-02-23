from django.contrib import admin
from student.models import Student,Category
# Register your models here.

admin.site.register([Student, Category])