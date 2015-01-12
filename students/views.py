from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.views.generic.base import TemplateView, View
from students.models import Student, StudentGroup
from students.form import AddStudentForm, AddGroupForm, EmailUserCreationForm


class StudentGroupView(TemplateView):
    template_name = 'ng/index.html'

# url(r'^page/(?P<page_name>[-\w]+)', PageView.as_view()),
class PageView(View):

    def get(self, request, page_name):
        template_name = "ng/{}.html".format(page_name)
        return render_to_response(template_name)

class StudentGroupDetailView(DetailView):
    model = StudentGroup
    template_name = 'group_detail.html'


class StudentProfileView(DetailView):
    model = Student
    template_name = 'student_detail.html'


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    model = User
    form_class = EmailUserCreationForm
    success_url = reverse_lazy('login')


class AddStudent(CreateView):
    template_name = 'add_new_student.html'
    model = Student
    form_class = AddStudentForm
    success_url = reverse_lazy('index')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddStudent, self).dispatch(*args, **kwargs)


class AddGroup(CreateView):
    template_name = 'add_new_group.html'
    model = StudentGroup
    form_class = AddGroupForm
    success_url = reverse_lazy('index')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddGroup, self).dispatch(*args, **kwargs)


class StudentUpdate(UpdateView):
    form_class = AddStudentForm
    model = Student
    template_name = "edit_student.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentUpdate, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        studentgroup_id = self.object.group.id
        return reverse('group_detail', args=(studentgroup_id, ))


class GroupUpdate(UpdateView):
    model = StudentGroup
    template_name = "edit_group.html"
    success_url = reverse_lazy('index')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GroupUpdate, self).dispatch(*args, **kwargs)


class StudentDelete(DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentDelete, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        studentgroup_id = self.object.group.id
        return reverse('group_detail', args=(studentgroup_id, ))


class GroupDelete(DeleteView):
    model = StudentGroup
    template_name = "group_confirm_delete.html"
    success_url = reverse_lazy('index')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GroupDelete, self).dispatch(*args, **kwargs)
