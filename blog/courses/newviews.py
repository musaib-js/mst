from multiprocessing import context
from re import sub
from django.shortcuts import render , redirect
from .models import Course, Teacher, Contact
from django.contrib import messages
from courses.models import UserCourse
from django.contrib.auth.decorators import login_required

def allcourses(request):
    allcourses = Course.objects.all()
    print(allcourses)
    context = {'allcourses': allcourses}
    return render(request, 'courses.html', context)

def teachers(request):
    teachers = Teacher.objects.all()
    context = {'teachers':teachers}
    return render(request, 'teachers.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone= request.POST['phone']
        message = request.POST['message']

        newmsg = Contact(name =  name, email = email, subject = subject, phone = phone, message = message)
        newmsg.save()
        messages.success(request, "Your Query Has Been Submitted. We Shall Be In Touch With You Soon")
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url='/login')
def profile(request):
    user = request.user
    usercourse =  UserCourse.objects.filter(user = user)[0:3]
    print(usercourse)
    context = {'usercourse':usercourse}
    return render(request, 'profile.html', context)

def search(request):
    query=request.GET['query']
    if len(query)>100:
        allCourses=Course.objects.none()
    else:
        allCoursesName= Course.objects.filter(name__icontains=query)
        allCourses=  allCoursesName
    if allCourses.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    context={'allCourses': allCourses, 'query': query}
    return render(request, 'search.html', context)

def faqs(request):
    return render(request, 'faqs.html')