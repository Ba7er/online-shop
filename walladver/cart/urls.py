from django.urls import path, include
from django.conf.urls import url
from cart import views
from cart.views import CartHome , Checkout


app_name = 'cart'


urlpatterns=[
    path('',CartHome.as_view(),name='cart'),
    path('cart_add/<str:product_name>',views.cartadd, name='cart_add'),
    path('cart_remove/<int:product_id>',views.cart_del_item, name = 'cart_del_item'),
    path('checkout/', Checkout.as_view(),name='checkout'),
]
