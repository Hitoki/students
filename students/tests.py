from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User


class StudentTestCase(TestCase):
    studentgroup = {'title': 'TestGroup'}
    student = {'first_name': 'TestFirstName',
              'second_name': 'TestSecondName',
              'last_name': 'TestLastName',
              'birth_date': '1666-01-01',
              'student_card': '1660101',
              'group': 'TestGroup',
              }
    username = 'TestUsername'
    password = 'TestPassword'
    password1 = 'TestPassword'
    email = 'testuser@testemail.com'

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.client.login(username=self.username, email=self.email, password=self.password,
                          password1=self.password1)

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': self.email,
                                                       'password': self.password})
        self.assertEqual(response.status_code, 302)

    def test_add_group_and_student_in_it(self):
        response = self.client.post(reverse('add_new_group'), self.studentgroup)
        self.assertEqual(response.status_code, 302)
        #add group

        response = self.client.post(reverse('add_new_student'), self.student)
        self.assertEquals(response.status_code, 302)
        #add student
