from django import http
from django.core.checks import messages
from django.db.models import query
from django.http import response
from django.http.response import FileResponse, HttpResponse
from django.shortcuts import render , redirect
from . import models

# Create your views here.
def home(request):
    data = models.PersonalData.objects.get(id= 1)
    edu = models.Education.objects.all
    exp = models.Experience.objects.all
    cskill = models.CodingSkills.objects.all
    dskill = models.DevelopmentSkills.objects.all
    count = models.Counter.objects.all
    mywork = models.mywork.objects.all
    tags = models.Tags.objects.all
    resume = models.links.objects.get(id= 1)
        
    return render(request,'index.html',{'mydata':data,'exp':exp,'edu':edu, 'cskill':cskill,
                                        'dskill':dskill, 'count':count , 'mywork': mywork,
                                        'tags': tags ,'resume':resume.resume})

def getdata(request):
    if request.method == 'POST':
        name1 = request.POST['Name']
        email1 = request.POST['Email']
        subject1 = request.POST['Subject']
        message1 = request.POST['Message']
        querry = models.Querry(name = name1 , email = email1 , subect = subject1 , message = message1)
        querry.save()
        return redirect('/')
def Subscribe(request):
    if request.method == 'POST':
        Subscribe = request.POST['Email_Subs']
        subs = models.Subscibe(email = Subscribe)
        subs.save()
        return redirect('/')

