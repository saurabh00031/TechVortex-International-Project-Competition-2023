from django import forms


class PasswordGeneratorForm(forms.Form):
    keyword = forms.CharField(max_length=100)
    sizez = forms.IntegerField()