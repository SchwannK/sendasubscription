from django.shortcuts import render

from subscriptions_dir.utils import subscription_filter_utils
from subscriptions_lib.models import Subscription


def subscriptions_dir(request):
    subscriptions = Subscription.objects.order_by('company__name')

    # Show all categories, regardless of whether subscriptions exist or not
    categories = Category.objects.all()

    # Only show categories for which subscriptions exist
    # categories = subscription_filter_utils.get_subscription_categories(Subscription.objects.all())

    return render(request, 'subscriptions_dir/subscriptions_dir.html', {'navbar':'subscriptions', 'subscriptions': subscriptions, 'categories': categories, })
