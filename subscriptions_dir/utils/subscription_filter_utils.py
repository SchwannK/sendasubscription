# @param subscriptions: a QuerySet
def get_subscription_subcategories(subscriptions):
    all_subscription_subcategories = subscriptions.values_list('company__subcategory__name', flat=True)
    return sorted(list(set(list(all_subscription_subcategories))))
