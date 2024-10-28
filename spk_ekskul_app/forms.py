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
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(PenilaianForm, self).__init__(*args, **kwargs)

        # Filter untuk kolom C1 dan menampilkan nama namun saat disimpan akan mengambil nilainya
        self.fields['c1'].queryset = SubKriteria.objects.filter(kriteria__simbol='C1').order_by('nama')
        self.fields['c1'].label_from_instance = lambda obj: obj.nama

        # Filter untuk kolom C2 dan menampilkan nama namun saat disimpan akan mengambil nilainya
        self.fields['c2'].queryset = SubKriteria.objects.filter(kriteria__simbol='C2').order_by('nama')
        self.fields['c2'].label_from_instance = lambda obj: obj.nama

        # Filter untuk kolom C3 dan menampilkan nama namun saat disimpan akan mengambil nilainya
        self.fields['c3'].queryset = SubKriteria.objects.filter(kriteria__simbol='C3').order_by('nama')
        self.fields['c3'].label_from_instance = lambda obj: obj.nama

        # Filter untuk kolom C4 dan menampilkan nama namun saat disimpan akan mengambil nilainya
        self.fields['c4'].queryset = SubKriteria.objects.filter(kriteria__simbol='C4').order_by('nama')
        self.fields['c4'].label_from_instance = lambda obj: obj.nama