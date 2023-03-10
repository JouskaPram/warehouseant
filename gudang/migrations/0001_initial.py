# Generated by Django 4.1.5 on 2023-01-14 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_penyetuju', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Suplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_suplier', models.CharField(max_length=40)),
                ('datasup', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Preorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produk', models.CharField(max_length=50)),
                ('bahan', models.CharField(max_length=10)),
                ('warna', models.CharField(max_length=30)),
                ('ukuran', models.CharField(max_length=30)),
                ('qty', models.IntegerField(null=True)),
                ('harga', models.IntegerField(null=True)),
                ('nama_penulis', models.CharField(max_length=40)),
                ('proved_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gudang.proved')),
                ('suplier_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gudang.suplier')),
            ],
        ),
    ]
