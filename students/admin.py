from django.contrib import admin
from students.models import Student, StudentGroup, Log


class StudentInline(admin.TabularInline):
    model = Student


class StudentGroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]


class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'add_date', 'log', 'model')
    search_fields = ('log', )
    list_filter = ('add_date',)
    list_display_links = ('add_date',)

admin.site.register(Student)
admin.site.register(StudentGroup, StudentGroupAdmin)
admin.site.register(Log, LogAdmin)