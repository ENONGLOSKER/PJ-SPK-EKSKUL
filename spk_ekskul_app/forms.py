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
        fields = ['simbol', 'nama','jenis']

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
        fields = ['siswa', 'ekskul', 'kriteria', 'sub_kriteria', 'nilai']