from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, UpdateView
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
        student = Student.objects.filter(group__pk=kwargs['pk'])
        context['students'] = student
        return context


class StudentProfileView(DetailView):
    model = Student
    template_name = 'student_detail.html'


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


# class EditStudent(TemplateView):
#     template_name = 'edit_student.html'
#
#     def get(self, request, *args, **kwargs):
#         form = AddStudentForm()
#         return self.render_to_response({'form': form})
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(EditStudent, self).dispatch(*args, **kwargs)
#
#     def post(self, request, student_id):
#         student = get_object_or_404(Student.objects, id=student_id)
#         form = AddStudentForm(data=request.POST, instanse=student)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         return self.render_to_response({'form': form, 'student': student})
#
#
# class EditGroup(TemplateView):
#     template_name = 'edit_group.html'
#
#     def get(self, request, *args, **kwargs):
#         form = AddGroupForm()
#         return self.render_to_response({'form': form})
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(EditGroup, self).dispatch(*args, **kwargs)
#
#     def post(self, request, studentgroup_id):
#         form = AddGroupForm(data=request.POST, instanse=studentgroup_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         return self.render_to_response({'form': form})

class StudentUpdate(UpdateView):
    model = Student
    template_name = "edit_student.html"
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentUpdate, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentUpdate, self).get_context_data(**kwargs)
        context['student_update'] = reverse('student_edit',
                                            kwargs={'pk': self.get_object().id})

        return context


class GroupUpdate(UpdateView):
    model = StudentGroup
    template_name = "edit_group.html"
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GroupUpdate, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GroupUpdate, self).get_context_data(**kwargs)
        context['group_update'] = reverse('group_edit',
                                            kwargs={'pk': self.get_object().id})

        return context


class StudentDelete(DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentDelete, self).dispatch(*args, **kwargs)

    # def get_success_url(self):
    #     return reverse('/')
    # pohodu ustarelo i zamenilos' na success_url = ""


class GroupDelete(DeleteView):
    model = StudentGroup
    template_name = "group_confirm_delete.html"
    success_url = "/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GroupDelete, self).dispatch(*args, **kwargs)
