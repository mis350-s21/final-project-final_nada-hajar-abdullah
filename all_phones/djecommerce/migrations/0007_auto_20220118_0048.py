# Generated by Django 3.2.9 on 2022-01-17 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djecommerce', '0006_product_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='model',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='djecommerce.customer')),
            ],
        ),
    ]