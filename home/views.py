import email
from email import message
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # context={
    #     'variable1':'variable1',
    #     'variable2':'variable2'

    # }
    # messages.success(request,"This is test Message")
    return render(request,'index.html')
    # return HttpResponse('This is Home page') #it directly run string on web without writing html

def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')



def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save() 
        messages.success(request,'Your Querry has been sent')

    return render(request,'contact.html')

