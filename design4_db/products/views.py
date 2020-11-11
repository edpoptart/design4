from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from products.forms import ProductForm
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.

# API Related
@csrf_exempt
def product_fetch(request, barcode):
    """
    Retrieve, update or delete a product by barcode.
    """
    try:
        product = Product.objects.get(id=barcode)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)

@csrf_exempt
def product_atributes_fetch(request):
    """
    Retrieve, update or delete a product by its attributes.
    """
    if request.method == 'POST':
        product = Product()
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        
        products = []
        products.extend(Product.objects.get(brand_name=[product.logos]))
        products.extend(Product.objects.get(brand_name=[product.logos.split("L")[0]]))
        print(len(products))

        #if serializer.is_valid():
        #    serializer.save()
        #    return JsonResponse(serializer.data)
        #return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_insert(request):
    """
    Insert a product.
    """
    if request.method == 'PUT':
        product = Product()
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

# Web

@login_required
def product_create_view(request):
    # TODO Remove initial values
    # TODO Change template to accomodate Product_item
    initial_value = {
        'id':'1234206956',
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
        'ingredients':'Whey Protein Concentrates, Whey Protein Peptides, Natural and Artificial flavours, Lecithin',
        'allergens':'milk'
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