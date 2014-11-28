# django.db.models.signals.pre_save & django.db.models.signals.post_save
#
# Отправляются до или после вызова метода save() модели.
#
# django.db.models.signals.pre_delete & django.db.models.signals.post_delete
#
# Отправляются до или после вызова метода delete() модели или delete() класса QuerySet.
from django.core.signals import request_finished

from django.dispatch import Signal
from django.db.models.signals import pre_save
from django.dispatch import receiver
from students.models import Student, StudentGroup, Log


@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=StudentGroup)
def stud_and_group_saver(sender, instance, signal, *args, *kwargs):
    print ('start')
    saver = Log()
    saver.model = str(sender)

    try:
        sender.objects.get(pk=instance.pk)
        saver.log = 'edit'

    except sender.DoesNotExist:
        saver.log = 'create'

    saver.log = 'Object {}{}'.format(instance, saver.log)
    saver.save()
    print ('end')

# Signal.connect(stud_and_group_saver, sender=None, weak=True, dispatch_uid=None)


@receiver(request_finished)
def test_signal(sender, **kwargs):
    print('Test signal')