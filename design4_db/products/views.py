from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProductForm
from .models import Product

# Create your views here.


@login_required
def product_create_view(request):
    # TODO Remove initial values
    # TODO Change template to accomodate Product_item
    initial_value = {
        'barcode':'1234206956',
        'name':'Gold Standard Whey',
        'brand_name':'Omny Nutrition',
        'total_weight':'2270g',
        'serving_size':'31g',
        'calories':'110 cal',
        'fat':'1g',
        'saturated_fat':'0.5g',
        'trans_fat':'0',
        'cholesterol':'40mg',
        'sodium':'130mg',
        'carbohydrate':'2g',
        'fibre':'0g',
        'sugars':'2g',
        'protein':'24g',
        'vitamin_a':'0%',
        'vitamin_c':'0%',
        'calcium':'8%',
        'iron':'0%',
        'ingredients':'Whey Protein Concentrates, Whey Protein Peptides, Natural and Artificial flavours, Lecithin'
    }
    form_product = ProductForm(request.POST or None, initial=initial_value)
    if form_product.is_valid():
        new_product = form_product.save(commit=False)
        new_product.creator = request.user
        new_product = form_product.save()
        return product_detail_view(request, new_product.id)

    context = {
        'form':form_product,
        'request': request
    }
    return render(request, 'products/product_create.html', context)



# If user is seller shows bids, otherwise display basic info on Product
def product_detail_view(request, id):
    product_object = get_object_or_404(Product, id=id)

    context = {
        'product_object': product_object
    }
    return render(request, 'products/product_detail_base.html', context)


# List every product without bid offers
#TODO Should everyone be able to see product or we keep them private?
def product_list_public_view(request):
    # TODO Change template to accomodate Product_item
    queryset = Product.objects.all()
    context = {
        'product_list': queryset
    }
    return render(request, 'products/product_list.html', context)