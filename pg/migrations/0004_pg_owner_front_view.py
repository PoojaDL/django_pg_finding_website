# Generated by Django 4.1.1 on 2022-09-22 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0003_remove_pg_owner_r_password_pg_owner_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='pg_owner',
            name='front_view',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
