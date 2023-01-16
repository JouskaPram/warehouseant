from django.shortcuts import render, redirect
from gudang.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your views here.
def base(req):
    return render(req,'home.html')
# template admin page
@login_required(login_url='masuk')
def adminpage(req):
    preorder = Preorder.objects.all()
  
    konteks={
        'preorder':preorder,
      
    }
    return render(req,'admin-page.html',konteks)
@login_required(login_url='masuk')
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
            pesan="data berhasil di tambahkan"
            konteks={
                'form':form,
                'pesan':pesan,
            }
            return render(req,'tambah-po.html',konteks)
    else:
        form = FormPreorder(req.POST)
        konteks={
                'form':form,
                
            }
    return render(req,'tambah-po.html',konteks)

@login_required(login_url='masuk')
def suplier(req):
    sup = Suplier.objects.all()
    konteks={
        "sup":sup
    }
    return render(req,'supplier.html',konteks)
# update unapproved to approved


@login_required(login_url='masuk')
def appo(req,id_preorder):
    App = Preorder.objects.get(id=id_preorder)
    if req.POST:
        form = Formapp(req.POST,instance=App)
        if form.is_valid():
            data = form.cleaned_data
            Status.objects.create(produk=data['produk'],bahan=data['bahan'],warna=data['warna'],ukuran=data['ukuran'],qty=data['qty'],harga=data['harga'],nama_penulis=data['nama_penulis'],proved_id=data['proved_id'],
            suplier_id=data['suplier_id'])
            Preorder.objects.filter(id=id_preorder).delete()
            pesan='data berhasil di ubah'
            konteks ={
            'pesan':pesan,
            'form':form,
            'App':App,
                }
            
            return render(req,'needapp.html',konteks)
            
    else:
        form = Formapp(instance=App)
        konteks ={
         
            'form':form,
            'App':App,
        }

    return render(req,'needapp.html',konteks)
# approved page
@login_required(login_url='masuk')
def getappo(req):
    status = Status.objects.all()
    konteks={
        'status':status
    }

    return render(req,'appadmin-po.html',konteks)
# detail approved

def detail_appo(req,id_status):
    # author = Suplier.objects.get(nama_suplier='irfan')
    Allappo = Status.objects.filter(id=id_status).values()
    jumlah = Status.objects.annotate(sum_fields=F('harga') * F('qty'))
    konteks={
        'Allappo':Allappo,
        'jumlah':jumlah
       
    }

    return render(req,'detail-appo.html',konteks)

# base count
@login_required(login_url='masuk')
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

#page awal approved
def approved(req):
    status = Status.objects.all()
    konteks={
        'status':status
    }

    return render(req,'approved.html',konteks)

def delete_approved(req,id_approved):
    approved = Status.objects.filter(id=id_approved)
    approved.delete()
    pesan = "delete berhasil di lakukan"
    konteks={
        'pesan':pesan
    }

    return render(req,'appadmin-po.html',konteks)

# tambah suplier
@login_required(login_url='masuk')
def tambah_suplier(req):
    if req.POST:
        form = FormSuplier(req.POST)
        if form.is_valid:
            form.save()
            form=FormSuplier()
            pesan="data berhasil di tambahkan"
            konteks={
                'form':form,
                
            }
            return redirect('/supplier/',konteks)
    else:
        form = FormSuplier(req.POST)
        konteks={
                'form':form,
            
            }
    return render(req,'tambahsup.html',konteks)

def dashboard(req):
    preorder = Preorder.objects.all()
    po_count = Preorder.objects.count()
    status = Status.objects.all()
    appo_count = Status.objects.count()
    suplier = Suplier.objects.all()
    suplier_count = Suplier.objects.count()
    konteks={
        'preorder':preorder,
        'po_count':po_count,
        'status':status,
        'appo_count':appo_count,
        'suplier':suplier,
        'suplier_count':suplier_count
    }
    return render(req,'dashboard.html',konteks)