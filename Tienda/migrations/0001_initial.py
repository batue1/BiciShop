# Generated by Django 3.2.7 on 2021-11-05 01:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('Tipo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Pedido',
            fields=[
                ('estadoPedido', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Forma_Pago',
            fields=[
                ('formaPago', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Material_Cuadro',
            fields=[
                ('color', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos_Cabecera',
            fields=[
                ('pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fechahora', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rodado',
            fields=[
                ('rodado', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(36), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Tipos_Bicicleta',
            fields=[
                ('tipo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, max_length=250, validators=[django.core.validators.MaxLengthValidator(250)])),
                ('precio', models.DecimalField(decimal_places=2, default=150000.0, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('cantidad', models.IntegerField(default=0)),
                ('imagen', models.ImageField(upload_to='fotos', verbose_name='Foto')),
                ('usado', models.BooleanField(default=False)),
                ('publicar', models.BooleanField()),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tienda.color')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tienda.material_cuadro')),
                ('rodado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tienda.rodado')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tienda.tipos_bicicleta')),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos_linea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('precioPedido', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tienda.pedidos_cabecera')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tienda.producto')),
            ],
        ),
    ]
