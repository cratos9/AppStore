from django import forms

class Post(forms.Form):
    title = forms.CharField(max_length=100, label="Titulo:", required=True, widget=forms.TextInput(attrs={'Class':'form--campos'}))
    desc = forms.CharField(max_length=300, label="Descripcion", required=True, widget=forms.Textarea(attrs={'Class':'form--campos'}))
    price = forms.FloatField(label="Precio", required=True, widget=forms.NumberInput(attrs={'Class':'form--campos'}))
    photo = forms.ImageField(label="Imagen del producto", required=True, widget=forms.ClearableFileInput(attrs={'Class':'form--campos'}))