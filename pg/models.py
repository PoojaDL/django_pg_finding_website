from distutils.command.upload import upload
# from msilib import MSIMODIFY_VALIDATE_DELETE
from django.db import models

class amenitie(models.Model):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='amenities/icon', null=True, blank=True)

    def __str__(self):
        return self.name

class pg_owner(models.Model):
    name = models.CharField(max_length=100)
    pgname = models.CharField(max_length=20)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=20, null=True)
    fees = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=15,unique=True)
    amenities = models.CharField(max_length=100)
    front_view = models.ImageField(upload_to='baduku', null=True, blank='True')
    any_view = models.ImageField(upload_to='baduku', null=True, blank='True')
    bed_room = models.ImageField(upload_to='baduku', null=True, blank='True')
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.pgname


class pg_amenities(models.Model):
    pg_id = models.ForeignKey(pg_owner, on_delete=models.CASCADE)
    amenitie = models.ForeignKey(amenitie, on_delete=models.CASCADE)

    def __str__(self):
        return self.pg_id


class student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15,unique=True)
    duration = models.CharField(max_length=20)
    sharing = models.CharField(max_length=20)
    purpose = models.CharField(max_length=200)
    pg_id = models.ForeignKey(pg_owner, on_delete=models.CASCADE)


class adm(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

