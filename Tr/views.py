from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
# from Tr.forms import *

def index(request):
    return render(request,"index.html")

# def contactUsForm(request):
#     cForm = ContactUsForm(request.POST or None)
#     if request.method == 'POST':
#         f = cForm.save(commit=False)
#         f.name = cForm.cleaned_data['name']
#         f.email = cForm.cleaned_data['email']
#         f.message = cForm.cleaned_data['message']
#         f.save()
#         return HttpResponse("Your message has been sent")
#     else:
#         cForm = ContactUsForm()
#     context = {'cForm': cForm, }
#     return render(request, 'index.html', context)


def termscondition(request):
    return render(request,'termsandcondition.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

