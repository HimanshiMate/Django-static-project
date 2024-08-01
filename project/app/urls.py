from django.contrib import admin
from django.urls import path
from .views import home 
from .views import product 
from .views import shop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('product/',product,name='product'),
    path('shop/',shop,name='shop')
]