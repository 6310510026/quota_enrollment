from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.student_id}'


class RegisteredCourses(models.Model):
    REQUESTED_STATUS = [
        ('approved', 'APPROVED'),
        ('not approved', 'NOT APPROVED'),
        ('pending', 'PENDING')
    ]

    registered_status = models.CharField(max_length=20, choices=REQUESTED_STATUS, default='pending')
    registered_course = models.ManyToManyField('courses.Course')

    def __str__(self):
        return f'{self.registered_course} ({self.registered_status})'