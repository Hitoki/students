from django import forms
from django.contrib.auth.forms import UserCreationForm
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
        fields = '__all__'


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email address', max_length=75)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("This email address already exists.")
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.is_active = True  # change to false if using email activation
        if commit:
            user.save()

        return user
