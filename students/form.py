from django import forms
from students.models import Student, StudentGroup


class AddStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class AddGroupForm(forms.ModelForm):

    class Meta:
        model = StudentGroup
        fields = '__all__'
