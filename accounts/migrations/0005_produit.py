# Generated by Django 4.2.16 on 2024-11-13 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_is_staff_alter_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='produits/')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
