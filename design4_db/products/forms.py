from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'barcode',
            'name',
            'brand_name',
            'total_weight',
            'serving_size',
            'calories',
            'fat',
            'saturated_fat',
            'trans_fat',
            'cholesterol',
            'sodium',
            'carbohydrate',
            'fibre',
            'sugars',
            'protein',
            'vitamin_a',
            'vitamin_c',
            'calcium',
            'iron',
            'ingredients'
        ]
