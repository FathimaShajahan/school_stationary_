from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from credentials.form import OrderForm
from .models import Course, Department

from .form import OrderForm, SubjectForm
from django.shortcuts import render
from .models import Course, Department
from django.shortcuts import render, redirect


#############################################

def subject(request):
    form = SubjectForm()
    return render(request,'new_page.html',{'form':form})


def loadcourse(request):
    department_id = request.GET.get("department")
    courses = Course.objects.filter(department_id=department_id)
    return JsonResponse({"courses": list(courses.values())}, safe=False)


####################################
def course_view(request):
    courses = Course.objects.all()
    print(courses)
    return render(request, 'form.html', {'courses': courses})

def form_view(request):
    departments = Department.objects.all()
    courses = Course.objects.all()
    # courses = Course.objects.filter(department=departments) 
    return render(request, 'new_page.html', {'departments': departments, 'courses': courses})


def submit_form(request):
    confirmation_message = ""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the form data to the database
            confirmation_message = "Order Confirmed"
        return render(request, 'thankyou.html', {'confirmation_message': confirmation_message})
    return redirect('index')


def login(request):
     if request.method =='POST':
          username=request.POST['username']
          password = request.POST['password']
          user=auth.authenticate(username=username,password=password)
          if user is not None:
               auth.login(request,user)
               return redirect('form_view')
          else:
               messages.error(request,"Invalid Credentials")
               return redirect('login')
     return render(request,'login.html')

def logout(request):
     auth.logout(request)
     return redirect('/')
     

def register(request):
   if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_pasword = request.POST['confirm_password']
        if password == confirm_pasword:
             if User.objects.filter(username=username).exists():
                  messages.info(request,'User Name already exist ')
                  return redirect('register')

             else:
                  user = User.objects.create_user(username=username,password=password)
                  user.save()
                  print('user created')
                  return redirect('login')
        else:
             messages.info(request,'PASSWORD NOT SAME')
             return render(request,'register.html')
        return redirect('/')
   return render(request,"register.html")
                 


