# Generated by Django 4.1.1 on 2022-09-24 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0012_alter_pg_owner_contact_alter_pg_owner_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='pg_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pg.pg_owner'),
            preserve_default=False,
        ),
    ]