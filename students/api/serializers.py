import datetime
from django.contrib.auth.models import User
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from students.models import StudentGroup, Student


class UserSerializer(ModelSerializer):

    days_offline = SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'days_offline')

    def get_days_offline(self, obj):
        date = datetime.datetime.today()
        diff = date.replace(tzinfo=None) - obj.last_login.replace(tzinfo=None)
        return diff.days


class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'second_name', 'last_name',
                  'birth_date', 'student_card', 'group', 'student_name',)


class StudentGroupSerializer(ModelSerializer):

    students = StudentSerializer(source='student_set.all', many=True)
    steward = StudentSerializer(many=False)

    class Meta:
        model = StudentGroup
        fields = ('id', 'title', 'steward', 'students')


    def create(self, validated_data):
        steward_data = validated_data.pop('steward')
        group = StudentGroup.objects.create(**validated_data)
        Student.objects.create(group=group, **steward_data)
        return group

    def __delete__(self, instance):
        pass

    def update(self, instance, validated_data):
        steward_data = validated_data.pop('steward')

        steward = None
        if steward_data:
            steward = Student.objects.get(**steward_data)

        instance.title = validated_data.get('title', instance.title)
        instance.steward = steward
        instance.save()

        return instance



# class Log(models.Model):
#     add_date = models.DateTimeField(auto_now=True)
#     log = models.CharField(max_length=255)
#     model = models.CharField(max_length=125, null=True, blank=True)
#
#     def __unicode__(self):
#         return str(self.add_date)
#
#
# @receiver(pre_save, sender=Student)
# @receiver(pre_save, sender=StudentGroup)
# def stud_and_group_saver(sender, instance, **kwargs):
#     saver = Log()
#     saver.model = str(sender._meta.model_name)
#
#     try:
#         sender.objects.get(pk=instance.pk)
#         saver.log = 'edit'
#
#     except sender.DoesNotExist:
#         saver.log = 'create'
#
#     saver.log = 'Object {} {}'.format(instance, saver.log)
#     saver.save()
#
#
# @receiver(pre_delete, sender=Student)
# @receiver(pre_delete, sender=StudentGroup)
# def stud_adn_group_delete(sender, instance, **kwargs):
#     deleter = Log()
#     deleter.model = str(sender._meta.model_name)
#     deleter.log = 'Object {} was deleted'.format(instance)
#     deleter.save()
