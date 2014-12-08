from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, UpdateView, CreateView
from students.models import Student, StudentGroup
from students.form import AddStudentForm, AddGroupForm, EmailUserCreationForm


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
        form = EmailUserCreationForm()
        return self.render_to_response({'form': form})

    def post(self, request):
        form = EmailUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        return self.render_to_response({'form': form})


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
