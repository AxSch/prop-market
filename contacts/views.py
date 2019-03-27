from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def contact(request):
  if request.method == "POST":
    listing_id = request.POST["listing_id"]
    listing = request.POST["listing"]
    name = request.POST["name"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    message = request.POST["message"]
    user_id = request.POST["user_id"]
    realtor_email = request.POST["realtor_email"]
    
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, "You've already made an inquiry for this listing!")
        return redirect('/listings/'+listing_id)
    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

    contact.save()

    # email = EmailMessage("Property Inquiry","Test for",'korrolschu@gmail.com',['korrolschu@gmail.com'])
    # email.send()
    messages.success(request, "Your inquiry has been submitted!, A realtor will be in touch soon!")
    return redirect('/listings/'+listing_id)