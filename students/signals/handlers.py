from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from students.models import Student, StudentGroup, Log

@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=StudentGroup)
def stud_and_group_saver(sender, instance, **kwargs):
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


@receiver(pre_delete, sender=Student)
@receiver(pre_delete, sender=StudentGroup)
def stud_adn_group_delete(sender, instance, **kwargs):
    deleter = Log()
    deleter.model = str(sender._meta.model_name)
    deleter.log = 'Object {} was deleted'.format(instance)
    deleter.save()
