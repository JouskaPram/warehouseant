from django.db import models
from django.db.models import F , ExpressionWrapper, FloatField
# Create your models here.
class Suplier(models.Model):
    nama_suplier=models.CharField(max_length=40)
    datasup = models.TextField()
    def __str__(self):
        return self.nama_suplier

class Proved(models.Model):
    nama_penyetuju = models.CharField(max_length=35)
    alasan = models.CharField(max_length=80)
    def __str__(self):
        return self.nama_penyetuju


class Preorder(models.Model):
    produk = models.CharField(max_length=50,blank=True)
    bahan = models.CharField(max_length=10,blank=True)
    warna = models.CharField(max_length=30,blank=True)
    ukuran = models.CharField(max_length=30,blank=True)
    qty = models.IntegerField(null=True,blank=True)
    harga = models.IntegerField(null=True,blank=True)
    nama_penulis = models.CharField(max_length=40,blank=True)
    proved_id = models.ForeignKey(Proved,on_delete=models.CASCADE,null=True,blank=True)
    suplier_id =models.ForeignKey(Suplier,on_delete=models.CASCADE,null=True,blank=True)
 


   
    def jumlah(self):
        jumlah = self.qty * self.harga
        return jumlah
    def __str__(self):
        return self.nama_penulis

class Status(models.Model):
    produk = models.CharField(max_length=50)
    bahan = models.CharField(max_length=10)
    warna = models.CharField(max_length=30)
    ukuran = models.CharField(max_length=30)
    qty = models.IntegerField(null=True)
    harga = models.IntegerField(null=True)
    nama_penulis = models.CharField(max_length=40)
    proved_id = models.ForeignKey(Proved,on_delete=models.CASCADE,null=True)
    suplier_id =models.ForeignKey(Suplier,on_delete=models.CASCADE,null=True)
    def jumlah(self):
        jumlah = self.qty * self.harga
        return jumlah