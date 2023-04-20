from django.shortcuts import render
from home_app.models import contactform

# Create your views here.

'''Function for home page'''
def home(request):
    return render(request, 'home_app/home.html')

'''Function for about page'''
def about(request):
    return render(request, 'home_app/about.html')

'''Function for contact page'''
def contact(request):
    
    if request.method == 'POST':
        
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_subject = request.POST.get('subject')
        contact_message = request.POST.get('message')
        
        contactformdata = contactform(name=contact_name, email=contact_email, 
                                      subject=contact_subject, message=contact_message)
        contactformdata.save()
    
    return render(request, 'home_app/contact.html')

