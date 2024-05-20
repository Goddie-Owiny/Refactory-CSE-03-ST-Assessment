from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.template import loader


# Create your views here.

#create view for the application form page
def student_reg(request):
    if request.method == 'POST':
        studentform = StudentForm(request.POST)
        print(request.POST)
        if studentform.is_valid():
            first_name = studentform.cleaned_data['first_name']
            last_name = studentform.cleaned_data['last_name']
            course = studentform.cleaned_data['course']
            entry_scheme = studentform.cleaned_data['entry_scheme']
            intake = studentform.cleaned_data['intake']
            sponsorship = studentform.cleaned_data['sponsorship']
            gender = studentform.cleaned_data['gender']
            dob = studentform.cleaned_data['dob']
            residence = studentform.cleaned_data['residence']
            Student.objects.create(first_name=first_name, last_name=last_name, course=course, entry_scheme=entry_scheme, intake=intake, sponsorship=sponsorship, dob=dob, residence=residence)
            return HttpResponseRedirect(reverse('student_reg'))
    else:
        studentform = StudentForm()
    studentlist = Student.objects.all()            
    return render(request, 'assessment_app/student_reg.html', {'studentform': studentform})
