from django.shortcuts import render, redirect
from gudang.models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def base(req):
    return render(req,'home.html')
# template admin page
def adminpage(req):
    preorder = Preorder.objects.all()
  
    konteks={
        'preorder':preorder,
      
    }
    return render(req,'admin-page.html',konteks)

def getpo(req):
    preorder = Preorder.objects.all()
    row_count = Preorder.objects.count()
    konteks={
        'preorder':preorder,
        'row_count':row_count
       
        
    }
    return render(req,'admin-po.html',konteks)

def addpreorder(req):
    if req.POST:
        form = FormPreorder(req.POST)
        if form.is_valid:
            form.save()
            form=FormPreorder()
            # pesan="data berhasil di tambahkan"
            konteks={
                'form':form,
                # 'pesan':pesan
            }
            return render(req,'tambah-po.html',konteks)
    else:
        form = FormPreorder(req.POST)
        konteks={
                'form':form,
                # 'pesan':pesan
            }
    return render(req,'tambah-po.html',konteks)


def suplier(req):
    sup = Suplier.objects.all()
    konteks={
        "sup":sup
    }
    return render(req,'supplier.html',konteks)
# update unapproved to approved
def appo(req,id_preorder):
    App = Preorder.objects.get(id=id_preorder)
    if req.POST:
        form = Formapp(req.POST,instance=App)
        if form.is_valid():
            data = form.cleaned_data
            Status.objects.create(produk=data['produk'],bahan=data['bahan'],warna=data['warna'],ukuran=data['ukuran'],qty=data['qty'],harga=data['harga'],nama_penulis=data['nama_penulis'],proved_id=data['proved_id'],
            suplier_id=data['suplier_id'])
            Preorder.objects.all().delete()
            return redirect('preorder')
    else:
        form = Formapp(instance=App)
        konteks ={
            'form':form,
            'App':App,
        }

    return render(req,'needapp.html',konteks)
# approved page
def getappo(req):
    status = Status.objects.all()
    konteks={
        'status':status
    }

    return render(req,'appadmin-po.html',konteks)
# detail approved
def detail_appo(req,id_status):
    Allappo = Status.objects.filter(id=id_status).values()
    konteks={
        'Allappo':Allappo
    }

    return render(req,'detail-appo.html',konteks)

# base count
def basecount(req):
    preorder = Preorder.objects.all()
    po_count = Preorder.objects.count()
    status = Status.objects.all()
    appo_count = Status.objects.count()
    konteks={
        'preoder':preorder,
        'po_count':po_count,
        'status':status,
        'appo_count':appo_count
    }
    return render(req,'base.html',konteks)