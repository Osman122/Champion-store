from django import  forms
from champions.models import Product,Category
from django.core.exceptions import ValidationError



class ProductForm(forms.Form):
    name = forms.CharField()
    price = forms.IntegerField(required=False)
    image = forms.ImageField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    # define validation rule in forms.py

    def clean_name(self):
        
        # cleaned data
        print(self.cleaned_data['name'] ,Product.name)
        found = Product.objects.filter(name=self.cleaned_data['name']).exists()
        if found:
            raise ValidationError("product name already exists")
        return self.cleaned_data['name']