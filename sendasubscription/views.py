from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.templatetags.static import static
from sendasubscription.forms import *

def contact(request):

    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the contact information
            template = get_template('contact_template.txt')

            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Send-a-subscription" + '',
                ['schwann.khaw@gmail.com'],
                reply_to=[contact_email],
            )
            email.send(fail_silently=False)
            return redirect('contact')

    return render(request, 'sendasubscription/contact.html', {'navbar':'contact', 'form': form_class})
