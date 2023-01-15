from django.forms import ModelForm
from gudang.models import *
from django import forms




class FormPreorder(ModelForm):
    class Meta:
        model=Preorder
        exclude = ("proved_id",)

    widgets={
        'produk':forms.TextInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'bahan':forms.TextInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'warna':forms.TextInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'ukuran':forms.TextInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'qty':forms.NumberInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'harga':forms.NumberInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'nama_penulis':forms.TextInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
          
    }
class Formapp(ModelForm):
    class Meta:
        model=Preorder
        fields = "__all__"

    widgets={
        'produk':forms.TextInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'bahan':forms.TextInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'warna':forms.TextInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'ukuran':forms.TextInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'qty':forms.NumberInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'harga':forms.NumberInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
        'nama_penulis':forms.TextInput({
            'class':'bg-slate-700 w-24 h-[50px] rounded-md my-3 w-full hover:bg-slate-600 '
        }),
          
    }