from django.contrib import admin
from students.models import Student, StudentGroup


class StudentInline(admin.TabularInline):
    model = Student


class StudentGroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]

admin.site.register(Student)
admin.site.register(StudentGroup, StudentGroupAdmin)