from django import forms

class loginForm(forms.Form):
    user = forms.CharField(max_length= 50, label= "Usurio:", widget=forms.TextInput(attrs={'Class':'form--campos'}),required = True)
    email = forms.EmailField(label="Correo electronico:", widget=forms.EmailInput(attrs={'Class':'form--campos'}), required=True)
    password = forms.CharField(label="Contrasena:", widget=forms.PasswordInput(attrs={'Class':'form--campos'}), required=True)