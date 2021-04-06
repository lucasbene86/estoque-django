from django import forms

class CadastroForms(forms.Form):
    nome = forms.CharField(label='Nome')