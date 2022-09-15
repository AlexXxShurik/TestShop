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
    intent = stripe.PaymentIntent.create(
      amount=itemID.price,
      currency=itemID.currency,
      payment_method_types=['card'],
    )
    return JsonResponse(intent, safe=False)
