from django import forms
from students.models import RegisteredCourses

class CourseSelectionForm(forms.ModelForm):
    class Meta:
        model = RegisteredCourses
        fields = ['registered_course']