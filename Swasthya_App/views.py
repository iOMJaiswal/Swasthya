from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import FirstAid, Ambulance, Doctor, Patient
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout



# User Login and Authentication

def login(request):
    if request.user.is_authenticated:
        return redirect('/index')
    
    else:
        if request.method == 'POST':
            email = request.POST['user_email']
            password = request.POST['user_pass']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request,"User login Successful!!!")
                
                return redirect('/index')
            
            else:
                messages.error(request, "Username or Password is Wrong!!! Try Again.")
                return redirect('/login')


    return render(request, 'login.html')

def register(request):

    if request.user.is_authenticated:
        return redirect('/index')
    
    else:
        if request.method == 'POST':
            fname = request.POST['user_fname']
            lname = request.POST['user_lname']
            email = request.POST['user_email']
            password = request.POST['user_pass']
            Cpassword = request.POST['user_Cpass']
            

            # Check if email already exists or not
            # Here I am using try except block because of .exists() method is not working, showing Database error
            # The following method throws a database error while it dont get results. It is only while using Mongodb

            try:
                User.objects.get(username =email)
                messages.error(request, "Email Already Exists!!! Try Again.")
                return redirect('/register')
            except:
                if password != Cpassword:
                    messages.error(request, "Password and Confirm Password did not match!!")
                    return redirect('/register')
                else:
                    user = User.objects.create_user(username=email, email=email,password=password)
                    user.first_name = fname
                    user.last_name = lname
                    user.save()
                    messages.success(request, "Account Created Successfully!!!")
                    return redirect('/index')
    
    return render(request, 'register.html')

def logout(request):
    auth_logout(request)
    messages.success(request, "Logout Succsessfully!!!")
    return redirect('/index')








def index(request):
    return render(request, 'index.html')




def firstaid(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        new_firstaid = FirstAid(title=title, description=description)
        new_firstaid.save()
        return redirect('/firstaid')
    
    elif request.method == 'GET':
        firstaids = FirstAid.objects.all()
        context = {
            'firstaids' : firstaids
        }
        return render(request, 'firstaid.html', context)
    
    else:
        return render(request, 'firstaid.html')


def doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        degree = request.POST.get('degree')
        hospital = request.POST.get('hospital')
        mobile = request.POST.get('mobile')

        new_doctor = Doctor(name=name,degree=degree,hospital=hospital,mobile=mobile)
        new_doctor.save()

        return redirect('/doctor')
    
    elif request.method == 'GET':
        doctors = Doctor.objects.all()
        context = {
            'doctors' : doctors
        }
        return render(request, 'doctor.html', context)    
    else:
        return render(request, 'doctor.html')



def ambulance(request):
    if request.method == 'POST':
        urgency = request.POST.get('urgency')
        location = request.POST.get('location')

        ambulance_req = Ambulance(urgency=urgency,location=location)
        ambulance_req.save()
        messages.success(request,"Ambulance is On the Way!!!")

        return redirect('/index')
    
    elif request.method == 'GET':

        return render(request, 'ambulance.html')
    
    else:
        return render(request, 'ambulance.html')


def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        problem = request.POST.get('problem')
        mobile = request.POST.get('mobile')

        new_Patient = Patient(name=name,location=location,problem=problem,mobile=mobile)
        new_Patient.save()
        
        messages.success(request,"Appointment Booked!!!")


        return redirect('/index')
    
    elif request.method == 'GET':
        doctors = Doctor.objects.all()
        context = {
            'doctors' : doctors
        }
        return render(request, 'doctor.html', context)    
    else:
        return render(request, 'doctor.html')



# Created Context