#####
# try to refine this code by checking on how to create FormViews or Model.Form also
#have a look at form validations



from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class Billing_address_form(forms.Form):
    fullname    = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    city        = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    area        = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address_line= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Pobox       = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
