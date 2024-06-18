from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Meeting, Post

# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,"index.html",{'posts':posts})

def insert_demo(request):
    m=Meeting(meeting_code="m002",meeting_dt="2024-04-10",meeting_subject="WTW",meeting_np=50)
    m.save()
    m=Meeting(meeting_code="m003",meeting_dt="2024-04-10",meeting_subject="parent meet",meeting_np=50)
    m.save()
    m=Meeting(meeting_code="m004",meeting_dt="2024-04-10",meeting_subject="course",meeting_np=50)
    m.save()
    m=Meeting(meeting_code="m005",meeting_dt="2024-04-10",meeting_subject="infrastructure",meeting_np=50)
    m.save()
    return HttpResponse('<h1>record inserted successfully</h1>')
def update_demo(request):
    m=Meeting.objects.get(meeting_code="m002")
    m.meeting_dt="2024-04-11"
    m.meeting_np=100
    m.save()
    return HttpResponse("<h1>record updated successfully</h1>")

def delete_demo(request):
    m=Meeting.objects.get(meeting_code="m005")
    m.delete()
    return HttpResponse("<h1>record deleted</h1>")