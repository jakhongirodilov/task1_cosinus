from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'status']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
