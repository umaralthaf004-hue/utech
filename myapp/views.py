# myapp/views.py

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponse

# View untuk Merender Halaman One-Page (Home)
def home_view(request):
    """Merender template home.html yang berisi semua section."""
    context = {}
    return render(request, 'home.html', context) 

# View untuk Memproses Formulir Kontak
@require_http_methods(["POST"])
def submit_kontak(request):
    """memproses data yang dikirim dari formulir kontak."""
    
    # Ambil data dari formulir (pastikan attribute 'name' sesuai di HTML)
    nama = request.POST.get('nama')
    email = request.POST.get('email')
    pesan = request.POST.get('pesan')
    
    if not nama or not email or not pesan:
        messages.error(request, 'semua field wajib diisi!')
        return redirect('home') 
    
    # --- Tempatkan Logika Pengiriman Email/Penyimpanan Database di sini ---
    # Contoh: send_mail(...)
    
    messages.success(request, 'Terima kasih! Pesan Anda telah terkirim.')
    
    # Redirect kembali ke halaman home, dengan anchor ke bagian kontak
    return redirect('/#kontak')