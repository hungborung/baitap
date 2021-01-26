from django.urls import path
from .views import *
from .api import *
from cart.views import *
from cart.webhook import webhook
from coupon.api import api_can_use


urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', categorydetail, name='categorydetail'),
    path('product/<str:slug>', productdetail, name='productdetail'),
    path('cart/', cart_detail, name='cart'),
    path('cart/success/', success, name='success'),
    path('hooks/', webhook, name="webhook"),

    #API
    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    path('api/checkout/', api_checkout, name='api_checkout'),
    path('api/can_use/', api_can_use, name='api_can_use'),

]