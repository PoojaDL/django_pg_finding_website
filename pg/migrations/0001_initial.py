# Generated by Django 4.1.1 on 2022-09-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pg_owner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('pgname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100, null=True)),
                ('fees', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('amenities', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('r_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('duration', models.CharField(max_length=20)),
                ('sharing', models.CharField(max_length=20)),
                ('purpose', models.CharField(max_length=200)),
            ],
        ),
    ]
