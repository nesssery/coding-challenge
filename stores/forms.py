from django import forms
from stores.models import Model3d

class CustomCreationModel3DForm(forms.Form):

    title = forms.CharField(
        max_length=256,
        required=True,
        label="Donner un titre avec votre image",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Le titre de votre image"})
    )
    description = forms.CharField(
        max_length=1048576,
        required=True,
        label="Donner une courte description de couverture",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Donner une courte description de couverture", 'rows': 5, 'cols': 40})
    )

    image = forms.ImageField(
        label="Image 3D",
        required=True,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
