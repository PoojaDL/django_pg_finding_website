# Generated by Django 4.1.1 on 2022-09-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0009_alter_pg_owner_front_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='pg_owner',
            name='any_view',
            field=models.ImageField(blank='True', null=True, upload_to='baduku'),
        ),
        migrations.AddField(
            model_name='pg_owner',
            name='bed_room',
            field=models.ImageField(blank='True', null=True, upload_to='baduku'),
        ),
    ]
