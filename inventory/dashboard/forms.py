from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.models import ModelForm
from .models import *

class ProductForm(ModelForm):
	class Meta:
		model=Product
		fields='__all__'