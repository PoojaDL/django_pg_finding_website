# Generated by Django 4.1.1 on 2022-09-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0011_amenitie_pg_amenities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pg_owner',
            name='contact',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='pg_owner',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]