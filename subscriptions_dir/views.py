from _decimal import Decimal

import braintree
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt

from subscriptions_dir.models import Order, Customer
from subscriptions_dir.utils import subscription_filter_utils
from subscriptions_lib.models import Category, Company, Subscription

from .forms import GiftForm


def subscriptions_dir(request):

    subscriptions = Subscription.objects.order_by('company__name')

    categories = Category.objects.all()

    form = GiftForm()
    content = {'navbar':'subscriptions', 'subscriptions': subscriptions, 'categories': categories, 'form': form}
    
    if 'message' in request.session:
        content['message'] = request.session['message']

    return render(request, 'subscriptions_dir/subscriptions_dir.html', content)


def subscriptions_dir_specific(request, recipient_tag):

    subscriptions = Subscription.objects.filter(tags__name__in=[recipient_tag]).order_by('company__name')

    categories = Category.objects.filter(subscription__in=subscriptions).distinct()

    form = GiftForm()

    return render(request, 'subscriptions_dir/subscriptions_dir.html', {'navbar':'subscriptions', 'subscriptions': subscriptions, 'categories': categories, 'form': form})

@login_required
@csrf_exempt
def checkout(request):
    if request.POST and request.POST.get('subscription'):
        subscription = Subscription.objects.get(pk=request.POST.get('subscription'))
        user = request.user
        customer = Customer.objects.get(user = user)
        a_customer_id = ''
        if not customer.customer_id:
            print("Not a customer. Creating...")
            result = braintree.Customer.create({
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                })
            print("result: " + str(vars(result)))
            if result.is_success:
                customer.customer_id = result.customer.id
                customer.save()
                a_customer_id = customer.customer_id
        else:
            a_customer_id = customer.customer_id
        
        print("Customer id: " + str(a_customer_id))
    
        if not customer.client_token:
            print("Fetching client token...")
            client_token = braintree.ClientToken.generate({
                    "customer_id": a_customer_id
                })
            customer.client_token = client_token
            customer.save()
        else:
            client_token = customer.client_token
            
        print("Client token: " + str(client_token))
        print("Subscription: " + str(request.POST.get('subscription')))
        varibles = {'subscription':subscription, 'client_token':client_token}
        
        return render(request, 'subscriptions_dir/checkout.html', varibles)
    return redirect("/")

@login_required
@csrf_exempt
def payment(request):
    request.session['message'] = None
    if request.POST:
        if request.POST.get("payment_method_nonce"):
            subscription = Subscription.objects.get(pk=request.POST.get('subscription'))
            nonce_from_the_client = request.POST.get("payment_method_nonce")
            user = request.user
            order = Order()
            order.subscription = subscription
            order.user = user
            order.payment_nonce = nonce_from_the_client
            order.save()
            result = braintree.Transaction.sale({
                "amount": Decimal(order.subscription.price),
                "payment_method_nonce": order.payment_nonce
            })
            transaction_id = result.transaction.id
            order.txnid = transaction_id
            order.save()
            message = ''
            if result.is_success:
                order.result = True
                order.save()
                request.session['message'] = 'Transaction successfully completed' + ' : ' + transaction_id
                return redirect("/")
            else:
                message = 'Error Transaction Failed'

                variables = {'message':message, }
                return render(request, 'subscriptions_dir/checkout.html', variables)
        else:
            message = 'No transaction'

            variables = {'message':message, }
            return render(request, 'subscriptions_dir/checkout.html', variables)
