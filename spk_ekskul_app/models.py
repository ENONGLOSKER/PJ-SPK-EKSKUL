from django.db import models

# Create your models here.
class Alternatif(models.Model): #untuk siswa
    simbol = models.CharField(max_length=5)
    nama = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nama
    
class Kriteria(models.Model):
    JS = [('BENEFIT', 'BENEFIT'),('COST','COST')]

    simbol = models.CharField(max_length=5)
    nama = models.CharField(max_length=50)
    bobot = models.FloatField(default=0)  # Nilai bobot antara 0-1
    jenis = models.CharField(choices=JS, default='benefit', max_length=10)

    def __str__(self) -> str:
        return self.nama
    
class SubKriteria(models.Model):
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE, related_name='subkriteria')
    nama = models.CharField(max_length=100)
    nilai = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"{self.nama} (Nilai: {self.nilai})"

class Ekskul(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Penilaian(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE, related_name='penilaian')
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE, related_name='penilaian')
    nilai = models.FloatField()  # Nilai penilaian untuk setiap kriteria

    def __str__(self):
        return f"{self.alternatif.nama} - {self.kriteria.nama} (Nilai: {self.nilai})"

