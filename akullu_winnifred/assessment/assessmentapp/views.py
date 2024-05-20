from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = regform(request.POST)
        fname = request.POST['first name']
        lname = request.POST.get('last name')
        course = request.POST.get('course')
        entryscheme = request.POST.get('entryscheme')
        intake = request.POST.get('intake')
        sponsorship = request.POST.get('sponsorship')
        gender = request.POST.get('flexRadioDefault')
        dob = request.POST.get('dob')
        residence = request.POST.get('residence')
        form = Reg(fname=fname,lname=lname,dob=dob,gender=gender,course=course,entryscheme=entryscheme,intake=intake,sponsorship=sponsorship,residence=residence)
        form.save()
        messages.success(request,'Form has Been Submitted Successfully!')
        return redirect('/')
    else:
        return render(request,'assessmentapp/index.html')