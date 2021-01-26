from django import forms
from .models import *

class CategoryForm(form.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(form.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'