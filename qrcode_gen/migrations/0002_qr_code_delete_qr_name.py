# Generated by Django 4.0.6 on 2022-07-23 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode_gen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qr_Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qr_Name', models.CharField(max_length=200, verbose_name='Name')),
                ('Qr_Code', models.ImageField(blank=True, upload_to='qrcode', verbose_name='Code')),
            ],
        ),
        migrations.DeleteModel(
            name='Qr_Name',
        ),
    ]
