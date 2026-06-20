# 🗺️ Optik Zada — Development Roadmap
### Target Launch: 20 Juni 2026
> Timeline pengembangan dari fase Beta menuju Production-ready untuk kebutuhan UMKM Optik.

---

## 🏷️ Skema Versi

| Versi | Status | Milestone |
|-------|--------|-----------|
| **v7.7 Beta** | ✅ Dirilis | Starting point — app sebelum sesi pengembangan ini dimulai |
| **v7.8 Beta** | ✅ Dirilis | Week 1: Rx fields, audit log, karyawan lunaskan, reset PW, soft delete, pagination, CSV fix, CI/CD security rules, release notes |
| **v7.9 Beta** | ✅ Dirilis | Cashflow module (pengeluaran operasional, profit bersih, tutup buku) + bug fix layout |
| **v8.0 Beta** | ✅ Dirilis | Critical: auth persistence + network error handling + bug fixes (double popup, item name, currency format, gelar, offline spinner) |
| **v8.1 Beta** | ✅ Dirilis | Username login, auto-create Firebase Auth user, custom domain optik-zada.store, Blaze upgrade, Firebase CDN retry, security fixes |
| **v8.2 Beta** | ✅ Dirilis | Filter bulan di Riwayat Transaksi, data size monitor dengan progress bar + peringatan otomatis 700KB/900KB |
| **v8.3 Beta** | ✅ Dirilis | Badge emas "siap diambil" di sidebar (lewat tglSiap & belum lunas), password reset continue URL ke optik-zada.store |
| **v8.4 Beta** | ✅ Dirilis | Info toko dinamis dari Pengaturan (nama, alamat, HP, jam, footer) — struk, print thermal, WA otomatis update |
| **v8.5 Beta** | ✅ Dirilis | Firestore per-document restructure — invoices/{id}, backward-compat migration UI |
| **v8.5.1 Beta** | ✅ Dirilis | Hotfix: hapus produk & customer pakai modal in-app (bukan `confirm()` native — blocked oleh Chrome desktop) |
| **v8.5.2 Beta** | ✅ Dirilis | Karyawan bisa lihat stok & harga jual produk (frame/lensa/softlens/aksesoris) — harga modal & margin tetap tersembunyi |
| **v8.6 Beta** | ✅ Dirilis | Import massal produk dari Excel (.xlsx) per kategori + template Excel siap pakai; kolom Modal/Margin hilang sepenuhnya di view karyawan |
| **v8.7 Beta** | ✅ Dirilis | Mobile responsive audit (#33), verifikasi email akun baru (#35), laporan profit per produk (#36) |
| **v8.7.1 Beta** | ✅ Dirilis | Autocomplete pencarian produk di form invoice |
| **v8.7.2 Beta** | ✅ Dirilis | Filter/cari di master data semua kategori + import Excel pertahankan stok existing |
| **v8.8.0 Beta** | ✅ Dirilis | Riwayat customer lengkap (#27), dark mode otomatis (#38), tooltip Rx/DP (#39) |
| **v8.9.0 Beta** | ✅ Dirilis | Karyawan: halaman Profil Saya, filter Transaksi Saya di Riwayat, notif stok kritis di dashboard |
| **v8.9.1 Beta** | ✅ Dirilis | Import historis customer dari Excel — deteksi kolom otomatis, preview sebelum import, badge "Historis" di Riwayat |
| **v8.9.2 Beta** | ✅ Dirilis | Manajemen supplier lensa di Pengaturan + Order ke Supplier via WhatsApp langsung dari modal invoice |
| **v8.9.3 Beta** | ✅ Dirilis | Fix: detail lensa double di struk + button invoice overflow di layar kecil |
| **v8.9.4 Beta** | ✅ Dirilis | PD, Dm.A/B, DBL, TP dipisah dari form invoice → diisi post-facto di Riwayat, tidak tampil di struk customer |
| **v8.9.5 Beta** | ✅ Dirilis | Fix tombol aksi master data (FAB pointer-events), HTML escape nama produk/customer, paginasi tengah |
| **v8.9.6 Beta** | ✅ Dirilis | Fix export Cashflow (cross-browser), fix Global Search tidak redirect saat klik hasil |
| **v8.9.7 Beta** | ✅ Dirilis | Fix tanggal 2-digit tahun (1926→2026), salesInvs() filter historis dari semua kalkulasi keuangan |
| **v8.9.8 Beta** | ✅ Dirilis | Import historis simpan ke rxHistory[] customer (bukan invoice), Riwayat & statistik tidak lagi tercemar data import |
| **v8.9.9 Beta** | ✅ Dirilis | Rename peran: Staff & Admin; topbar baru (nama + versi + logout); Release Notes bisa dibuka kapan saja; toast login lebih ramah |
| **v8.9.10 Beta** | ✅ Dirilis | Role baru "Keluarga" — akses penuh kecuali Cashflow & setting sensitif; class `admin-strict` untuk bagian berbahaya di Pengaturan |
| **v8.9.11 Beta** | ✅ Dirilis | Fix bug Hapus Transaksi (renderHistory + error surfacing); Zona Berbahaya redesign; form Customer fix; hapus Release Notes dari Pengaturan |
| **v8.9.12 Beta** | ✅ Dirilis | Template Excel untuk import customer (kolom BON/NAMA/Rx kanan-kiri/PD/ADD); klarifikasi import = data customer + riwayat resep, bukan transaksi |
| **v8.9.13 Beta** | ✅ Dirilis | Stabilisasi prod: surface Firestore write errors (invoice/lunas/arsip/pengukuran) via toast; fix rxHdrRow undeclared bug di importHistorisCustomer |
| **v8.9.14 Beta** | ✅ Dirilis | Item GRATIS (jual=Rp0) bisa masuk invoice jika ada kata "GRATIS" di nama; struk tampil "GRATIS" bukan "Rp0"; stok & profit tetap terhitung |
| **v8.9.15 Beta** | ✅ Dirilis | Cash-basis accounting fix: kas masuk & profit dicatat sesuai kapan uang diterima, bukan tanggal invoice; profit DP invoice dibagi proporsional (dpRatio × profit → bulan DP, lunasRatio × profit → bulan pelunasan) |
| **v8.9.16 Beta** | ✅ Dirilis | Fix Cashflow: `_cfCalc` sekarang cash-basis (dpAmount/lunasAmount bukan tot); profit kotor proporsional; dropdown bulan tambah lunasDate months; bar chart Dashboard ikut tampilkan cross-month pelunasan |
| **v8.9.17 Beta** | ✅ Dirilis | Cashflow transparan: kartu "Alur Kas" waterfall (Penjualan Baru per kategori + Pelunasan Piutang → Kas Masuk → HPP → Profit Kotor → Pengeluaran → Profit Bersih); kartu Pelunasan Piutang di modal Kas Masuk (Dashboard & Laporan); export PDF Cashflow; export CSV Cashflow lebih lengkap (ringkasan + detail invoice + pelunasan + pengeluaran) |
| **v8.9.18 Beta** | ✅ Dirilis | Optimasi kritis Firestore: (1) Enable IndexedDB offline cache — page load berikutnya instant dari cache; (2) Fix bug: config onSnapshot tidak lagi re-fetch semua invoice setiap ada perubahan kecil (hemat 90%+ reads); (3) Tambah invoice onSnapshot inkremental untuk multi-device sync real-time |
| **v8.9.19 Beta** | ✅ Dirilis | Cache lokal otomatis ke localStorage — jika Firestore quota habis/no internet, tampilkan data cache terakhir (≤48 jam) alih-alih halaman kosong; notif error spesifik saat quota habis (reset jam 07.00 WIB); sederhanakan kode initializeFirestore |
| **v8.9.20 Beta** | ✅ Dirilis | Hotfix: revert `initializeFirestore + persistentLocalCache` yang ditambahkan v8.9.18 — menyebabkan app hang di beberapa browser karena setup IndexedDB memblokir koneksi Firestore; kembali ke `getFirestore()` standar |
| **v8.9.21 Beta** | ✅ Dirilis | Diagnostic: tambah toast error di semua jalur load — meta_not_found, migrated=false silent, dan Firestore read error kini tampil sebagai toast dengan pesan spesifik untuk memudahkan debugging |
| **v8.9.22 Beta** | ✅ Dirilis | Versi tampil di topbar (konfirmasi deploy); fix silent Rp0: path `optik-zada/config` tidak ada kini munculkan toast merah (sebelumnya diam-diam reset ke seedDB + save, berpotensi timpa data); APP_VERSION sinkron ke 8.9.22 |
| **v8.9.23 Beta** | ✅ Dirilis | HOTFIX: spinner login 15s → 5s (mencegah user stuck di spinner jika refresh sebelum form muncul); error login lebih jelas (Firestore errors sebelumnya muncul sebagai "username/password salah"); error sesi auto-login kini tampil di form login dengan kode error spesifik |
| **v8.9.24 Beta** | ✅ Dirilis | 🔴 FIX KRITIS: syntax error (kutip kurang di `exportCashflowCSV`, `createdBy?.nama\|\|','']`) menyebabkan SELURUH inline script gagal parse sejak v8.9.17 — app tampil dashboard statik tapi semua tombol mati, login overlay tak muncul, data tak ter-load, & semua toast diagnostik v8.9.21–23 tak pernah jalan. Diperbaiki + validasi `node --check` sebelum rilis |
| **v8.9.25 Beta** | ✅ Dirilis | Security patch: XSS escape semua innerHTML customer/produk/supplier; stok dikembalikan saat invoice diarsipkan (dan dikurangi kembali saat dipulihkan); auto-logout diperpanjang 3 menit → 15 menit |
| **v8.9.26 Beta** | ✅ Dirilis | Format nomor invoice baru `INV/OZ/DDMMYY/NNNN` (counter reset per-tanggal, anti-collision multi-device via dedup `existingBons`); double-submit guard di tombol Simpan; Tutup Buku tegas — blok simpan invoice & pelunasan ke bulan yang sudah ditutup |
| **v8.9.27 Beta** | ✅ Dirilis | Restore data lebih aman (validasi struktur + ringkasan perubahan + auto-backup sebelum timpa); fix bug invoice tidak ter-restore di mode migrated; tombol Export PDF di arsip laporan Tutup Buku |
| **v8.9.28 Beta** | ✅ Dirilis | Ganti semua 9 `confirm()` native ke modal in-app + pending-state pattern — arsip invoice, hapus pengeluaran, tutup buku, reset master, hapus transaksi, reset all, migrasi, dll |
| **v8.9.29 Beta** | ✅ Dirilis | Security: perketat Firestore rules `users/{userId}` — `create` hanya uid sendiri; `update` hanya uid sendiri AND field `role` immutable (blok privilege escalation via REST) |
| **v8.9.30 Beta** | ✅ Dirilis | Hotfix: data kosong setelah login akibat rules v8.9.29 — fix `_ensureDataLoaded()` dipanggil sebelum semua login flows |
| **v8.9.31 Beta** | ✅ Dirilis | Bulk delete master data per kategori — tombol "Hapus Semua" untuk Frame/Lensa/Softlens/Aksesoris dengan konfirmasi modal |
| **v8.9.32 Beta** | ✅ Dirilis | Full audit log semua tindakan hapus — helper `_logAudit()` + semua destructive actions (produk, customer, invoice, supplier, pengeluaran, akun) tercatat ke log audit (maks. 50 entri) |
| **v8.9.33 Beta** | ✅ Dirilis | TP Pengukuran Lensa dipisah jadi Kanan (OD) & Kiri (OS) — backward compat untuk data lama `rx.tp` |
| **v8.9.34 Beta** | ✅ Dirilis | Tambah field Ket. Faset di Pengukuran Lensa — tampil di struk internal, WA supplier, dan CSV export |
| **v8.9.35 Beta** | ✅ Dirilis | Koreksi label Dm.A(L)/Dm.B(T) di form Pengukuran Lensa dan header CSV export (sebelumnya terbalik) |
| **v8.9.36 Beta** | ✅ Dirilis | Kas Masuk per Kategori: breakdown top-3 berubah dari nama produk → nama pembeli + no. invoice |
| **v8.9.37 Beta** | ✅ Dirilis | Kas Masuk per Kategori: tambah daftar produk yang dibeli di baris kedua setiap transaksi |
| **v8.9.38 Beta** | ✅ Dirilis | Tombol "Unduh Data Sekarang" di semua halaman Master Data — export data aktif (stok terkini) ke Excel, format identik template import |
| **v8.9.39 Beta** | ✅ Dirilis | Print thermal: tambah `@page { size: 80mm auto; margin: 0 }` + print media CSS 72mm — hint ke browser/driver soal ukuran kertas thermal roll |
| **v8.9.40 Beta** | ✅ Dirilis | Print thermal BTP3100: sesuaikan @page 80mm, margin 4mm, tombol "Simpan PDF", hint ukuran |
| **v8.9.41 Beta** | ✅ Dirilis | Print thermal: hapus `@page size` — fix rotasi / landscape di printer KASSEN |
| **v8.9.42 Beta** | ✅ Dirilis | Print thermal: `@page { margin: 0mm; size: auto }` + print-color-adjust — suppress header/footer URL Chrome otomatis |
| **v8.9.43 Beta** | ✅ Dirilis | Print thermal: body `width:100%` di media print agar konten mengisi penuh kertas (58mm/80mm); hapus tombol "Simpan PDF"; hint instruksi uncheck Headers and footers di dialog Chrome |
| **v8.9.44 Beta** | ✅ Dirilis | Print thermal: redesain struk — nama toko 16px bold, separator solid/dashed untuk hirarki, layout item baru (qty tag), badge LUNAS 2px border, footer double-line, max-width 72mm |
| **v8.9.45** | ✅ Dirilis | Cetak invoice: Rx 2 baris (R & L terpisah), label Dm.A (Lebar)/Dm.B (Tinggi) lengkap; stok karyawan diblokir (tombol +/- disembunyikan untuk Staff) |
| **v8.9.46** | ✅ Dirilis | Polish hak akses: tombol Edit/Hapus produk admin-only (selaras guard); kartu Backup & Restore admin-strict + guard `restoreData`; rapikan section markers (escape text ═/· + dedup SECTION 22B); **rename file app → `index.html`** |
| **v8.9.47** | ✅ Dirilis | Security: guard semua `_do*` mutators (delCustomer, delInvoice, clearTransactions, resetAll, migrate, supplier); kartu Export admin-only; header CSV Dm.A/B dibenerin; stat Kas Masuk/Profit → admin-strict |
| **v8.9.48** | ✅ Dirilis | Polish UI/UX: topbar ver sync dinamis; badge role invoice pakai label UI (Staff/Keluarga/Admin); typo "progressif"→"progresif"; WA label DM.A/B → Dm.A (Lebar)/Dm.B (Tinggi); item-row mobile fix; tooltip title= pada semua tombol icon-only |
| **v8.9.49** | ✅ Dirilis | Warning stok saat simpan invoice: block jika stok habis (= 0), warn jika qty > stok; notif stok ≤ 2 kini untuk semua kategori (eks-C6/D1) |
| **v8.9.50** | ✅ Dirilis | Firestore rules granular: hapus invoice = admin/keluarga only di level server; `createdBy` immutable di update (anti-impersonation) — perlu deploy manual ke Firebase Console (eks-C4/D2) |
| **v8.9.51** | ✅ Dirilis | Template WA supplier bisa dikustom dari Pengaturan (placeholder `{supplier}`, `{customer}`, `{rx_block}`, dst — eks-C2); fix modal Profit per Kategori untuk skenario profit negatif (warna merah, bar magnitude, tanda `−` proper) |
| **v8.9.52** | ✅ Dirilis | Badge "Siap Diambil" di tabel Riwayat (emas=sudah waktunya, abu=masih jadwal); tombol notif WA siap diambil `btnWASiap()` di tabel + modal detail; Quick Invoice dari halaman Customer (auto-fill nama/HP/alamat); Top 5 Terlaris tampilkan omzet (Rp) di samping qty; Catatan Internal per customer (simpan di modal Riwayat, preview singkat di tabel) |
| **v8.9 RC** | 📋 Planned | Regression test end-to-end, tidak ada fitur baru |
| **v9.0** | 🚀 Target | Production launch — 20 Juni 2026 |

> **Skema:** patch (x.x.Y) = bugfix kecil · minor (x.Y.0) = fitur baru · major (Y.0.0) = perubahan arsitektur besar · RC = Release Candidate

---

## 📊 Status Overview

| Fase | Periode | Versi | Status |
|------|---------|-------|--------|
| Week 1 — Foundation & Beta Features | 20–27 Mei | v7.7 → v7.8 | ✅ Selesai |
| Week 2 — Cashflow + Early Fixes | 28–29 Mei | v7.8 → v7.9 | ✅ Selesai |
| Week 3 — Critical Fixes & UX | 30 Mei – 5 Juni | v7.9 → v8.0 | ✅ Selesai |
| Week 3 lanjutan — Search, Monitor, Infra | 30 Mei – 5 Juni | v8.0 → v8.1 | ✅ Selesai |
| Week 4 — Core Features & Print Thermal | 6–8 Juni | v8.1 → v8.9.44 | ✅ Selesai |
| Week 5 — Pre-Release Polish & Security | 9–17 Juni | v8.9.44 → v8.9 RC | 🔨 Aktif |
| Launch Week | 18–20 Juni | v8.9 RC → v9.0 | 🚀 Target |

---

## ✅ v7.7 → v7.8 Beta — Foundation & Beta Features (20–27 Mei)
> Semua item selesai. Deployed.

| # | Item | Tipe | Versi |
|---|------|------|-------|
| 1 | Resep Mata Lengkap (Dm.A, Dm.B, DBL, TP) | Enhancement | v7.8 |
| 2 | Audit Log Invoice (`createdBy` per invoice) | Enhancement | v7.8 |
| 3 | Karyawan bisa Lunaskan DP | Fix | v7.8 |
| 4 | Reset Password via Email ("Lupa password?") | Feature | v7.8 |
| 5 | Soft Delete / Arsip Invoice + Pulihkan | Feature | v7.8 |
| 6 | Pagination Riwayat (25/halaman) | Enhancement | v7.8 |
| 7 | CSV Export Fix — langsung rapi di Excel, kolom Rx baru ter-export | Fix | v7.8 |
| 8 | Firestore Security Rules — auto deploy via GitHub Actions CI/CD | Security | v7.8 |
| 9 | Release Notes Modal — muncul setelah login, versi terbaru | Feature | v7.8 |

---

## ✅ v7.8 → v7.9 Beta — Cashflow Module (28–29 Mei)
> Selesai. Deployed.

| # | Item | Tipe | Versi |
|---|------|------|-------|
| 10 | **Cashflow Module** — halaman pengeluaran operasional + profit bersih | Major Feature | v7.9 |
| 11 | Admin: 4 stat cards (Kas Masuk, Profit Kotor, Pengeluaran, Profit Bersih) | Feature | v7.9 |
| 12 | Admin: Form catat pengeluaran (6 kategori, tanggal, nominal, keterangan) | Feature | v7.9 |
| 13 | Admin: Tabel riwayat pengeluaran per bulan + delete | Feature | v7.9 |
| 14 | Admin: Breakdown pengeluaran per kategori (progress bar) | Feature | v7.9 |
| 15 | Admin: Tutup Buku bulanan — snapshot terkunci permanen | Feature | v7.9 |
| 16 | Admin: Arsip laporan tertutup + modal detail | Feature | v7.9 |
| 17 | Admin: Export CSV pengeluaran | Feature | v7.9 |
| 18 | Karyawan: Input pengeluaran + view harian saja | Feature | v7.9 |
| 19 | Laporan page: Ringkasan Cashflow card (Profit Kotor → Pengeluaran → Profit Bersih) | Integration | v7.9 |
| 20 | **Bug Fix**: Cashflow page di luar `.main` wrapper → posisi salah di mobile | Critical Fix | v7.9 |

---

## ✅ v7.9 → v8.0 Beta — Critical Fixes & UX (30 Mei – 5 Juni)
> Selesai. Deployed.

### 🔴 CRITICAL

| # | Item | Tipe | Versi | Detail |
|---|------|------|-------|--------|
| 21 | **Fix Auth Persistence** | Critical Fix | v8.0 | `inMemoryPersistence` → `browserLocalStoragePersistence`. Sesi tersimpan di localStorage — user tidak logout setiap refresh. Login panel tampil spinner "Memeriksa sesi aktif..." saat restore. |
| 22 | **Network Error Handling** | Critical Fix | v8.0 | Banner merah slide-down saat offline: "Koneksi terputus — perubahan mungkin belum tersimpan". Hijau saat reconnect. |

### 🟠 BUG FIXES (v8.0 sepaket)

| # | Item | Tipe | Versi |
|---|------|------|-------|
| B1 | Double release notes popup saat login | Bug Fix | v8.0 | Race condition `onAuthStateChanged` vs `doAuthLogin()` — fix double-check `!currentRole` setelah await |
| B2 | Nama item invoice hilang saat tambah item lain | Bug Fix | v8.0 | `renderCart()` tidak mark `selected` pada option yang aktif — fix per-item opts dengan `selected` attribute |
| B3 | Format nominal rupiah tidak konsisten | Bug Fix | v8.0 | Semua input harga (cashflow, produk, cart) kini format ribuan otomatis (1.500.000) |
| B4 | Hapus gelar "Dr." dari dropdown invoice & customer | Bug Fix | v8.0 | Tidak relevan untuk toko optik — dihapus dari semua dropdown + regex |
| B5 | Spinner "Memeriksa sesi aktif..." macet selamanya | Critical Fix | v8.0 | Hard timeout 5 detik di `injectAuthUI()` + timeout 8 detik di `_initFB()` saat offline |

### 🟡 MEDIUM

| # | Item | Tipe | Target Versi | Detail |
|---|------|------|-------------|--------|
| 23 | Search & Filter Riwayat | Feature | ✅ v8.2 | Filter bulan ditambah ke halaman Riwayat. Search nama/invoice + filter status/pembayaran/bulan/sort sudah lengkap. |
| 24 | Data Size Monitor + Warning | Monitoring | ✅ v8.2 | Progress bar di Pengaturan + toast warning otomatis saat login jika data ≥700KB (⚠️) atau ≥900KB (🚨). |
| 25 | Firebase Blaze Plan Setup | Infrastructure | ✅ v8.1 | Upgrade dari Spark free tier — aktif dengan GCP free trial credit Rp5.1jt s/d Agustus 2026. |
| 32 | Custom Domain `optik-zada.store` | Infrastructure | ✅ v8.1 | Domain aktif, SSL auto-provisioned Firebase, authDomain diupdate di kode. |
| 33 | Custom Email Sender `noreply@optik-zada.store` | Infrastructure | ✅ v8.1 | DNS records (SPF + DKIM) ditambahkan, verifikasi Firebase Auth email domain pending (max 48 jam). |
| B6 | **Auto-create Firebase Auth saat tambah karyawan** | Bug Fix | ✅ v8.1 | Admin tidak perlu buka Firebase Console lagi. `createUserWithEmailAndPassword()` + `updateCurrentUser()` untuk restore admin session. Karyawan terima email set-password otomatis. |
| B7 | **Login pakai username** | Feature | ✅ v8.1 | Karyawan login pakai username pendek (contoh: `budi_kasir`) bukan email. Admin set username saat buat akun. Lookup via Firestore `usernames/{username}` → email → Firebase signIn. Email tetap ada untuk reset password. |

---

## 📋 v8.1 → v8.5 Beta — Core Production Features (6–12 Juni)

### 🔵 MAJOR — Architectural

| # | Item | Tipe | Target Versi | Detail |
|---|------|------|-------------|--------|
| 26 | **Firestore Per-Document Restructure** | Major / Architectural | ✅ v8.5 | Setiap invoice disimpan sebagai dokumen `invoices/{id}` terpisah. Config (produk, customer, toko, dll) di `optik-zada/config`. Migration flag di `optik-zada/meta`. Migrasi satu klik dari Pengaturan (Admin). Backward-compatible — app tetap jalan di struktur lama sampai migrasi dijalankan. |

### 🟡 MEDIUM

| # | Item | Tipe | Target Versi | Detail |
|---|------|------|-------------|--------|
| 27 | Riwayat Resep per Customer | Feature | ✅ v8.8.0 | Customer → tombol riwayat → semua invoice (item, total, Rx), diurutkan terbaru. Invoice dengan Rx ditandai badge biru. |
| 28 | List DP Outstanding + WA Blast Reminder | Feature | ⏭️ Skip | Sama konsepnya dengan tombol WA yang sudah ada di riwayat invoice. Tidak perlu duplikasi. |
| 29 | Notif "Siap Diambil" — badge sidebar | Enhancement | ✅ v8.3 | Badge emas di sidebar Riwayat — hitung invoice DP yang sudah lewat tglSiap. Terpisah dari badge merah total DP. |
| 30 | Print Nota Customization | Feature | ✅ v8.4 | Admin edit nama/alamat/HP/jam/footer dari Pengaturan → otomatis update struk modal, print thermal, dan WA. |
| 30 | Print Nota Customization | Feature | v8.3 | Admin bisa edit nama toko, alamat, HP, footer struk dari Settings (saat ini hardcoded). |

---

## 📋 v8.5 → v8.8 RC — Polish & Launch Prep (13–17 Juni)

### 🔵 MAJOR

| # | Item | Tipe | Target Versi | Detail |
|---|------|------|-------------|--------|
| 31 | **Multi-User Concurrent Edit Safety** | Major | v8.6 | Risk overwrite data saat admin dan karyawan edit bersamaan. Implementasi Firestore transactions untuk operasi kritis. |

### 🟡 MEDIUM

| # | Item | Tipe | Target Versi | Detail |
|---|------|------|-------------|--------|
| 32 | Custom Domain Setup | Infrastructure | v8.7 | Ganti URL default Firebase ke domain sendiri (misal `optikzada.com`). |
| 33 | Mobile Responsive Audit | Polish | ✅ v8.7 | `.frow` kolaps ke 1 kolom di <600px, `.modal-box` tidak overflow layar mobile, modal padding dikurangi. |
| 34 | Kompresi Aset (logo.png) | Performance | v8.8 | `assets/logo.png` ~1MB → <100KB via [squoosh.app](https://squoosh.app). Manual oleh user. |
| 35 | Konfirmasi Email Akun Baru | Security | ✅ v8.7 | `requiresEmailVerification:true` di Firestore → verifikasi screen saat login pertama. Email kirim otomatis + tombol resend. |
| 36 | Laporan Profit per Produk | Feature | ✅ v8.7 | Tabel per produk di halaman Laporan (admin): qty terjual, omzet, profit, margin. Diurutkan omzet terbesar. |

### 🟢 NICE TO HAVE

| # | Item | Tipe | Target Versi | Detail |
|---|------|------|-------------|--------|
| 37 | Diskon Global / Promo | Feature | ⏭️ Skip | User prefer input diskon langsung per invoice (field sudah ada). Fitur global tidak diperlukan. |
| 38 | Dark/Light Mode Toggle Otomatis | Enhancement | ✅ v8.8.0 | `prefers-color-scheme` digunakan jika belum ada pilihan manual. `matchMedia` listener — otomatis ikut sistem saat berubah. |
| 39 | Tooltip / Help Onboarding | UX | ✅ v8.8.0 | Tooltip ikon `?` di semua field Rx (Sph, Cyl, Axis, Visus, PD, Add, Dm.A, Dm.B, DBL, TP) + field DP. |
| 40 | Halaman Profil Karyawan | Feature | ✅ v8.9.0 | Halaman "Profil Saya" untuk semua role: nama, email, badge peran, info toko, tombol kirim email ganti password (Firebase mode). |
| 41 | Filter "Transaksi Saya" di Riwayat | Feature | ✅ v8.9.0 | Toggle button di Riwayat Transaksi — filter hanya invoice yang dibuat oleh user yang login (`createdBy.uid`). |
| 42 | Notif Stok Kritis untuk Karyawan | Enhancement | ✅ v8.9.0 | Banner stok menipis di Dashboard kini tampil untuk role karyawan (sebelumnya admin-only). |
| 43 | Import Historis Customer dari Excel | Feature | ✅ v8.9.1 | Upload .xlsx dengan format header bebas (multi-baris). Auto-deteksi kolom Bon, Nama, Usia, HP, Tipe, Rx (R/L Sph/Cyl/Axis/Vis), PD, Add, DM.A/B, DBL, TP. Preview tabel sebelum konfirmasi. Invoice disimpan dengan flag `isHistoris:true` + badge "Historis" abu-abu di Riwayat. |
| 44 | Manajemen Supplier + Order via WhatsApp | Feature | ✅ v8.9.2 | Admin kelola daftar supplier lensa (nama, WA, catatan) dari Pengaturan. Di modal invoice, tombol truk membuka picker supplier → app buka WA dengan pesan order otomatis berisi detail Rx + ukuran lensa + info customer. |
| 45 | Fix Struk & Button Invoice | Bug Fix | ✅ v8.9.3 | (1) Detail lensa di struk tidak lagi double jika lensa diambil dari katalog item. (2) Button WA/Supplier/Thermal dijadikan ikon-only dengan tooltip agar tidak overflow di layar kecil. |
| 46 | Pengukuran Lensa Dipisah dari Invoice | Feature | ✅ v8.9.4 | PD, Dm.A(T), Dm.B(L), DBL, TP dihapus dari form invoice. Diisi post-facto dari modal Riwayat (section "Pengukuran Lensa – Internal / Supplier"). Data tetap diteruskan ke supplier via WA order. Struk customer lebih bersih. |
| 47 | Fix Tombol Aksi + Paginasi Rapi | Bug Fix | ✅ v8.9.5 | (1) FAB container diberi `pointer-events:none` sehingga tidak menutupi tombol tabel di bawahnya. (2) Nama produk/customer di-escape HTML untuk mencegah injeksi. (3) Pagination bar diubah jadi layout tengah ← Hal X/Y · N item → konsisten di semua tabel. |
| 48 | Fix Export Cashflow + Global Search | Bug Fix | ✅ v8.9.6 | (1) Export CSV Cashflow kini pakai `appendChild/click/removeChild` — berfungsi di semua browser. (2) Global search redirect pakai `onmousedown` (sebelum blur) sehingga klik hasil langsung navigasi ke halaman/produk/invoice. |
| 49 | Fix Tanggal Historis + Filter Finansial | Bug Fix | ✅ v8.9.7 | (1) `monthKeyOf()` normalisasi tahun 2-digit (e.g. "26" → 2026). (2) `salesInvs()` — filter baru yang mengecualikan data historis dari semua kalkulasi Dashboard, Laporan, Cashflow. |
| 50 | Import Historis Tanpa Invoice Palsu | Feature | ✅ v8.9.8 | Import historis kini menyimpan data ke `customer.rxHistory[]`, bukan membuat invoice Rp0. Riwayat Transaksi bersih. Profil customer tampil dua seksi: Transaksi & Riwayat Resep Mata (Historis). Backward compat: data lama `isHistoris:true` tetap terbaca. |
| 51 | Rename Peran + Topbar Baru + Login UX | Enhancement | ✅ v8.9.9 | (1) Label peran: "Karyawan" → Staff, "Admin / Pemilik" → Admin (internal key tidak berubah). (2) Topbar badge baru: nama pengguna + tombol versi (klik = Release Notes) + tombol logout. Indikator peran dihapus. (3) Release Notes kini bisa dibuka kapan saja via tombol versi — tidak muncul otomatis saat login. (4) Toast login: "Selamat datang, [nama]!". |
| 52 | Role Baru: Keluarga | Feature | ✅ v8.9.10 | Peran baru antara Admin dan Staff. Akses penuh ke semua fitur kecuali: Cashflow, Kelola Pengguna, Log Audit, Migrasi Data, Zona Berbahaya, Status Penyimpanan. Diimplementasi via class `admin-strict` di HTML dan helper `_isAdminLike()` yang mencakup admin+keluarga di semua logika render. |

---

## 🔍 Audit Produksi — Backlog Temuan (Juni 2026)
> Hasil audit menyeluruh saat app sedang dipakai client (production testing aktif). Dikelompokkan berdasarkan prioritas.

### 🔴 P0 — Harus Sebelum Lebih Banyak Data Masuk

| # | Temuan | Detail | Status |
|---|--------|--------|--------|
| A1 | **Firestore `users/{id}` terlalu permissive** | Rules saat ini: `allow read, write: if request.auth != null` — siapapun yang login bisa menulis role `admin` ke dokumen dirinya sendiri via Firestore REST. Perlu restrict ke `request.auth.uid == userId` untuk read, dan `admin SDK only` atau whitelist uid untuk write role. | ✅ Done v8.9.29 — `allow create: if uid==userId`; `allow update: if uid==userId && role immutable`; `allow delete: if auth!=null` (batas: tidak bisa cek role requester tanpa Custom Claims). Deploy manual dari Firebase Console. |
| A2 | **Data customers dalam satu dokumen 1MB** | Semua customer + rxHistory disimpan di `optik-zada/config`. Setiap rxHistory row import Excel menambah ukuran. Jika ada 500+ customer dengan riwayat resep, dokumen bisa melebihi 1MB Firestore limit → write gagal total. Solusi: pindahkan `customers[]` ke `customers/{id}` per dokumen. | 📋 Backlog |
| A3 | **Invoice counter collision multi-device** | Counter `db.config.lastInvNo` dibaca dari in-memory state, bukan atomic Firestore transaction. Jika dua perangkat simpan invoice bersamaan, bisa dapat nomor BON yang sama. Solusi: `runTransaction` di Firestore untuk increment counter. | ✅ Done v8.9.26 (format per-tanggal + dedup `existingBons`) |

### 🟠 P1 — Sebelum Launch v9.0

| # | Temuan | Detail | Status |
|---|--------|--------|--------|
| B1 | **Backup restore kurang validasi** | Import backup JSON tidak cek versi skema, field wajib, atau ukuran. Data korup atau JSON parsial bisa menggantikan seluruh db tanpa konfirmasi apa stok/invoice ikut hilang. Perlu: (1) cek field wajib, (2) preview ringkasan sebelum konfirmasi, (3) backup otomatis sebelum restore. | ✅ Done v8.9.27 — + fix bug invoice tidak ter-restore di mode migrated (Store.save buang invoices) |
| B2 | **Tutup Buku tidak mencegah pelunasan retroaktif** | Invoice dari bulan yang sudah di-tutup buku masih bisa dilunasi — angka cashflow bulan itu berubah padahal sudah ter-snapshot. Perlu: cek `closedMonths` sebelum izinkan perubahan finansial. | ✅ Done v8.9.26 |
| B3 | **Double-submit invoice** | Tombol "Simpan Invoice" tidak di-disable setelah klik pertama. Klik ganda atau koneksi lambat bisa membuat invoice duplikat. Perlu: disable tombol + loading state selama `persist()` berjalan. | ✅ Done v8.9.26 |
| B4 | **`confirm()` native masih dipakai** | `delInvoice()` masih pakai `window.confirm()` yang bisa diblokir Chrome desktop (policy: blocked in cross-origin iframes) dan tidak ada di beberapa browser mobile. Perlu ganti ke modal in-app. | ✅ Done v8.9.28 — semua 9 lokasi diganti ke `_confirmModal()` helper + pending-state pattern |
| B5 | **Export PDF Cashflow setelah Tutup Buku** | Sudah disepakati dengan client, belum diimplementasi. PDF snapshot per bulan yang sudah tutup buku. | ✅ Done v8.9.27 — tombol PDF di arsip laporan tertutup + modal detail (reuse exportCashflowPDF) |

### 🟡 P2 — Nice-to-Have / Polish

| # | Temuan | Detail | Status |
|---|--------|--------|--------|
| C1 | **Custom format nomor BON** | Sudah disepakati client (format: `OZ/YYYY/MM/NNNN`), belum diimplementasi. Saat ini auto-increment integer. | ✅ Done v8.9.26 (format final: `INV/OZ/DDMMYY/NNNN`) |
| C2 | **Template WA untuk supplier** | Solusi: admin bisa edit template sendiri dari Pengaturan dengan placeholder system, tidak perlu nunggu client kasih format. | ✅ Done v8.9.51 |
| C3 | **Garansi frame** | Client belum memutuskan flow garansi. Menunggu keputusan. | ⏳ Menunggu client |
| C4 | **Firestore Security Rules lebih granular** | Rules saat ini: `allow read, write: if request.auth != null` untuk invoices. Idealnya tambah validasi: karyawan tidak bisa delete invoice, tidak bisa ubah field `createdBy`. | 🔨 v8.9.46 |
| C5 | **Kompresi logo** | `assets/logo.png` ~1MB → <100KB. Proses manual via squoosh.app. | 📋 User task |
| C6 | **Stok tidak bisa negatif tapi juga tidak ada warning** | Saat ini stok dikurangi diam-diam hingga 0 (Math.max(0,...)). Perlu toast warning jika qty melebihi stok tersedia saat simpan invoice. | 🔨 v8.9.45 |

---

## 🔨 v8.9.44 → v8.9 RC — Week 5: Pre-Release Polish (9–17 Juni)

> Target: semua item selesai sebelum 17 Juni. RC = tidak ada fitur baru, hanya regression test & hotfix.

### Timeline Detail

| Tanggal | Versi Target | Item | Prioritas |
|---------|-------------|------|-----------|
| 9 Juni | v8.9.45 ✅ | Cetak invoice Rx 2 baris + label Dm.A/B lengkap + stok karyawan diblokir | ✅ Selesai |
| 9 Juni | v8.9.46 ✅ | Polish hak akses produk + Backup/Restore admin-strict + rapikan markers + rename `index.html` | ✅ Selesai |
| 9–10 Juni | v8.9.47 ✅ | Security: guard semua `_do*` mutators + Export admin-only + stat Kas/Profit admin-strict | ✅ Selesai |
| 10 Juni | v8.9.48 ✅ | Polish UI/UX: topbar ver sync; badge role invoice; typo; WA label; mobile fix; tooltip icon-only | ✅ Selesai |
| 10 Juni | v8.9.49 ✅ | Warning stok saat simpan invoice: block stok habis, warn qty > stok, notif ≤ 2 semua kategori | ✅ Selesai |
| 10 Juni | v8.9.50 ✅ | Firestore Security Rules granular (karyawan: no delete, no edit `createdBy`) — deploy manual ke Console | ✅ Selesai |
| 10 Juni | v8.9.51 ✅ | Template WA supplier customizable + fix profit modal negatif | ✅ Selesai |
| 11–13 Juni | — | Merge semua dev → main, regression test end-to-end | — |
| 14–17 Juni | v8.9 RC | Tidak ada fitur baru — hanya hotfix bug kritis yang ditemukan saat testing | ✅ RC |

### 🔴 P1 — Harus Selesai Sebelum v9.0

| # | Item | Detail | Target |
|---|------|--------|--------|
| D1 | **Warning Stok Saat Invoice** | Saat ini stok dikurangi senyap hingga 0. Perlu: toast warning "Stok [produk] hanya N tersisa" jika qty input melebihi stok, dan blokir simpan jika stok = 0 (kecuali stok tidak di-track / stok = 0 dari awal). | v8.9.45 |
| D2 | **Firestore Rules Granular** | Rules `invoices/{id}` saat ini: `allow read, write: if auth != null` — karyawan bisa delete invoice dan ubah `createdBy`. Perlu: role-based rules (admin/keluarga: full; karyawan: create + update terbatas, no delete, `createdBy` immutable). | v8.9.46 |
| D3 | **Merge dev → main sebelum RC** | v8.9.43 + v8.9.44 (thermal redesign) masih di dev, belum di main. Merge setelah user konfirmasi hasil print thermal oke. | 12 Juni |

### 🟠 P2 — Nice-to-Have Sebelum Launch

| # | Item | Detail | Status |
|---|------|--------|--------|
| C5 | **Kompresi Logo** | `assets/logo.png` ~1MB → <100KB. Proses manual user via [squoosh.app](https://squoosh.app). Tidak perlu dev. | 📋 User task |
| C2 | **Template WA Supplier** | Solusi self-serve: editable dari Pengaturan dengan placeholder, tidak nunggu client. | ✅ Done v8.9.51 |
| C3 | **Garansi Frame** | Flow garansi frame belum diputuskan client. | ⏳ Menunggu client |
| A2 | **Customer Per-Document Firestore** | Risiko 1MB pada `optik-zada/config` jika customer + rxHistory banyak. Solusi: `customers/{id}` per dokumen. **Defer ke v9.1** — terlalu risky diimplementasi saat production testing aktif, data real sudah ada. | 🔁 Defer v9.1 |

### ✅ Regression Test Checklist (sebelum v9.0)

- [ ] Buat invoice baru → DP → lunaskan → cek cashflow
- [ ] Print struk thermal (58mm & 80mm) — cek konten fit, no URL header
- [ ] Import produk dari Excel → cek stok tidak overwrite
- [ ] Unduh Data Sekarang → buka di Excel → isi produk baru → re-import
- [ ] Backup data → restore → cek semua invoice + customer + produk intact
- [ ] Tutup Buku bulan ini → cek tidak bisa entry retroaktif
- [ ] Login karyawan → cek tidak bisa lihat cashflow, hapus invoice, ubah harga modal
- [ ] Login keluarga → cek akses lengkap minus cashflow & pengaturan sensitif
- [ ] Multi-device: dua browser buka bersamaan → simpan invoice → cek tidak collision

---

## 🚀 v8.9 → v9.0 — Launch Week (18–20 Juni)

| # | Item | Detail |
|---|------|--------|
| L1 | Final Testing End-to-End | Simulasi skenario lengkap: invoice → DP → lunaskan → print → export CSV → backup → cashflow → tutup buku |
| L2 | Data Migration (jika #26 dikerjakan) | Migrasi single-doc ke per-doc Firestore dengan validasi tidak ada data hilang |
| L3 | Onboarding Client | Buat akun admin + karyawan; demo alur kerja utama; panduan backup rutin |
| L4 | Monitor Firebase Usage 24 jam | Pantau reads/writes/hosting bandwidth di Firebase Console |
| L5 | Hotfix Standby | Siap deploy fix darurat jika bug ditemukan saat pertama dipakai |

---

## 💰 Detail: Modul Cashflow & Pengeluaran Toko (Item #10–19)
> Status: **✅ SELESAI — Deployed di v7.9 Beta**

### Kategori Pengeluaran (6 kategori final)

| Kategori | Kode |
|----------|------|
| ⚡ Biaya Listrik Toko | `listrik` |
| 📶 Biaya WiFi | `wifi` |
| 👤 Biaya Gaji Karyawan | `gaji_karyawan` |
| 🏠 Biaya Sewa Ruko | `sewa` |
| 📉 Biaya Penyusutan Etalase | `penyusutan` |
| 📝 Lain-lain | `lainnya` |

> Tagihan Lensa & Restock Frame tidak masuk cashflow — sudah terhitung otomatis sebagai HPP (modal produk) di setiap invoice. Pakai **Skenario B** untuk menghindari double counting.

### Akses per Role

| Fitur | Admin | Karyawan |
|-------|-------|----------|
| Input pengeluaran | ✅ | ✅ |
| View riwayat | ✅ Semua periode | ⚠️ Hari ini saja |
| Profit Bersih & summary | ✅ | ❌ |
| Tutup Buku bulanan | ✅ | ❌ |
| Export CSV | ✅ | ❌ |
| Delete entri | ✅ (kecuali bulan ditutup) | ❌ |

### Formula
```
Profit Bersih = Omzet − HPP (modal produk, otomatis) − Pengeluaran Operasional (manual)
```

---

## 📌 Catatan Penting

### Risk Register

| Risk | Severity | Status | Mitigasi |
|------|----------|--------|---------|
| Firestore 1MB limit (item #26) | 🔴 High | 📋 Planned v8.5 | Restructure sebelum data production banyak masuk |
| Auth logout setiap refresh (item #21) | 🔴 High | ✅ Fixed v8.0 | `browserLocalStoragePersistence` — sesi persistent |
| Concurrent edit overwrite (item #31) | 🟡 Medium | ⏭️ Defer v9.1 | SOP sementara: jangan edit bersamaan di 2 perangkat. Format invoice per-tanggal (v8.9.26) sudah mitigasi collision nomor. |
| Firebase Spark quota (item #25) | 🟡 Medium | 📋 Planned v8.1 | Upgrade Blaze sebelum launch |

### Cara Update Roadmap Ini
Setiap ada tambahan request dari client atau fixing selesai:
1. Pindahkan item dari "Planned" → "Selesai" dengan versi yang sesuai
2. Update tabel Skema Versi dan Status Overview
3. Tambah entry ke Changelog
4. Commit: `docs: roadmap - [versi] [nama item]`

---

## 📋 Changelog

| Tanggal | Versi | Perubahan |
|---------|-------|-----------|
| 28 Mei 2026 | — | Roadmap dibuat — 29 item + 5 launch checklist |
| 28 Mei 2026 | — | Tambah item #21 Cashflow (request client) |
| 29 Mei 2026 | — | Cashflow spec dikonfirmasi client — semua 7 checklist selesai |
| 29 Mei 2026 | v7.9 | Cashflow module selesai diimplementasi & deployed |
| 29 Mei 2026 | v7.9 | Bug fix: cashflow page di luar `.main` wrapper (mobile layout) |
| 29 Mei 2026 | — | Roadmap di-restructure dengan skema versi v7.7→v9.0 |
| 29 Mei 2026 | v8.0 | Auth persistence fix (item #21) + network error banner (item #22) |
| 29 Mei 2026 | v8.0 | Bug fixes: double popup, item nama hilang, format rupiah, hapus Dr. |
| 29 Mei 2026 | v8.0 | Hotfix: spinner macet saat offline (timeout 5s + _initFB timeout 8s) |
| 29 Mei 2026 | v8.0 | Hotfix: "Koneksi ke server belum siap" — _initFB() rewrite Promise.race 10s + injectAuthUI timeout 15s |
| 29 Mei 2026 | v8.0 | Hotfix: _connectFirebase() refactor — retry 3x CDN import, handle duplicate-app, setPersistence try-catch |
| 29 Mei 2026 | v8.1 | Fix: auto-create Firebase Auth saat admin tambah karyawan — tidak perlu Firebase Console lagi |
| 29 Mei 2026 | v8.1 | Feat: login pakai username (karyawan tidak perlu ingat email) + Firestore usernames collection |
| 29 Mei 2026 | v8.1 | Infra: Firebase Blaze plan aktif (GCP free trial) + budget alert setup |
| 29 Mei 2026 | v8.1 | Infra: Custom domain optik-zada.store live + authDomain diupdate |
| 29 Mei 2026 | v8.1 | Infra: Custom email sender noreply@optik-zada.store — DNS records added, verifikasi pending |
| 29 Mei 2026 | v8.2 | Feat: filter bulan di Riwayat Transaksi — dropdown otomatis berisi bulan yang ada datanya |
| 29 Mei 2026 | v8.2 | Feat: data size monitor — progress bar + peringatan otomatis saat login jika data ≥700KB atau ≥900KB |
| 29 Mei 2026 | v8.3 | Feat: badge emas "siap diambil" di sidebar — count invoice DP lewat tglSiap, terpisah dari badge merah total DP |
| 29 Mei 2026 | v8.3 | Fix: password reset continue URL → optik-zada.store (bukan firebaseapp.com) |
| 29 Mei 2026 | v8.4 | Feat: info toko dinamis — nama, alamat, HP, jam, footer bisa diedit dari Pengaturan, update ke struk/print/WA |
| 31 Mei 2026 | v8.9.0 | Feat: halaman Profil Saya (semua role), filter "Transaksi Saya" di Riwayat, notif stok kritis untuk karyawan |
| 31 Mei 2026 | v8.9.1 | Feat: import historis customer dari Excel — deteksi header otomatis, PD/Add multi-row, preview sebelum import |
| 31 Mei 2026 | v8.9.1 | Infra: file Excel historis dibersihkan (159 baris, tipe dinormalisasi, tanggal diperbaiki, header Rx merge ranges) |
| 31 Mei 2026 | v8.9.2 | Feat: manajemen supplier lensa di Pengaturan + order ke supplier via WhatsApp dari modal invoice |
| 31 Mei 2026 | v8.9.3 | Fix: detail lensa double di struk + button WA/Supplier/Thermal jadi ikon-only agar tidak overflow |
| 31 Mei 2026 | v8.9.4 | Feat: PD/Dm.A/B/DBL/TP dipisah dari form invoice → isi post-facto di Riwayat, tidak tampil di struk customer |
| 31 Mei 2026 | v8.9.5 | Fix: FAB pointer-events + HTML escape nama produk/customer + pagination layout tengah |
| 1 Jun 2026 | v8.9.6 | Fix: export cashflow cross-browser + global search redirect via onmousedown |
| 1 Jun 2026 | v8.9.7 | Fix: monthKeyOf() normalisasi tahun 2-digit + salesInvs() filter historis dari finansial |
| 1 Jun 2026 | v8.9.8 | Feat: import historis → rxHistory[] customer (bukan invoice); profil customer 2 seksi; Riwayat bersih |
| 1 Jun 2026 | v8.9.9 | Enhancement: Staff/Admin rename + topbar badge baru + Release Notes via tombol versi + toast login ramah |
| 1 Jun 2026 | v8.9.10 | Feat: role Keluarga (admin-like minus cashflow & setting sensitif); admin-strict class; _isAdminLike() helper |
| 1 Jun 2026 | v8.9.11 | Fix: hapus transaksi (renderHistory + error surfacing); Zona Berbahaya redesign; hapus Release Notes dari Pengaturan |
| 1 Jun 2026 | v8.9.12 | Feat: template Excel untuk import customer (BON/NAMA/Rx/PD/ADD); klarifikasi import = data customer + riwayat resep |
| 1 Jun 2026 | v8.9.13 | Stabilisasi prod: surface Firestore write errors (invoice/lunas/arsip/pengukuran) via toast; fix rxHdrRow undeclared bug |
| 1 Jun 2026 | v8.9.14 | Feat: item GRATIS (jual=Rp0) — struk tampil "GRATIS"; stok & profit tetap terhitung |
| 2 Jun 2026 | v8.9.15 | Fix: cash-basis accounting — kas masuk & profit dicatat sesuai kapan uang diterima, bukan tanggal invoice |
| 2 Jun 2026 | v8.9.16 | Fix: Cashflow `_cfCalc` cash-basis (dpAmount/lunasAmount); dropdown bulan tambah lunasDate months |
| 2 Jun 2026 | v8.9.17 | Feat: Cashflow waterfall (Penjualan Baru + Pelunasan → Kas Masuk → HPP → Profit Kotor → Pengeluaran → Profit Bersih); export PDF + CSV Cashflow lebih lengkap |
| 2 Jun 2026 | v8.9.18 | Optimasi Firestore: IndexedDB offline cache + fix config onSnapshot re-fetch semua invoice + invoice onSnapshot inkremental |
| 2 Jun 2026 | v8.9.19 | Cache lokal localStorage + notif error spesifik saat quota Firestore habis |
| 2 Jun 2026 | v8.9.20 | Hotfix: revert IndexedDB cache (menyebabkan hang di beberapa browser) |
| 3 Jun 2026 | v8.9.21 | Diagnostic: toast error di semua jalur load Firestore — meta_not_found, migrated=false, read error |
| 3 Jun 2026 | v8.9.22 | Feat: versi tampil di topbar; fix silent Rp0 saat config cloud tidak ada — sekarang toast merah + tidak auto-save |
| 3 Jun 2026 | v8.9.23 | Hotfix: spinner login 15s → 5s; error login Firestore lebih jelas; error sesi auto-login tampil di form |
| 3 Jun 2026 | v8.9.24 | FIX KRITIS: syntax error `createdBy?.nama\|\|','']` di exportCashflowCSV (ada sejak v8.9.17) → seluruh inline JS gagal parse, app mati total; + CI `node --check` ditambahkan |
| 4 Jun 2026 | v8.9.25 | Security: XSS escape semua innerHTML customer/produk/supplier; fix stok restore saat delInvoice/restoreInvoice; auto-logout 3 menit → 15 menit; tambah audit backlog ke ROADMAP |
| 7 Jun 2026 | v8.9.26 | Feat: format nomor invoice baru `INV/OZ/DDMMYY/NNNN` (counter per-tanggal, anti-collision via dedup) + onchange listener tanggal; Fix: double-submit guard di tombol Simpan Invoice; Enforcement: Tutup Buku blok simpan invoice & pelunasan retroaktif ke bulan yang ditutup |
| 7 Jun 2026 | v8.9.27 | Feat: restore data lebih aman (validasi struktur + ringkasan perubahan + auto-backup sebelum timpa) & fix bug invoice tidak ter-restore di mode migrated; Feat: tombol Export PDF di arsip laporan Tutup Buku + modal detail |
| 7 Jun 2026 | v8.9.28 | Fix B4: ganti semua 9 `confirm()` native ke `_confirmModal()` in-app helper + pending-state pattern — arsip invoice, hapus pengeluaran, tutup buku, reset master, hapus transaksi, reset all, migrasi v8.5, batalkan pending user, hapus akun |
| 7 Jun 2026 | v8.9.29 | Security A1: perketat Firestore rules `users/{userId}` — `create` hanya untuk uid sendiri; `update` hanya untuk uid sendiri AND field `role` tidak bisa diubah (blok eskalasi privilege via Firestore REST). Deploy manual di Firebase Console. |
| 7 Jun 2026 | v8.9.30 | Hotfix: data kosong setelah login akibat rules v8.9.29 — fix `_ensureDataLoaded()` dipanggil sebelum semua login flows |
| 8 Jun 2026 | v8.9.31 | Feat: bulk delete master data per kategori (Frame/Lensa/Softlens/Aksesoris) |
| 8 Jun 2026 | v8.9.32 | Feat: full audit log semua tindakan hapus — helper `_logAudit()`, 50 entri, semua destructive actions |
| 8 Jun 2026 | v8.9.33 | Feat: TP Pengukuran Lensa dipisah Kanan (OD) & Kiri (OS), backward compat `rx.tp` |
| 8 Jun 2026 | v8.9.34 | Feat: field Ket. Faset di Pengukuran Lensa |
| 8 Jun 2026 | v8.9.35 | Fix: koreksi label Dm.A(L)/Dm.B(T) di form & CSV (sebelumnya terbalik) |
| 8 Jun 2026 | v8.9.36 | Feat: Kas Masuk per Kategori tampil nama pembeli + no. invoice (top-3) |
| 8 Jun 2026 | v8.9.37 | Feat: Kas Masuk per Kategori tambah daftar produk per transaksi |
| 8 Jun 2026 | v8.9.38 | Feat: tombol "Unduh Data Sekarang" di semua Master Data — export aktif ke Excel |
| 8 Jun 2026 | v8.9.39 | Fix: print thermal `@page 80mm auto` + print media CSS 72mm untuk printer thermal roll |
| 8 Jun 2026 | v8.9.40 | Fix: print thermal BTP3100 — @page 80mm, margin 4mm, tombol Simpan PDF, hint ukuran |
| 8 Jun 2026 | v8.9.41 | Fix: print thermal hapus `@page size` — fix rotasi/landscape di KASSEN printer |
| 8 Jun 2026 | v8.9.42 | Fix: print thermal `@page{margin:0mm;size:auto}` + print-color-adjust — suppress URL header/footer Chrome |
| 8 Jun 2026 | v8.9.43 | Fix: print thermal width:100% di media print; hapus tombol Simpan PDF; hint uncheck Headers and footers |
| 8 Jun 2026 | v8.9.44 | Feat: redesain struk thermal — nama toko 16px, separator hirarki solid/dashed, item layout + qty tag, badge LUNAS 2px, footer double-line, max-width 72mm |
| 8 Jun 2026 | — | Roadmap diperbarui: timeline Week 5 (9–17 Juni), target v8.9.45–v8.9 RC, regression checklist |
| 9 Jun 2026 | v8.9.45 | Feat: cetak invoice Rx 2 baris (R & L terpisah), label Dm.A (Lebar)/Dm.B (Tinggi) lengkap; stok karyawan diblokir (tombol +/- disembunyikan untuk Staff) |
| 9 Jun 2026 | v8.9.46 | Polish: tombol Edit/Hapus produk admin-only (selaras guard); kartu Backup & Restore admin-strict + guard `restoreData`; rapikan section markers (escape text ═/· + dedup SECTION 22B) |
| 9 Jun 2026 | — | Chore: rename file app `Optik-Zada v7.7 (Beta Version).html` → `index.html` + update 5 referensi CI (firebase-deploy.yml) & CLAUDE.md. CI deploy-dev hijau. |

---

*Last updated: 9 Jun 2026 · Optik Zada Management System v8.9.46 Beta*
