from django.shortcuts import render

from subscriptions_lib.models import Category, Company, Subscription
from subscriptions_dir.utils import subscription_filter_utils

from .forms import GiftForm

def subscriptions_dir(request):

    subscriptions = Subscription.objects.order_by('company__name')

    categories = Category.objects.all()

    form = GiftForm()

    return render(request, 'subscriptions_dir/subscriptions_dir.html', {'navbar':'subscriptions', 'subscriptions': subscriptions, 'categories': categories, 'form': form})


def subscriptions_dir_specific(request, recipient_tag):

    subscriptions = Subscription.objects.filter(tags__name__in=[recipient_tag]).order_by('company__name')

    categories = Category.objects.filter(subscription__in=subscriptions).distinct()

    form = GiftForm()

    return render(request, 'subscriptions_dir/subscriptions_dir.html', {'navbar':'subscriptions', 'subscriptions': subscriptions, 'categories': categories, 'form': form})
