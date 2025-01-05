from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Instructor, Course, Lecture
from .forms import LectureForm, LoginForm, InstructorRegistrationForm, CourseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return redirect('login_user')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard') if request.user.is_superuser else redirect('instructor_dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard') if user.is_superuser else redirect('instructor_dashboard')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login_user')
def logout_user(request):
    logout(request)
    return redirect('login_user')

@login_required(login_url='login_user')
def admin_dashboard(request):
    user = request.user
    if user.is_superuser:
        instructors = Instructor.objects.all()
        courses = Course.objects.all()
        lectures = Lecture.objects.all()
        return render(request, 'admin_dashboard.html', {
            'instructors': instructors,
            'courses': courses,
            'lectures': lectures,
        })
    else:
        return redirect('instructor_dashboard')

@login_required(login_url='login_user')
def add_instructor(request):
    user = request.user
    if user.is_superuser:
        if request.method == 'POST':
            form = InstructorRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Instructor added successfully!')
                return redirect('admin_dashboard')
        else:
            form = InstructorRegistrationForm()
        return render(request, 'add_instructor.html', {'form': form})
    else:
        redirect('instructor_dashboard')

@login_required(login_url='login_user')
def add_course(request):
    user = request.user
    if user.is_superuser:
        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Course added successfully!')
                return redirect('admin_dashboard')
        else:
            form = CourseForm()
        return render(request, 'add_course.html', {'form': form})
    else:
        redirect('instructor_dashboard')

@login_required(login_url='login_user')
def schedule_lecture(request):
    user = request.user
    if user.is_superuser:
        if request.method == 'POST':
            form = LectureForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_dashboard')
        else:
            form = LectureForm()
        return render(request, 'schedule_lecture.html', {'form': form})
    else:
        redirect('instructor_dashboard')

@login_required(login_url='login_user')
def instructor_dashboard(request):
    try:
        instructor = request.user.instructor
        lectures = Lecture.objects.filter(instructor=instructor)
        return render(request, 'instructor_dashboard.html', {'lectures': lectures})
    except:
        return redirect('admin_dashboard') if request.user.is_superuser else redirect('instructor_dashboard')

