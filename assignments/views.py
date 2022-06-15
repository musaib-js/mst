from django.shortcuts import render, redirect
from .models import Assignment, Submission
from . forms import SubmissionForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# Create your views here.
def assignmentshome(request):
    assignments  = Assignment.objects.filter(is_active = True)
    context = {'assignments': assignments}
    return render(request, 'assignmentshome.html', context)

def assignmentview(request, unique_name):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            user = request.user
            file = form.cleaned_data['file']
            assignment = form.cleaned_data['assignment']
            newsubmission = Submission(user = user, file = file, assignment = assignment)
            already_submitted = Submission.objects.filter(user = user, assignment = assignment )
            if already_submitted:
                return HttpResponse("You Have Already Submitted A Response For the Same Assignment")
            else:
                newsubmission.save()
                return HttpResponse("Thanks Press This Button To Go Home")
    form = SubmissionForm(request.POST)
    assignment = Assignment.objects.filter(unique_name = unique_name).first()
    asslist = Assignment.objects.all()
    context = {'assignment': assignment, 'asslist':asslist, 'form':form}
    return render(request, 'assignment.html', context)