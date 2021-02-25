from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.
def register(request):
    if request.method == 'POST':
        #Get values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #Password check
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already used')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,"Registration Successfull")
                    return redirect('login')
        else:
            messages.error(request,'Password Do Not Match')
            return redirect('register')

    else:
        return render(request,'accounts/register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')
    
def dashboard(request):
    user_contact = Contact.objects.order_by('-Contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contact
    }
    return render(request,'accounts/dashboard.html',context)