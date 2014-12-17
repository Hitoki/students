from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from students.api.serializers import UserSerializer


class UserView(ViewSet):

    def list(self, request):
        users = User.objects.all()

        data = UserSerializer(users, many=True).data
        return Response(data)