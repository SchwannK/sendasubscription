from django.shortcuts import render
from sendasubscription.forms import *

def contact(request):

    return render(request, 'sendasubscription/contact.html', {'navbar':'contact', 'form': ContactForm()})
