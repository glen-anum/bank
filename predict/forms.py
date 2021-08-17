from django.forms import ModelForm

from django import forms

from .models import PredResults

class Pred_Results(ModelForm):
	class Meta:
		model = PredResults
		fields = '__all__'
		exclude = ['classification']