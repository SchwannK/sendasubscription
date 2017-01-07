from django.shortcuts import render
from .models import FaqCategory, FaqEntry

# Create your views here.

def faq_list(request):

    faq_categories = FaqCategory.objects.all()

    faq_entries = FaqEntry.objects.all()

    return render(request, 'faq/faq_list.html', {'navbar':'faq', 'faq_categories': faq_categories, 'faq_entries': faq_entries })
