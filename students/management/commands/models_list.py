from django.core.management.base import AppCommand
from students.models import Student, StudentGroup


class Command(AppCommand):
    requires_model_validation = True

    def handle_app(self, app, **options):
        groups = StudentGroup.objects.all()
        lines = []
        
        for studentgroup in groups(app):
            lines.append("[%s]\n" % studentgroup.title)
            for student in Student.objects.filter(group=studentgroup.id):
                lines.append("\t[%s]\n" % student.student_name(self))

        return "\n".join( lines )