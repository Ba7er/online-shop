from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from prod_cat_app.views import Cat_product_view , Product_details_view


app_name = 'prod_cat_app'

urlpatterns = [

        path('cat_products/<slug:category_slug>',Cat_product_view.as_view(), name='cat_products'),
        path('product_detail/<slug:product_slug>',Product_details_view.as_view(), name='product_detail'),

]
