from django.forms import ModelForm


class RutaForm(forms.Form):
    mane = forms.CharField()
    message = forms.CharField( widget=forms.Textarea)

    def send_email(self):
        pass