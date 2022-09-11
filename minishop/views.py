from django.http import JsonResponse
from django.shortcuts import render

from .models import *
from django.conf import settings

import stripe


def Minishop(request):
    items = Item.objects.all()
    return render(request, 'minishop.html', {'items': items})

def MinishopItem(request, id):
    itemID = Item.objects.get(pk=id)
    return render(request, 'minishop_item.html', {'item': itemID})

def MinishopBuy(request, id):
    itemID = Item.objects.get(pk=id)
    stripe.api_key = settings.STRIPE_API_KEY
    product = stripe.Product.create(name=itemID.name, description=itemID.description)
    price = stripe.Price.create(
      unit_amount=itemID.price*100,
      currency=itemID.currency,
      product=product,
    )
    session = stripe.checkout.Session.create(
      success_url=request.build_absolute_uri('/'),
      cancel_url=request.build_absolute_uri('/'),
      line_items=[
        {
          "price": price,
          "quantity": 1,
        },
      ],
      mode="payment",
    )
    return JsonResponse(session, safe=False)
