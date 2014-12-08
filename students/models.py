from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver


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
        return "{} {} {}".format(self.first_name, self.last_name, self.second_name)


class StudentGroup(models.Model):
    title = models.CharField(max_length=255)
    steward = models.ForeignKey(Student, null=True, blank=True)

    def __unicode__(self):
        return self.title


class Log(models.Model):
    add_date = models.DateTimeField(auto_now=True)
    log = models.CharField(max_length=255)
    model = models.CharField(max_length=125, null=True, blank=True)

    def __unicode__(self):
        return str(self.add_date)


@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=StudentGroup)
def stud_and_group_saver(sender, instance, **kwargs):
    saver = Log()
    saver.model = str(sender._meta.model_name)

    try:
        sender.objects.get(pk=instance.pk)
        saver.log = 'edit'

    except sender.DoesNotExist:
        saver.log = 'create'

    saver.log = 'Object {} {}'.format(instance, saver.log)
    saver.save()


@receiver(pre_delete, sender=Student)
@receiver(pre_delete, sender=StudentGroup)
def stud_adn_group_delete(sender, instance, **kwargs):
    deleter = Log()
    deleter.model = str(sender._meta.model_name)
    deleter.log = 'Object {} was deleted'.format(instance)
    deleter.save()
