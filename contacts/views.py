from django.shortcuts import render,redirect

# from btre import contacts
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method =='POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']    
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)
        contact = Contact(listing=listing,listing_id = listing_id,email=email,name=name,phone=phone,message=message, user_id=user_id)
        contact.save()
        messages.success(request, 'A realtor will get back to you')
        return redirect('/listings/'+listing_id)