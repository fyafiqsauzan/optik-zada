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
| **v8.8.0 Beta** | ✅ Dirilis | Promo global (#37), riwayat customer lengkap (#27), dark mode otomatis (#38), tooltip Rx/DP (#39) |
| **v8.8 RC** | 📋 Planned | Polish & launch prep |
| **v9.0** | 🚀 Target | Production launch — 20 Juni 2026 |

> **Skema:** patch (x.x.Y) = bugfix kecil · minor (x.Y.0) = fitur baru · major (Y.0.0) = perubahan arsitektur besar · RC = Release Candidate

---

## 📊 Status Overview

| Fase | Periode | Versi | Status |
|------|---------|-------|--------|
| Week 1 — Foundation & Beta Features | 20–27 Mei | v7.7 → v7.8 | ✅ Selesai |
| Week 2 — Cashflow + Early Fixes | 28–29 Mei | v7.8 → v7.9 | ✅ Selesai |
| Week 3 — Critical Fixes & UX | 30 Mei – 5 Juni | v7.9 → v8.0 | ✅ Selesai |
| Week 3 lanjutan — Search, Monitor, Infra | 30 Mei – 5 Juni | v8.0 → v8.1 | 🔄 In Progress |
| Week 4 — Core Features | 6–12 Juni | v8.1 → v8.5 | 📋 Planned |
| Week 5 — Architectural & Polish | 13–17 Juni | v8.5 → v8.8 | 📋 Planned |
| Launch Week | 18–20 Juni | v8.8 → v9.0 | 🚀 Target |

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
| 37 | Diskon Global / Promo | Feature | ✅ v8.8.0 | Setting promo di Pengaturan (label + jumlah Rp). Aktif → semua invoice baru dapat diskon otomatis, tampil di struk & live preview. |
| 38 | Dark/Light Mode Toggle Otomatis | Enhancement | ✅ v8.8.0 | `prefers-color-scheme` digunakan jika belum ada pilihan manual. `matchMedia` listener — otomatis ikut sistem saat berubah. |
| 39 | Tooltip / Help Onboarding | UX | ✅ v8.8.0 | Tooltip ikon `?` di semua field Rx (Sph, Cyl, Axis, Visus, PD, Add, Dm.A, Dm.B, DBL, TP) + field DP. |

---

## 🚀 v8.8 → v9.0 — Launch Week (18–20 Juni)

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
| Concurrent edit overwrite (item #31) | 🟡 Medium | 📋 Planned v8.6 | SOP sementara: jangan edit bersamaan |
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

---

*Last updated: 29 Mei 2026 · Optik Zada Management System v8.5 Beta*
