# Generated by Django 4.2.7 on 2023-12-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplication', '0004_articulos_compra_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='Nompro',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]