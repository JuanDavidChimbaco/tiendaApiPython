# Generated by Django 4.2.3 on 2023-08-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='catFoto',
        ),
        migrations.AlterField(
            model_name='producto',
            name='proFoto',
            field=models.FileField(null=True, upload_to='fotos/'),
        ),
    ]