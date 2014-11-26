from django import forms
from django.contrib.auth.models import User
from students.models import Student, StudentGroup


class AddStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['user']


class AddGroupForm(forms.ModelForm):

    class Meta:
        model = StudentGroup
        fields = ['title']


class EditGroupForm(forms.ModelForm):

    class Meta:
        model = StudentGroup

