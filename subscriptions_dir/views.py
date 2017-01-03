from django.shortcuts import render

from subscriptions_lib.models import Category, Company, Subscription
from subscriptions_dir.utils import subscription_filter_utils


def subscriptions_dir(request):
    subscriptions = Subscription.objects.order_by('company__name')
    subcategories = subscription_filter_utils.get_subscription_subcategories(Subscription.objects.all())

    return render(request, 'subscriptions_dir/subscriptions_dir.html', {'navbar':'subscriptions', 'subscriptions': subscriptions, 'subcategories': subcategories,})
