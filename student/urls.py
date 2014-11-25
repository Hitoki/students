from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout, login
from students.views import StudentGroupView, StudentGroupDetailView, RegistrationView,\
    AddStudent, AddGroup, EditStudent, EditGroup, GroupDelete, StudentDelete

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'student.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', StudentGroupView.as_view(), name='index'),
    url(r'^group_detail/(?P<pk>\d+)/$', StudentGroupDetailView.as_view(), name='group_detail'),

    url(r'^add_new_student', AddStudent.as_view(), name='add_new_student'),
    url(r'^add_new_group', AddGroup.as_view(), name='add_new_group'),
    url(r'^edit_student', EditStudent.as_view(), name='edit_student'),
    url(r'^edit_group', EditGroup.as_view(), name='edit_group'),
    url(r'^delete_student', StudentDelete.as_view(), name='delete_student'),
    url(r'^delete_group', GroupDelete.as_view(), name='delete_group'),

    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^registration/$', RegistrationView.as_view(), name='registration')
)
