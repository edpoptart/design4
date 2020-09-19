"""design4_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include
from django.conf.urls import url

import pages.views
import products.views

urlpatterns = [
    # Default
    path('', pages.views.index_view, name='index'),
    path('contact/', pages.views.contact_view, name='contact'),

    # Product
    path('products/create/', products.views.product_create_view, name='product-create'),
    path('products/public/list/', products.views.product_list_public_view, name='product-list-public'),
    path('products/<id>/detail/', products.views.product_detail_view, name='product-detail'),

    # Accounts
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', pages.views.signup, name='signup'),
    path('activate/<uidb64>/<token>/', pages.views.activate, name='activate'),

    # API
    path('API/fetchProductDataByBarcode/<barcode>/', products.views.product_detail),
]
