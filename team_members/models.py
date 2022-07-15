from django.db import models
from django import forms
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

ROLE_CHOICES =(
    ("1", "Regular - can't delete members"),
    ("2", "Admin - can delete members")
)

class TeamMember(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    mobile = models.IntegerField(max_length = 12)
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)
