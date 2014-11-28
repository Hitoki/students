from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(auto_now=False)
    student_card = models.IntegerField()
    group = models.ForeignKey('StudentGroup')

    def __unicode__(self):
        return self.second_name

    class Meta:
        ordering = ['last_name']

    def student_name(self):
        return self.first_name + self.last_name + self.second_name


class StudentGroup(models.Model):
    title = models.CharField(max_length=255)
    steward = models.ForeignKey(Student, null=True, blank=True)

    def __unicode__(self):
        return self.title