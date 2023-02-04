from django.urls import path
from . import views
from django.urls import path, include
urlpatterns = [
    path('',views.home,name='home'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('view/<int:packageId>/', views.view, name='view'),
    path('process_order/', views.processOrder, name='process_order'),
    path('reachus/', views.reachus, name='reachus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    # path('login/', views.login, name='login'),
]
