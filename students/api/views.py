from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from students.api.serializers import UserSerializer, StudentSerializer, StudentGroupSerializer
from students.models import Student, StudentGroup


class UserView(ViewSet):

    def list(self, request):
        users = User.objects.all()

        data = UserSerializer(users, many=True).data
        return Response(data)


class StudentView(ViewSet):

    def list(self, request):
        students = Student.objects.all()
        data = StudentSerializer(students, many=True).data

        return Response(data)


class StudentGroupView(ModelViewSet):

    serializer_class = StudentGroupSerializer

    def get_queryset(self):
        return StudentGroup.objects.all()


