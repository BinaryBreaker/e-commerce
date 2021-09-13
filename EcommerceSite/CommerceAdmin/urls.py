from django.urls import path

from   . import views as v


urlpatterns = [
    path('', v.Base, name="Base"),
    path('AddProduct/', v.AddProduct, name="AddProduct"),
    path('UpdateProduct/<int:id>', v.UpdateProduct, name="UpdateProduct"),
    path('AddCategory/', v.AddCategory, name="AddCategory"),
    path('DasBoard/', v.DasBoard, name="DasBoard"),
    path('AllProducts/', v.AllProducts, name="AllProducts"),
    path('Orders/', v.Orders, name="Orders"),
    path('OrdersDetail/', v.OrdersDetail, name="OrdersDetail"),
    path('AllProductItems/<int:count>', v.AllProductItems, name="AllProductItems"),
    path('Search/<str:data>', v.Seacrh, name="Seacrh"),
    path('add/', v.AddProduct, name="AddProduct"),
]
