from django.shortcuts import render
from .models import Category , Products
from django.views.generic import DetailView , ListView
from django.shortcuts import render, get_object_or_404


# Create your views here.

class Cat_product_view(ListView):
    template_name = 'prod_cat_app/product_list.html'
    context_object_name = 'products_list'
    def get_queryset(self):
        category = get_object_or_404(Category,slug=self.kwargs['category_slug'])
        return Products.objects.filter(Category__name=category.name)
    def get_context_data(self, **kwargs):# we need to add more data from this view that is why I', using get_context_data
        context = super().get_context_data()
        #print(self.request.session)
        context['category_list'] = Category.objects.all()
        return context


class Product_details_view(DetailView):
    template_name = 'prod_cat_app/product_details.html'
    context_object_name = 'product_detail'
    queryset = Products.objects.all()


    def get_object(self):
        product_slug = self .kwargs.get('product_slug')
        return get_object_or_404(Products, slug=product_slug)
    def get_context_data(self, **kwargs): # we need to add more data from this view that is why I', using get_context_data
            context = super().get_context_data()
            context['category_list'] = Category.objects.all()
            return context
