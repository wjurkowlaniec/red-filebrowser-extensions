# django imports
from django import forms

class ImageCropDataForm(forms.Form):
    version = forms.CharField(max_length=255, widget=forms.HiddenInput)
    x = forms.IntegerField(widget=forms.HiddenInput, min_value=0)
    y = forms.IntegerField(widget=forms.HiddenInput, min_value=0)
    x2 = forms.IntegerField(widget=forms.HiddenInput, min_value=0)
    y2 = forms.IntegerField(widget=forms.HiddenInput, min_value=0)
