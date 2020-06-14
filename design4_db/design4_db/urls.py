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

import pages.views as pv
import products.views as av

urlpatterns = [
    # Default
    path('', pv.index_view, name='index'),
    path('contact/', pv.contact_view, name='contact'),

    # product
    path('products/create/', av.product_create_view, name='product-create'),
    path('products/public/list/', av.product_list_public_view, name='product-list-public'),
    path('products/<id>/detail/', av.product_detail_view, name='product-detail'),

    # Accounts
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', pv.signup, name='signup'),
    path('activate/<uidb64>/<token>/', pv.activate, name='activate'),
]
