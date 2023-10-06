from django.shortcuts import render, redirect
from .models import Course
from students.models import RegisteredCourses

# Create your views here.

def all_courses(request):
    search_query = request.GET.get('search_query', '')
    
    all_courses = Course.objects.filter(
        course_id__icontains=search_query
    ).order_by('course_id')

    context = { 'courses': all_courses, 'search_query': search_query }
    return render(request, 'courses/all_courses.html', context)

def confirm(request):
    return render(request, 'courses/confirm.html')

def course(request):
    return render(request, 'courses/course.html')