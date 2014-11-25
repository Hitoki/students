from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView, DeleteView
from students.models import Student, StudentGroup
from students.form import AddStudentForm, AddGroupForm
from django.contrib.auth.forms import UserCreationForm


class StudentGroupView(ListView):
    model = StudentGroup
    template_name = 'index.html'


class StudentGroupDetailView(TemplateView):
    template_name = 'group_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StudentGroupDetailView, self).get_context_data(**kwargs)
        student = Student.objects.all().filter(group__pk=kwargs['pk'])
        context['students'] = student
        return context


class RegistrationView(TemplateView):
    template_name = 'registration/registration.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return self.render_to_response({'form': form})

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
        return self.render_to_response({'form': form})


class AddStudent(TemplateView):
    template_name = 'add_new_student.html'

    def get(self, request, *args, **kwargs):
        form = AddStudentForm()
        return self.render_to_response({'form': form})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddStudent, self).dispatch(*args, **kwargs)

    def post(self, request):
        form = AddStudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return self.render_to_response({'form': form})


class AddGroup(TemplateView):
    template_name = 'add_new_group.html'

    def get(self, request, *args, **kwargs):
        form = AddGroupForm()
        return self.render_to_response({'form': form})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddGroup, self).dispatch(*args, **kwargs)

    def post(self, request):
        form = AddGroupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return self.render_to_response({'form': form})


class EditStudent(TemplateView):
    template_name = 'edit_student.html'

    def get(self, request, *args, **kwargs):
        form = AddStudentForm()
        return self.render_to_response({'form': form})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditStudent, self).dispatch(*args, **kwargs)

    def post(self, request, student_id):
        form = AddStudentForm(data=request.POST, instanse=student_id)
        if form.is_valid():
            form.save()
            return redirect('/')
        return self.render_to_response({'form': form})


class EditGroup(TemplateView):
    template_name = 'edit_group.html'

    def get(self, request, *args, **kwargs):
        form = AddGroupForm()
        return self.render_to_response({'form': form})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditGroup, self).dispatch(*args, **kwargs)

    def post(self, request, studentgroup_id):
        form = AddGroupForm(data=request.POST, instanse=studentgroup_id)
        if form.is_valid():
            form.save()
            return redirect('/')
        return self.render_to_response({'form': form})


class StudentDelete(DeleteView):
    model = Student
    template_name = "student_confirm_delete"
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentDelete, self).dispatch(*args, **kwargs)


class GroupDelete(DeleteView):
    model = StudentGroup
    template_name = "group_confirm_delete"
    success_url = "index.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GroupDelete, self).dispatch(*args, **kwargs)