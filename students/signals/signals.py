from django.core.signals import request_finished
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from students.models import Student, StudentGroup, Log
from django.dispatch import Signal


student_signals = Signal(providin_args=['saver', 'deleter'])
