from django.shortcuts import render, redirect, get_object_or_404
from .models import Alternatif, Kriteria, SubKriteria , Ekskul, Penilaian
from .forms import AlternatifForm, KriteriaForm, EkskulForm, PenilaianForm, SubKriteriaForm
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'dashboard.html')
def dashboard(request):
    data = Alternatif.objects.all()
    print (data)

    context = {
        'datas' : data
    }
    return render(request, 'dashboard_siswa.html', context)
def alternatif(request):
    data = Alternatif.objects.all()
    print (data)

    context = {
        'datas' : data
    }
    return render(request, 'dashboard_alternatif.html', context)

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

def delet_alternatif(request,id):
    alternatif = get_object_or_404(Alternatif, id=id)
    alternatif.delete()
    return redirect('dsb_alternatif')

def kriteria(request):
    
    data = Kriteria.objects.all()
    print (data)

    context = {
        'datas' : data
    }
    return render(request, 'dashboard_kriteria.html', context)

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

def delet_kriteria(request,id):
    kriteria = get_object_or_404(Kriteria, id=id)
    kriteria.delete()
    return redirect('dsb_kriteria')


def subkriteria_list(request, id):
    kriteria = Kriteria.objects.get(id=id)
    subkriterias = SubKriteria.objects.filter(kriteria=kriteria)
    context = {
        'kriteria': kriteria,
        'subkriterias': subkriterias
    }
    return render(request, 'dashboard_sub_kriteria.html', context)

def subkriteria_create(request):
    if request.method == 'POST':
        form = SubKriteriaForm(request.POST)
        if form.is_valid():
            subkriteria = form.save()
            return redirect('subkriteria_list', id=subkriteria.kriteria.id)
    else:
        form = SubKriteriaForm()
    return render(request, 'dashboard_form.html', {'form': form})

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

def subkriteria_delete(request, id):
    subkriteria = get_object_or_404(SubKriteria, id=id)
    kriteria_id = subkriteria.kriteria.id
    if request.method == 'POST':
        subkriteria.delete()
        return redirect('subkriteria_list', id=kriteria_id)
    else:
        # Jika request bukan POST, render halaman konfirmasi atau handle lainnya
        return HttpResponse("Invalid request method. Please delete using POST request.")
def ekskul_list(request):
    ekskuls = Ekskul.objects.all()
    return render(request, 'dashboard_ekskul.html', {'ekskuls': ekskuls})

def ekskul_create(request):
    if request.method == 'POST':
        form = EkskulForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ekskul_list')
    else:
        form = EkskulForm()
    return render(request, 'dashboard_form.html', {'form': form})

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

def ekskul_delete(request, id):
    ekskul = get_object_or_404(Ekskul, id=id)
    ekskul.delete()
    return redirect('ekskul_list')

# PENILAIAN CRUD
def penilaian_list(request):
    penilaians = Penilaian.objects.all()
    return render(request, 'penilaian_list.html', {'penilaians': penilaians})

def penilaian_create(request):
    if request.method == 'POST':
        form = PenilaianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('penilaian_list')
    else:
        form = PenilaianForm()
    return render(request, 'penilaian_form.html', {'form': form})

def penilaian_update(request, pk):
    penilaian = get_object_or_404(Penilaian, pk=pk)
    if request.method == 'POST':
        form = PenilaianForm(request.POST, instance=penilaian)
        if form.is_valid():
            form.save()
            return redirect('penilaian_list')
    else:
        form = PenilaianForm(instance=penilaian)
    return render(request, 'penilaian_form.html', {'form': form})

def penilaian_delete(request, pk):
    penilaian = get_object_or_404(Penilaian, pk=pk)
    if request.method == 'POST':
        penilaian.delete()
        return redirect('penilaian_list')
    return render(request, 'penilaian_confirm_delete.html', {'penilaian': penilaian})