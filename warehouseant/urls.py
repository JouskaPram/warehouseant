
from django.contrib import admin
from django.urls import path
from gudang.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminpage',adminpage),
    path('tambahpo/',addpreorder),
    path('',base),
    path('preorder/',getpo,name="preorder"),
    path('supplier/',suplier,name="suplier"),
    path('app/<int:id_preorder>',appo,name="appo"),
    path('approved/',getappo,name='getappo'),
    path('invoice/<int:id_status>',detail_appo,name="detail_appo")
]
