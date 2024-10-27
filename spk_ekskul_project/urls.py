"""
URL configuration for spk_ekskul_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# static
from django.conf import settings
from django.conf.urls.static import static
from spk_ekskul_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('auth/signin/', views.sigin_form, name='sigin_form'),
    path('auth/signout/', views.signout_form, name='signout_form'),
    path('dashboard/siswa/', views.dashboard, name='dsb_siswa'),
    path('dashboard/alternatif/', views.alternatif, name='dsb_alternatif'),
    path('dashboard/alternatif/add/', views.add_alternatif, name='add_alternatif'),
    path('dashboard/alternatif/update/<int:id>/', views.update_alternatif, name='update_alternatif'),
    path('dashboard/alternatif/delet/<int:id>/', views.delet_alternatif, name='delet_alternatif'),

    path('dashboard/kriteria/', views.kriteria, name='dsb_kriteria'),
    path('dashboard/kriteria/add/', views.add_kriteria, name='add_kriteria'),
    path('dashboard/kriteria/update/<int:id>/', views.update_kriteria, name='update_kriteria'),
    path('dashboard/kriteria/delet/<int:id>/', views.delet_kriteria, name='delet_kriteria'),

    # SubKriteria URLs
    path('subkriteria/<int:id>/', views.subkriteria_list, name='subkriteria_list'),
    path('subkriteria/create/', views.subkriteria_create, name='subkriteria_create'),
    path('subkriteria/update/<int:id>/', views.subkriteria_update, name='subkriteria_update'),
    path('subkriteria/delete/<int:id>/', views.subkriteria_delete, name='subkriteria_delete'),

    path('ekskul/', views.ekskul_list, name='ekskul_list'),
    path('ekskul/create/', views.ekskul_create, name='ekskul_create'),
    path('ekskul/update/<int:id>/', views.ekskul_update, name='ekskul_update'),
    path('ekskul/delete/<int:id>/', views.ekskul_delete, name='ekskul_delete'),

    # Penilaian URLs
    path('penilaian/', views.penilaian_list, name='penilaian_list'),
    path('penilaian/create/', views.penilaian_create, name='penilaian_create'),
    path('penilaian/update/<int:id>/', views.penilaian_update, name='penilaian_update'),
    path('penilaian/delete/<int:id>/', views.penilaian_delete, name='penilaian_delete'),
    path('get-subkriteria/',  views.get_subkriteria, name='get_subkriteria'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

