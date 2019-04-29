from django.db import models

# Create your models here.
from django.db import models
from django import forms

class MyForm(forms.Form):
    nom_commune = forms.CharField(widget=forms.HiddenInput(), required=False)
    total_prod = forms.CharField(widget=forms.HiddenInput(), required=False)
    prod_eolien = forms.CharField(widget=forms.HiddenInput(), required=False)
    prod_hydraulique = forms.CharField(widget=forms.HiddenInput(), required=False)
    prod_photovoltaique = forms.CharField(widget=forms.HiddenInput(), required=False)
    prod_bioenergie = forms.CharField(widget=forms.HiddenInput(), required=False)
    prod_indiv = forms.CharField(widget=forms.HiddenInput(), required=False)
    note = forms.CharField(widget=forms.HiddenInput(), required=False)
    population = forms.CharField(widget=forms.HiddenInput(), required=False)
    prod_cogénération = forms.CharField(widget=forms.HiddenInput(), required=False)
