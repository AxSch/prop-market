from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.
def register(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password != password2:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
    
    if User.objects.filter(username=username).exists():
      messages.error(request, "That username is taken")
      return redirect('register')
    
    if User.objects.filter(email=email).exists():
      messages.error(request, "That email is being used")
      return redirect('register')
    
    user = User.objects.create_user(username=username,\
      email=email, first_name=first_name, last_name=last_name)
    user.save()
    # auth.login(request, user)
    messages.success(request, "You have been successfully registered!")
    return redirect('login')
  else:
    return render(request, 'accounts/register.html')


def logout(request):
  return redirect('index')

def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
  context = {
    'contacts': user_contacts
  }
  return render(request, 'accounts/dashboard.html', context)