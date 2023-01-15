
from django.contrib import admin
from django.urls import path
from gudang.views import *
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminpage',adminpage,name='adminpage'),
    path('tambahpo/',addpreorder,name='tambahpo'),
    path('',base,name='base'),
    path('preorder/',getpo,name="preorder"),
    path('supplier/',suplier,name="suplier"),
    path('app/<int:id_preorder>',appo,name="appo"),
    path('approved-admin/',getappo,name='getappo'),
    path('invoice/<int:id_status>',detail_appo,name="detail_appo"),
    path('approved/',approved,name='approved'),
    path('masuk/',LoginView.as_view(),name="login"),
    path('delete/approved/<int:id_approved>',delete_approved,name='deleteapproved'),
    path('keluar/',LogoutView.as_view(),name="keluar"),
]
