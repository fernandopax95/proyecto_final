from django import forms
from mascota.models import Mascota, Vacuna


class VacunaForm(forms.ModelForm):

	class Meta:
		model = Vacuna
		fields = [
			'nombre',			
		]
		labels = {
			'nombre': 'Nombre de la Vacuna',
					
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
		}


class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'folio',
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'imagen',
            'persona',
            'vacuna',
        ]
        labels = {
            'folio': 'Id mascota',
            'nombre': 'Nombre de la mascota',
            'sexo': 'Sexo de la mascota',
            'edad_aproximada': 'Edad Aproximada',
            'fecha_rescate': 'Fecha de Rescate',
            'imagen': 'Foto de la mascota',
            'persona': 'Adoptante',
            'vacuna': 'Vacuna',

        }
        widgets = {
            'folio': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.DateInput(attrs={'class':'form-control'}),
            'imagen': forms.FileInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }
        type = {
            'vacuna': 'radio',
        }