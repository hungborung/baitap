from django.urls import path
from .views import *
from .api import api_add_to_cart, create_checkout_session, api_increment_quantity, api_remove_from_cart
from cart.views import *
from cart.webhook import webhook
from coupon.api import api_can_use
from userprofile.views import signup
from django.contrib.auth import views
from userprofile.views import account

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', categorydetail, name='categorydetail'),
    path('product/<str:slug>/', productdetail, name='productdetail'),
    path('cart/', cart_detail, name='cart'),
    path('cart/success/', success, name='success'),
    path('hooks/', webhook, name="webhook"),
    path('product-page/', search, name='search'),
    path('account/', account, name='account'),
    path('help/', help, name='help'),
    
    #auth
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),



    #API
    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    # path('api/checkout/', api_checkout, name='api_checkout'),
    path('api/can_use/', api_can_use, name='api_can_use'),

]