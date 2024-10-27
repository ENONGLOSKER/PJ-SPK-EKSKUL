from django import forms
from .models import Alternatif, Kriteria, SubKriteria, Penilaian, Ekskul

class AlternatifForm(forms.ModelForm):
    class Meta:
        model = Alternatif
        fields = ['simbol', 'nama']

        widgets = {
            'simbol':forms.TextInput(attrs={'class':'form-control'}),
            'nama':forms.TextInput(attrs={'class':'form-control'}),
        }
class KriteriaForm(forms.ModelForm):
    class Meta:
        model = Kriteria
        fields = ['simbol', 'nama','bobot','jenis']

        widgets = {
            'simbol':forms.TextInput(attrs={'class':'form-control'}),
            'nama':forms.TextInput(attrs={'class':'form-control'}),
            'jenis':forms.Select(attrs={'class':'form-control'}),
        }

class SubKriteriaForm(forms.ModelForm):
    class Meta:
        model = SubKriteria
        fields = ['kriteria', 'nama', 'nilai']

class EkskulForm(forms.ModelForm):
    class Meta:
        model = Ekskul
        fields = ['nama']
        
class PenilaianForm(forms.ModelForm):
    class Meta:
        model = Penilaian
        fields = ['alternatif', 'ekskul', 'kriteria', 'nilai']
        widgets = {
            'alternatif': forms.Select(attrs={'class': 'form-control'}),
            'ekskul': forms.Select(attrs={'class': 'form-control'}),
            'kriteria': forms.Select(attrs={'class': 'form-control'}),
            'nilai': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nilai'].queryset = SubKriteria.objects.all()  # Tampilkan semua subkriteria awalnya

    