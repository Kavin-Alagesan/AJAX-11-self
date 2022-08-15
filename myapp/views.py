from re import I
from urllib import request
from django.contrib import messages
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Work
from .forms import WorkCreate
from django.forms.models import model_to_dict

# Create your views here.
def home(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
            # Redirect to a success page.
        else:
            messages.warning(request, ("There was a error logging in. Try again... of if you are new user Register now"))
            return redirect(home)
    else:
        return render(request,'index.html')

@login_required()
def dashboard(request):
    return render(request,'homepage.html')

@login_required()
def blog(request):
    return render(request,'blog.html')

@login_required()
def contact(request):
    return render(request,'contact.html')

@login_required()
def work(request):
    if request.method=='POST':
        project=request.POST['project1']
        tasks=request.POST['tasks']
        team_member=request.POST['team_member']
        shift_timing=request.POST['flexRadioDefault']
        comments=request.POST['comments']
        save_in_db=Work.objects.create(project=project,task=tasks,team_member=team_member,shift_timing=shift_timing,comments=comments)
        save_in_db.save()
        messages.success(request, ("Task assigned successfully!"))
        return redirect('create_task')
    else:
        return render(request,'work/edit_task.html')

@login_required()
def create_task(request):
    datas=Work.objects.all()
    return render(request,'work/edit_task.html',{'datas':datas})

@login_required()
def edit_and_update(request,id):
    object=Work.objects.get(id=id)
    print(object)
    if request.method=='POST':
        project=request.POST['project']
        tasks=request.POST['task']
        team_member=request.POST['team_member']
        shift_timing=request.POST['flexRadioDefault']
        comments=request.POST['comments']
        Work.objects.filter(id=id).update(project=project,task=tasks,team_member=team_member,shift_timing=shift_timing,comments=comments)
        messages.success(request, "Task edited successfully!")
        return redirect('create_task')
    else:
        return render(request,'work/edit_task.html', {'object':object})

@login_required()
def delete_task(request,id):
    Work.objects.filter(id=id).delete()
    return redirect('create_task')

@login_required()
def post(request,id):
    data = Work.objects.get(id=id)
    #print(type(data))
    data_dict = model_to_dict(data)
    # print(type(data_dict))
    return JsonResponse(data_dict,safe=False)
    

@login_required()
def register(request):
    if request.method =="POST":
        username = request.POST['name']
        email=request.POST['email']
        password = request.POST['password']
        password2=request.POST['re_password']
        if password != password2:
            messages.warning(request, ("Primary password doen't matches with secondary password"))
            return render(request,'register/index-register.html')
        else:
            user=User.objects.create_user(username=username, email=email,password=password)
            user.save()
            messages.success(request, ("Registration successfull"))
            return redirect('home')
    else:   
        return render(request,'register/index-register.html')

def logout(request):
    django_logout(request)
    messages.success(request,('You were logged out'))
    return redirect('home')
