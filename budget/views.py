from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.
#registration of user
#login
#logout


def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    return render(request,"budget/registration.html",context)