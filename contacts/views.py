from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You already make an inquiry for this listing')
                return redirect('/listings/'+listing_id)
        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        #Send mail

        send_mail(
            'Property Listing enquiry',
            'There has been an enquiry for ' + listing + '. Sign in admin panel to check for more info.',
            'whiteVwalker@gmail.com',
            [realtor_email,'rajat6399@gmail.com'],
            fail_silently=False
        )
        messages.success(request,'Your request has been submitted, We will get back to you soon')
        return redirect('/listings/'+listing_id)
