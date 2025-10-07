from django.forms import ModelForm
from .models import Video
from django import forms

# Create the form class.

class CreateVideoForm(ModelForm):
    class Meta:
        model=Video
        fields=['MovieID','MovieTitle','Actor1Name','Actor2Name','DirectorName','MovieGenre','ReleaseYear']

class DeleteVideoForm(forms.Form):
    MovieID = forms.IntegerField(label="Enter Movie ID to delete")

class UpdateVideoIDForm(forms.Form):
    MovieID = forms.IntegerField(label="Enter Movie ID to update")