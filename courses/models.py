from django.db import models

# Create your models here.

class Course(models.Model):
    COURSE_STATUS = [
        ('open', 'OPEN'),
        ('close', 'CLOSE')
    ]

    course_id = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=60, unique=True)
    semester = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()
    course_status = models.CharField(max_length=10, choices=COURSE_STATUS, default='open')

    def __str__(self):
        return f'{self.course_id} (id={self.id})'