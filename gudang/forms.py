from django.forms import ModelForm
from gudang.models import *
from django import forms




class FormPreorder(ModelForm):
    class Meta:
        model=Preorder
        exclude = ("proved_id",)

    widgets={
        'produk':forms.TextInput(attrs=
            {
            'class':'input-forms'
        }),
        'bahan':forms.TextInput(
            attrs={
            'class':'input-forms'
        }),
        'warna':forms.TextInput(attrs=
        {
            'class':'input-forms'
        }),
        'ukuran':forms.TextInput(attrs=
            {
            'class':'input-forms'
        }),
        'qty':forms.NumberInput(attrs={
            'class':'input-forms'
        }),
        'harga':forms.NumberInput(attrs={
            'class':'input-forms'
        }),
        'nama_penulis':forms.TextInput(attrs={
            'class':'input-forms'
        }),
          
    }
class Formapp(ModelForm):
    class Meta:
        model=Preorder
        fields = "__all__"

  