from django.db import models
from django.forms import fields
from .models import  amenitie
from django import forms


# class UserImage(forms.ModelForm):
#     class meta:
#         # To specify the model to be used to create form
#         models = UploadImage
#         # It includes all the fields of model
#         fields = '__all__'
#         # in same way create form for that table i really don't know this upside code i copied from google


class AmenitiesForm(forms.ModelForm):
    class Meta:
        model = amenitie
        fields = '__all__'



