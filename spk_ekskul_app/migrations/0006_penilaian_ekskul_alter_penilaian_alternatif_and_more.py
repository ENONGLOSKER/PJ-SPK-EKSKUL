# Generated by Django 5.0 on 2024-10-26 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spk_ekskul_app', '0005_rename_siswa_penilaian_alternatif_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='penilaian',
            name='ekskul',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='penilaian_ex', to='spk_ekskul_app.ekskul'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='penilaian',
            name='alternatif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penilaian_al', to='spk_ekskul_app.alternatif'),
        ),
        migrations.AlterField(
            model_name='penilaian',
            name='kriteria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penilaian_kr', to='spk_ekskul_app.kriteria'),
        ),
    ]