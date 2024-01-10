from django.urls import path
from . import views
# from store.views import Aboutus, Services

urlpatterns =[
    path('', views.Index, name='index'),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('aboutus/', views.Aboutus, name='aboutus'),
    path('services/', views.Services, name='services'),
    path('contactus/', views.Contactus, name='contactus'),
    path('feedback/', views.Feedback, name='feedback'),
    path('supplier/', views.Supplierdet, name='supplier'),
    path('product/', views.Productdet, name='product'),

]