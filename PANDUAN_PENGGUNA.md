# Panduan Pengguna — Optik ZADA Management System
**Versi 8.9.52** · Terakhir diperbarui: 20 Juni 2026

---

## Daftar Isi
1. [Mengenal Sistem & Hak Akses](#1-mengenal-sistem--hak-akses)
2. [Instalasi Aplikasi (PWA)](#2-instalasi-aplikasi-pwa)
3. [Login](#3-login)
4. [Dashboard](#4-dashboard)
5. [Membuat Invoice Baru](#5-membuat-invoice-baru)
6. [Riwayat Transaksi](#6-riwayat-transaksi)
7. [Melunasi DP](#7-melunasi-dp)
8. [Data Customer](#8-data-customer)
9. [Master Data Produk & Stok](#9-master-data-produk--stok)
10. [Pengaturan Toko](#10-pengaturan-toko)
11. [Manajemen Pengguna](#11-manajemen-pengguna)
12. [Backup Data](#12-backup-data)
13. [FAQ & Masalah Umum](#13-faq--masalah-umum)

---

## 1. Mengenal Sistem & Hak Akses

Optik ZADA adalah sistem manajemen toko berbasis web yang berjalan di cloud. Data tersimpan secara otomatis dan dapat diakses dari perangkat manapun selama ada koneksi internet.

### Tingkat Hak Akses

| Role | Siapa | Bisa Apa |
|------|-------|----------|
| **Admin** | Pemilik toko | Semua fitur tanpa batas |
| **Keluarga** | Anggota keluarga pemilik | Semua fitur kecuali Cashflow & zona berbahaya |
| **Staff** | Karyawan | Operasional harian (invoice, riwayat, customer, stok lihat saja) |

> ⚠️ **Penting:** Staff **tidak bisa** menghapus invoice atau customer. Hanya Admin & Keluarga yang bisa.

---

## 2. Instalasi Aplikasi (PWA)

Aplikasi bisa diinstall ke perangkat seperti aplikasi native — tanpa perlu App Store.

### Di Komputer/Laptop (Chrome atau Edge)
1. Buka URL aplikasi di browser
2. Lihat ikon **install** (⊕) di bagian kanan address bar
3. Klik → pilih **"Install"**
4. Aplikasi akan muncul di taskbar dan bisa dibuka tanpa browser

### Di Android
1. Buka URL aplikasi di Chrome
2. Tap menu **⋮** → **"Add to Home Screen"**
3. Konfirmasi → ikon aplikasi muncul di home screen

### Di iPhone/iPad
1. Buka URL aplikasi di Safari
2. Tap ikon **Share** (kotak dengan panah ke atas)
3. Pilih **"Add to Home Screen"**

> 💡 Setelah diinstall, aplikasi bisa dibuka langsung dari taskbar/home screen tanpa perlu membuka browser terlebih dahulu.

---

## 3. Login

1. Buka aplikasi
2. Masukkan **Username** (bukan email) dan **Password**
3. Tekan **Masuk**

### Lupa Password
- Tekan **"Lupa password?"** di bawah tombol Masuk
- Masukkan email yang terdaftar
- Cek inbox email untuk link reset password

> ⚠️ Jika 5 menit tidak ada aktivitas, sistem akan otomatis logout untuk keamanan.

---

## 4. Dashboard

Dashboard menampilkan ringkasan bisnis bulan berjalan.

### Kartu Statistik
| Kartu | Artinya |
|-------|---------|
| **Total Transaksi** | Jumlah invoice bulan ini |
| **Kas Masuk** | Uang yang sudah diterima (DP + pelunasan) bulan ini |
| **Total Profit** | Keuntungan bersih bulan ini |
| **Customer** | Total customer terdaftar |

### Yang Perlu Diperhatikan
- **Banner kuning "stok menipis"** — ada produk yang stok ≤ 3, klik untuk lihat detail
- **Banner oranye "siap diambil"** — ada pesanan yang sudah siap tapi belum diambil customer
- **Transaksi Terakhir** — 5 transaksi terbaru (klik untuk lihat detail)
- **Stok Menipis** — daftar 5 produk dengan stok paling sedikit (kanan bawah)

---

## 5. Membuat Invoice Baru

Ini adalah alur kerja utama harian. Akses via menu **Invoice** atau tombol **+ Invoice Baru** di dashboard.

### Langkah-langkah

**A. Data Customer**
1. Ketik nama customer di kolom **Nama Customer** — sistem akan autocomplete jika sudah pernah transaksi
2. Isi **No. HP** (opsional, untuk kirim WA konfirmasi)
3. Isi **Alamat** dan **Usia** jika perlu

**B. Data Resep Mata** _(khusus kacamata/lensa)_
1. Isi kolom Sph, Cyl, Ax untuk mata kanan (OD) dan kiri (OS)
2. Isi **Add** jika lensa progresif/baca
3. Isi **PD** (pupil distance) jika ada

**C. Pilih Produk**
1. Klik tab **Frame**, **Lensa**, **Softlens**, atau **Aksesoris**
2. Pilih produk dari dropdown atau ketik untuk cari
3. Atur **harga jual** dan **qty**
4. Klik **+ Tambah** untuk masukkan ke keranjang

**D. Pembayaran**
1. Pilih metode: **Tunai**, **Transfer**, atau **QRIS**
2. Jika DP: centang **DP** → isi nominal DP
3. Isi **Tanggal Siap Diambil** jika pesanan kacamata (untuk notif otomatis)

**E. Simpan**
1. Klik **Simpan Invoice**
2. Struk otomatis muncul — bisa **Cetak** atau kirim **WA ke customer**

> ⚠️ Jika stok produk habis (0), invoice tidak bisa disimpan. Perbarui stok terlebih dahulu.

### Quick Invoice dari Halaman Customer
Buka menu **Customer** → cari customer → klik ikon **⊕** di kolom aksi → form invoice terbuka dengan data customer sudah terisi otomatis.

---

## 6. Riwayat Transaksi

Akses via menu **Riwayat**. Menampilkan semua transaksi aktif.

### Filter & Pencarian
- **Cari** — ketik nama customer atau nomor invoice
- **Filter Status** — Semua / Lunas / DP
- **Filter Bulan** — pilih bulan tertentu
- **Urutkan** — Terbaru, Terlama, Tertinggi, Terendah

### Membaca Tabel
| Kolom | Keterangan |
|-------|-----------|
| **No. Invoice** | Format: INV/OZ/DDMMYY/NNNN |
| **Status** | Hijau = Lunas, Oranye = DP belum lunas |
| **Badge Siap Diambil** | Emas = sudah waktunya diambil, Abu = jadwal mendatang |

### Aksi di Tabel
- **Klik baris** → lihat detail invoice lengkap
- **Ikon WA hijau** → kirim konfirmasi transaksi ke customer
- **Ikon bel hijau** → kirim notif "pesanan siap diambil" ke customer _(muncul jika ada tanggal siap)_
- **Ikon merah** → arsipkan invoice _(Admin/Keluarga saja)_

---

## 7. Melunasi DP

Saat customer datang untuk melunasi:

1. Cari invoice di **Riwayat** → klik untuk buka detail
2. Klik tombol **Lunaskan** (kuning/gold)
3. Pilih metode pembayaran pelunasan
4. Konfirmasi → status berubah menjadi **Lunas**

> Status DP yang sudah lewat tanggal siap diambil otomatis muncul di banner dashboard dan sidebar.

---

## 8. Data Customer

Akses via menu **Customer**.

### Menambah Customer
1. Isi formulir di bagian atas: Nama, HP, Alamat, Usia
2. Klik **Tambah Customer**

### Fitur di Tabel Customer
- **Ikon jam** → lihat riwayat transaksi & resep mata customer + tambah catatan internal
- **Ikon ⊕** → buat invoice baru dengan data customer sudah terisi otomatis
- **Ikon merah** → hapus customer _(Admin/Keluarga saja)_

### Catatan Internal Customer
Di modal riwayat customer, terdapat area **Catatan Internal** — bisa diisi catatan khusus (alergi lensa, preferensi frame, dll) yang tidak terlihat oleh customer. Klik **Simpan Catatan** setelah mengisi.

### Import Historis dari Excel
Jika ada data customer lama dari Excel (format resep mata):
1. Pengaturan → **Import Historis Customer**
2. Upload file Excel sesuai template
3. Preview data → konfirmasi import

---

## 9. Master Data Produk & Stok

Akses via menu **Frame / Lensa / Softlens / Aksesoris**.

### Menambah Produk
1. Isi nama, harga modal, harga jual, stok awal
2. Klik **Tambah**

### Update Stok
- Klik **+** atau **−** di kolom stok untuk tambah/kurangi manual
- Stok otomatis berkurang saat invoice disimpan
- Stok otomatis kembali saat invoice diarsipkan

### Import Massal dari Excel
Untuk input banyak produk sekaligus:
1. Klik **Download Template** untuk dapat format Excel yang benar
2. Isi data produk di Excel
3. Upload kembali → produk masuk otomatis

### Export Data Produk
Klik **Unduh Data** untuk export stok terkini ke Excel (untuk backup atau audit stok).

> ⚠️ Produk dengan stok 0 akan **memblokir** pembuatan invoice. Pastikan stok selalu diperbarui.

---

## 10. Pengaturan Toko

Akses via menu **Pengaturan** _(Admin/Keluarga saja)_.

### Info Toko
Isi nama toko, alamat, kota, no. HP, jam operasional, dan footer struk. Informasi ini otomatis muncul di struk, WA customer, dan WA supplier.

### Template WA Supplier
Template pesan WhatsApp saat order lensa ke supplier bisa dikustomisasi. Gunakan placeholder:
- `{supplier}` — nama supplier
- `{customer}` — nama customer
- `{rx_block}` — data resep mata otomatis
- `{lens_block}` — detail lensa
- `{toko_nama}`, `{toko_hp}` — info toko

Klik **Pakai Template Default** untuk kembali ke format bawaan.

### Daftar Supplier Lensa
Tambahkan supplier beserta nomor WA. Saat buat invoice, tombol **Order ke Supplier** akan muncul untuk kirim WA langsung dengan detail resep & lensa.

---

## 11. Manajemen Pengguna

Akses via **Pengaturan → Kelola Pengguna** _(Admin saja)_.

### Menambah Pengguna Baru
1. Klik **Tambah Pengguna**
2. Isi nama, username, email, password, dan pilih role
3. Simpan — pengguna bisa langsung login

### Mengubah Password
Admin bisa reset password pengguna lain dari halaman ini.

> Role pengguna **tidak bisa diubah** oleh siapapun setelah dibuat kecuali Admin langsung di Pengaturan. Ini untuk mencegah karyawan menaikkan akses sendiri.

---

## 12. Backup Data

**Sangat disarankan backup minimal 1x seminggu.**

### Cara Backup
1. Pengaturan → **Backup & Restore**
2. Klik **Backup Data (.json)**
3. File terunduh otomatis — simpan di Google Drive atau folder aman

### Cara Restore
1. Pengaturan → **Backup & Restore**
2. Klik **Pilih File Backup** → pilih file .json hasil backup
3. Review ringkasan perubahan → klik **Restore**

> ⚠️ Restore akan **menimpa** data yang ada. Pastikan sudah backup sebelum restore.

---

## 13. FAQ & Masalah Umum

**Q: Aplikasi tidak muncul data saat buka?**
Pastikan koneksi internet aktif. Data tersimpan di cloud (Firebase) dan butuh internet untuk diload. Jika tetap kosong setelah 30 detik, coba refresh halaman.

**Q: Invoice tidak bisa disimpan?**
Kemungkinan ada produk dengan stok 0 di keranjang. Lihat pesan error di layar — perbarui stok produk tersebut terlebih dahulu.

**Q: Tombol hapus/edit tidak muncul?**
Fitur hapus hanya tersedia untuk role Admin dan Keluarga. Jika login sebagai Staff, tombol tersebut disembunyikan.

**Q: Nomor invoice loncat atau tidak urut?**
Normal terjadi jika ada invoice yang dibuat di hari berbeda. Format nomor: `INV/OZ/DDMMYY/NNNN` — nomor urut (NNNN) reset setiap hari.

**Q: Data customer tidak muncul di autocomplete invoice?**
Customer harus sudah ditambahkan di menu Customer terlebih dahulu, atau pernah ada invoice dengan nama yang sama sebelumnya.

**Q: Notif WA tidak terkirim otomatis?**
WA tidak otomatis — sistem membuka WhatsApp Web/App dengan pesan yang sudah diisi. Pastikan tombol WA diklik, lalu tekan Send di WhatsApp.

**Q: Aplikasi di-logout sendiri?**
Sistem auto-logout setelah 15 menit tidak ada aktivitas untuk keamanan. Login kembali dengan username dan password.

**Q: Lupa username?**
Hubungi Admin toko — username bisa dilihat di Pengaturan → Kelola Pengguna.

---

*Optik ZADA Management System — Dikembangkan khusus untuk kebutuhan operasional toko optik.*
*Untuk bantuan teknis, hubungi pengembang.*
