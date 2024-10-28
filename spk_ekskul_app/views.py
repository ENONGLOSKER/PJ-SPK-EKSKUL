from django.shortcuts import render, redirect, get_object_or_404
from .models import Alternatif, Kriteria, SubKriteria , Ekskul, Penilaian
from .forms import AlternatifForm, KriteriaForm, EkskulForm, PenilaianForm, SubKriteriaForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal

# Create your views here.


# Fungsi signout_form digunakan untuk melakukan logout pengguna dan mengarahkannya kembali ke halaman indeks.
def signout_form(request):
    logout(request)
    return redirect('index')
# Fungsi signin_form digunakan untuk proses login pengguna. Jika metode permintaan adalah POST, maka akan melakukan otentikasi username dan password. Jika berhasil, pengguna akan diarahkan ke dashboard dengan pesan sukses. Jika gagal, akan diberikan pesan error dan diarahkan kembali ke halaman sign-in. Jika pengguna sudah terotentikasi, akan diarahkan ke dashboard.
def sigin_form(request):
    if request.user.is_authenticated:
        return redirect('dsb_alternatif')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Sign in Berhasil, Selamat datang {user}")
            return redirect('dsb_alternatif')
        else:
            messages.error(request, "Sign in Gagal, Silahkan coba kembali!")
            return redirect('index')

    return render(request, 'index.html')



def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    data = Alternatif.objects.all()
    print(data)

    context = {
        'datas': data
    }
    return render(request, 'dashboard_siswa.html', context)

@login_required
def alternatif(request):
    data = Alternatif.objects.all()
    print(data)

    context = {
        'datas': data
    }
    return render(request, 'dashboard_alternatif.html', context)

@login_required
def add_alternatif(request):
    if request.method == 'POST':
        form = AlternatifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dsb_alternatif')
    else:
        form = AlternatifForm()

    context ={
        'form':form,
    }
    return render(request,'dashboard_form.html',context)

@login_required
def update_alternatif(request, id):
    alternatif = get_object_or_404(Alternatif, id=id)
    if request.method == 'POST':
        form = AlternatifForm(request.POST, instance=alternatif)
        if form.is_valid():
            form.save()
            return redirect('dsb_alternatif')
    else:
        form = AlternatifForm(instance=alternatif)
    context = {
        'form':form
    }
    return render(request,'dashboard_form.html',context)

@login_required
def delet_alternatif(request,id):
    alternatif = get_object_or_404(Alternatif, id=id)
    alternatif.delete()
    return redirect('dsb_alternatif')

@login_required
def kriteria(request):
    
    data = Kriteria.objects.all()
    print (data)

    context = {
        'datas' : data
    }
    return render(request, 'dashboard_kriteria.html', context)

@login_required
def add_kriteria(request):
    if request.method == 'POST':
        form = KriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dsb_kriteria')
    else:
        form = KriteriaForm()

    context ={
        'form':form,
    }
    return render(request,'dashboard_form.html',context)

@login_required
def update_kriteria(request, id):
    kriteria = get_object_or_404(Kriteria, id=id)
    if request.method == 'POST':
        form = KriteriaForm(request.POST, instance=kriteria)
        if form.is_valid():
            form.save()
            return redirect('dsb_kriteria')
    else:
        form = KriteriaForm(instance=kriteria)
    context = {
        'form':form
    }
    return render(request,'dashboard_form.html',context)

@login_required
def delet_kriteria(request,id):
    kriteria = get_object_or_404(Kriteria, id=id)
    kriteria.delete()
    return redirect('dsb_kriteria')

@login_required
def subkriteria_list(request, id):
    kriteria = Kriteria.objects.get(id=id)
    subkriterias = SubKriteria.objects.filter(kriteria=kriteria)
    context = {
        'kriteria': kriteria,
        'subkriterias': subkriterias
    }
    return render(request, 'dashboard_sub_kriteria.html', context)

@login_required
def subkriteria_create(request):
    if request.method == 'POST':
        form = SubKriteriaForm(request.POST)
        if form.is_valid():
            subkriteria = form.save()
            return redirect('subkriteria_list', id=subkriteria.kriteria.id)
    else:
        form = SubKriteriaForm()
    return render(request, 'dashboard_form.html', {'form': form})

@login_required
def subkriteria_update(request, id):
    subkriteria = get_object_or_404(SubKriteria, id=id)
    if request.method == 'POST':
        form = SubKriteriaForm(request.POST, instance=subkriteria)
        if form.is_valid():
            subkriteria = form.save()
            return redirect('subkriteria_list', id=subkriteria.kriteria.id)
    else:
        form = SubKriteriaForm(instance=subkriteria)
    return render(request, 'dashboard_form.html', {'form': form})

@login_required
def subkriteria_delete(request, id):
    subkriteria = get_object_or_404(SubKriteria, id=id)
    kriteria_id = subkriteria.kriteria.id
    if request.method == 'POST':
        subkriteria.delete()
        return redirect('subkriteria_list', id=kriteria_id)
    else:
        # Jika request bukan POST, render halaman konfirmasi atau handle lainnya
        return HttpResponse("Invalid request method. Please delete using POST request.")
@login_required
def ekskul_list(request):
    ekskuls = Ekskul.objects.all()
    return render(request, 'dashboard_ekskul.html', {'ekskuls': ekskuls})

@login_required
def ekskul_create(request):
    if request.method == 'POST':
        form = EkskulForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ekskul_list')
    else:
        form = EkskulForm()
    return render(request, 'dashboard_form.html', {'form': form})

@login_required
def ekskul_update(request, id):
    ekskul = get_object_or_404(Ekskul, id=id)
    if request.method == 'POST':
        form = EkskulForm(request.POST, instance=ekskul)
        if form.is_valid():
            form.save()
            return redirect('ekskul_list')
    else:
        form = EkskulForm(instance=ekskul)
    return render(request, 'dashboard_form.html', {'form': form})

@login_required
def ekskul_delete(request, id):
    ekskul = get_object_or_404(Ekskul, id=id)
    ekskul.delete()
    return redirect('ekskul_list')

# PENILAIAN CRUD
@login_required
def penilaian_list(request):
    penilaians = Penilaian.objects.all()
    kriteria_bobot = Kriteria.objects.values('nama', 'bobot','jenis')
    jlh_bobot = sum(kriteria['bobot'] for kriteria in kriteria_bobot)
    jlh_item_bobot = [{'nama': item['nama'], 'bobot': item['bobot'] / jlh_bobot, 'jenis': item['jenis']} for item in kriteria_bobot]
    # tahap 1 mencari niali pangkat sesuia dengan jenis kriteria
    hasil_pangkat = {
        item['nama']: item['bobot'] * (1 if item['jenis'] == 'BENEFIT' else -1)
        for item in jlh_item_bobot
    }

    tabel_penilaian = [
        {
            'no': idx + 1,
            'alternatif': p.alternatif,
            'ekskul': p.ekskul,
            'c1': p.c1.nilai ** Decimal(hasil_pangkat['Minat']),
            'c2': p.c2.nilai ** Decimal(hasil_pangkat['Prestasi']),
            'c3': p.c3.nilai ** Decimal(hasil_pangkat['Waktu']),
            'c4': p.c4.nilai ** Decimal(hasil_pangkat['Biaya']),
            'hasil': (
                (p.c1.nilai ** Decimal(hasil_pangkat['Minat'])) *
                (p.c2.nilai ** Decimal(hasil_pangkat['Prestasi'])) *
                (p.c3.nilai ** Decimal(hasil_pangkat['Waktu'])) *
                (p.c4.nilai ** Decimal(hasil_pangkat['Biaya']))
            )
        }
        for idx, p in enumerate(penilaians)
    ]
    

    # -------------------------
   
    context = {
        'penilaians': penilaians,
        'bobot': kriteria_bobot,
        'jlh_bobot': jlh_bobot,
        'jlh_item_bobot': jlh_item_bobot,
        'hasil_pangkat': hasil_pangkat,
        'tabel_penilaian': tabel_penilaian,
    }
    return render(request, 'dashboard_penilaian.html', context)

@login_required
def penilaian_create(request):
    if request.method == 'POST':
        form = PenilaianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('penilaian_list')
    else:
        form = PenilaianForm()
    return render(request, 'dashboard_form.html', {'form': form})

@login_required
def penilaian_update(request, id):
    penilaian = get_object_or_404(Penilaian, id=id)
    if request.method == 'POST':
        form = PenilaianForm(request.POST, instance=penilaian)
        if form.is_valid():
            form.save()
            return redirect('penilaian_list')
    else:
        form = PenilaianForm(instance=penilaian)
    return render(request, 'dashboard_form.html', {'form': form})

@login_required
def penilaian_delete(request, id):
    penilaian = get_object_or_404(Penilaian, id=id)
    penilaian.delete()
    return redirect('penilaian_list')

def get_subkriteria(request):
    kriteria_id = request.GET.get('kriteria_id')
    subkriteria = SubKriteria.objects.filter(kriteria_id=kriteria_id).values('id', 'nama')  # Ganti 'nama' dengan field yang sesuai

    return JsonResponse(list(subkriteria), safe=False)