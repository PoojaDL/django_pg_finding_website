# Generated by Django 4.1.1 on 2022-09-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0004_pg_owner_front_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pg_owner',
            name='front_view',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
