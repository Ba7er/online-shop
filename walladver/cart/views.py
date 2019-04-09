from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from prod_cat_app.models import Products , Category
from .models import Cart ,ShippingAddresses , My_order
from cart.forms import Billing_address_form
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.db.models import Sum
from django.views import View
from django.http import HttpResponseRedirect
import stripe
import datetime
import random
# Create your views here.

class CartHome(ListView):
    template_name = 'cart.html'
    context_object_name = 'cart_detail'
    def get_queryset(self):
        cart_id = self.request.session.get('cart_id',None)
        cart_obj = Cart.objects.get(id=cart_id)
        print(cart_obj.product.all())
        return cart_obj.product.all()
    def get_context_data(self, **kwargs):# we need to add more data from this view that is why I', using get_context_data
        context = super().get_context_data()
        cart_id = self.request.session.get('cart_id',None)
        cart_obj = Cart.objects.get(id=cart_id)
        #print(self.request.session)
        context['context'] = Category.objects.all()
        context['total'] = cart_obj.product.all().aggregate(Sum('price'))
        return context


def cartadd(request,product_name):
    cart_id = request.session.get('cart_id',None)
    prod_obj = Products.objects.get(name=product_name)
    print('this is product object',prod_obj)
    cart_obj = Cart.objects.get(id=cart_id)
    cart_obj.product.add(prod_obj.id)
    total = cart_obj.product.aggregate(Sum('price'))
    print('the total is ',total)
    cart_obj.total = total['price__sum']
    cart_obj.save()
    return redirect('cart:cart')

def cart_del_item(request, product_id):
    if request.method == 'POST':
        cart_id = Cart.objects.get(id=request.session.get('cart_id', None))
        product_obj = Products.objects.get(id=product_id)
        product_obj.cart_set.remove(cart_id)
        return redirect('cart:cart')
    else:
        return redirect('cart:cart')
####### how to add the user after authentication to the shipping address model?????
class Checkout(View):
    def get(self,request):
        if request.user.is_authenticated:
            sh_obj = ShippingAddresses.objects.filter(user__email=request.user)
            form = Billing_address_form(initial={'fullname':request.user.firstname + ' ' +request.user.lastname ,
            'email':request.user.email})
            return render(request,'checkout.html',{'form':form})
        else:
            return redirect('/loginpage/'+'?next=shippingaddress')



#####still need to make sure the payments is sccessful#####
    def post(self,request):
        stripe.api_key = "sk_test_Ln325yMLJM96doz28lnlxAIx00vQplbcK4"
        cart_obj = Cart.objects.get(id=request.session.get('cart_id', None))
        form = Billing_address_form(request.POST)
        print('is form is valid',form.is_valid())
        if form.is_valid():
            shipping_address = ShippingAddresses(user=request.user,cart=cart_obj,
            city= form.cleaned_data['city'] ,
            area=form.cleaned_data['area'],
            address_line=form.cleaned_data['address_line'],
            Pobox=form.cleaned_data['Pobox'])
            shipping_address.save()
            token = request.POST['stripeToken']
            charge = stripe.Charge.create(
            amount=int(cart_obj.total),
            currency='usd',
            description='Purchase Order',
            source=token,)
            My_order_obj = My_order(user=request.user, cart=cart_obj, shipping_details=shipping_address,
                                        order_id=random.randint(10000,99999),
                                    order_date=datetime.datetime.now(),order_status=False)
            My_order_obj.save()
            return render(request,'order.html',{'order_id':My_order_obj.order_id})
        else:
            return HttpResponseRedirect('/home/')
