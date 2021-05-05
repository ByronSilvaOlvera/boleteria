from django.forms import ModelForm
from .models import ViajeRuta

class RutaForm(ModelForm):
    class Meta:
        model   = ViajeRuta
        fields  = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class':'form-control-sm col-sm-4 '})
    