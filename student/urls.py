from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout, login
from students.views import StudentGroupView, StudentGroupDetailView, RegistrationView, \
    AddStudent, AddGroup, StudentUpdate, GroupUpdate, GroupDelete, StudentDelete, StudentProfileView
from rest_framework.routers import DefaultRouter
from students.api import views

router = DefaultRouter()
router.register(r'users', views.UserView, base_name='users')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'student.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', StudentGroupView.as_view(), name='index'),
    url(r'^group_detail/(?P<pk>\d+)/$', StudentGroupDetailView.as_view(), name='group_detail'),
    url(r'^student_detail/(?P<pk>\d+)/$', StudentProfileView.as_view(), name='student_detail'),

    url(r'^add_new_student', AddStudent.as_view(), name='add_new_student'),
    url(r'^add_new_group', AddGroup.as_view(), name='add_new_group'),

    url(r'^edit_student/(?P<pk>\d+)/$', StudentUpdate.as_view(), name='student_edit'),
    url(r'^edit_group/(?P<pk>\d+)/$', GroupUpdate.as_view(), name='group_edit'),

    url(r'^delete_student/(?P<pk>\d+)/$', StudentDelete.as_view(), name='student_delete'),
    url(r'^delete_group/(?P<pk>\d+)/$', GroupDelete.as_view(), name='group_delete'),

    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
)
