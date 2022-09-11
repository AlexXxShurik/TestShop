from django.urls import path

from .views import *

urlpatterns = [
    path('', Minishop, name='minishop'),
    path('item/<int:id>', MinishopItem, name='minishop_item'),
    path('buy/<int:id>', MinishopBuy, name='minishop_buy'),
]