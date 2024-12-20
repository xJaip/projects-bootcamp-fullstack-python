from django import forms
from .models import Vehiculo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria','serial_motor', 'categoria', 'precio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Agregar Vehículo'))
