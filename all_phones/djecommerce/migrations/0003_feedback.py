# Generated by Django 3.2.9 on 2022-01-09 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djecommerce', '0002_rename_products_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('feedback', models.TextField()),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djecommerce.product')),
            ],
        ),
    ]