from django.test import TestCase, Client 
from django.contrib.auth.models import User
from students.models import Student, StudentGroup


class StudentTestCase(TestCase):
    studentgroup = {title : 'TestGroup'}
    student = {first_name : 'TestFirstName',
               second_name : 'TestSecondName',
               last_name : 'TestLastName',
               birth_date : '1666-01-01',
               student_card : '1660101',
               group : 'TestGroup',
               }
    username = 'TestUsername'
    password = 'TestPassword'
    password1 = 'TestPassword'
    email = 'testuser@testemail.com'

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(self.username, self.email, self.password, self.password1)

    def test_login(self):
        status = self.client.login(username=self.username, email=self.email, password=self.password, password1=self.password1)
        self.assertEqual(stutus, True)

    def test_add_group_student_in_it(self):
        self.client.login(username=self.username, email=self.email, password=self.password, password1=self.password1)
        #login

        response = self.client.post('add_new_group', self.studentgroup)
        self.assertEqual(response.status_code, 200)
        # 200 - OK, 302 - Found, 502 - Bad Gateway, 404 - Noy Found;
        #POST request and add group 

        studentgroup = StudentGroup.objects.get(title=self.studentgroup['title'])
        self.student['group'] = studentgroup.title
        # .get studentgroup

        response = self.client.post('add_new_student', self.student)
        self.assertEquals(response.status_code, 302)
        #add student

        student = Student.object.get(student_card=self.student['student_card'])
        self.assertEqual(student.group, group)
        #checker (student.group = group)

        
