# 🗺️ Optik Zada — Development Roadmap
### Target Launch: 20 Juni 2026
> Timeline pengembangan dari fase Beta menuju Production-ready untuk kebutuhan UMKM Optik.

---

## 📊 Status Overview

| Fase | Periode | Status |
|------|---------|--------|
| Week 1 — Foundation & Beta Features | 20–27 Mei | ✅ Selesai |
| Week 2 — Critical Fixes & UX | 28 Mei – 3 Juni | 🔄 In Progress |
| Week 3 — Core Production Features | 4–10 Juni | 📋 Planned |
| Week 4 — Architectural & Polish | 11–17 Juni | 📋 Planned |
| Launch Week | 18–20 Juni | 🚀 Target |

---

## ✅ Week 1 — Foundation & Beta Features (20–27 Mei)
> Semua item di bawah sudah selesai dikerjakan.

| # | Item | Tipe | Keterangan |
|---|------|------|------------|
| 1 | Resep Mata Lengkap (Dm.A, Dm.B, DBL, TP) | Enhancement | Field baru di bawah PD/Add; sync ke struk, CSV, arsip |
| 2 | Audit Log Invoice | Enhancement | Setiap invoice mencatat `createdBy` (nama user) |
| 3 | Karyawan bisa Lunaskan DP | Fix | Tidak perlu admin untuk proses pelunasan |
| 4 | Reset Password via Email | Feature | "Lupa password?" di halaman login |
| 5 | Soft Delete / Arsip Invoice | Feature | Hapus tidak permanen; pulihkan dari Settings |
| 6 | Pagination Riwayat (25/halaman) | Enhancement | Performa lebih baik untuk history banyak |
| 7 | CSV Export Fix | Fix | Langsung rapi di Excel tanpa Text-to-Columns manual; kolom Rx baru ikut ter-export |
| 8 | Firestore Security Rules — CI/CD | Security | Rules di-deploy otomatis via GitHub Actions |
| 9 | Release Notes Modal | Feature | Muncul setelah login; caution beta + daftar fitur |

---

## 🔄 Week 2 — Critical Fixes & UX (28 Mei – 3 Juni)

### 🔴 HIGH RISK — Wajib diselesaikan minggu ini

| # | Item | Tipe | Detail |
|---|------|------|--------|
| 10 | **Fix Auth Persistence** | **Critical Fix** | Sekarang pakai `inMemoryPersistence` — user logout setiap refresh halaman. Ganti ke `browserLocalStorage` agar sesi tetap aktif. Ini dealbreaker untuk daily use. |
| 11 | **Network Error Handling** | Critical Fix | Jika internet putus atau Firebase unreachable, user tidak dapat feedback apapun. Tambah banner "Koneksi terputus — data belum tersimpan" dan retry indicator. |

### 🟡 MEDIUM — Sangat dianjurkan

| # | Item | Tipe | Detail |
|---|------|------|--------|
| 12 | Search & Filter Riwayat | Feature | Cari invoice by nama customer, nomor invoice, atau bulan. Saat ini hanya bisa scroll. |
| 13 | Data Size Monitor + Warning | Monitoring | Firestore limit 1MB per dokumen. Tambah indikator ukuran data di Settings dan warning otomatis saat mendekati 700KB. |
| 14 | Firebase Blaze Plan Setup | Infrastructure | Free tier: 50K reads/day, 20K writes/day. Bisa terkena limit tiba-tiba. Upgrade ke Blaze (pay-as-you-go) — biaya praktis nol untuk skala toko kecil. |

---

## 📋 Week 3 — Core Production Features (4–10 Juni)

### 🔵 MAJOR — Architectural

| # | Item | Tipe | Detail |
|---|------|------|--------|
| 15 | **Firestore Per-Document Restructure** | **Major / Architectural** | Saat ini seluruh data (invoices, produk, customers) disimpan sebagai 1 JSON string dalam 1 dokumen Firestore. Hard limit = 1MB. Estimasi: 100 invoice/bulan × 12 bulan ≈ data meledak dalam ~8–10 bulan. Restructure ke: `invoices/{id}`, `products/{id}`, `customers/{id}` sebagai dokumen terpisah. Ini perubahan terbesar dan paling riskan — butuh migrasi data + testing menyeluruh. |

### 🟡 MEDIUM — Penting untuk daily ops

| # | Item | Tipe | Detail |
|---|------|------|--------|
| 16 | Riwayat Resep per Customer | Feature | Di halaman Customer → klik nama → lihat semua invoice + resep mata sebelumnya. Sangat berguna untuk repeat customer. |
| 17 | List DP Outstanding + WA Blast | Feature | Dashboard khusus: semua invoice DP yang belum lunas, lengkap dengan tombol WA reminder ke masing-masing customer. |
| 18 | Notif "Siap Diambil" lebih proaktif | Enhancement | Sekarang ada banner pasif. Tambah highlight + badge count di sidebar untuk pesanan yang sudah lewat tanggal siap ambil. |
| 19 | Print Nota Customization | Feature | Admin bisa edit nama toko, alamat, nomor telepon, dan footer struk dari Settings (saat ini hardcoded). |

---

## 📋 Week 4 — Polish & Launch Prep (11–17 Juni)

### 🔵 MAJOR

| # | Item | Tipe | Detail |
|---|------|------|--------|
| 20 | **Multi-User Concurrent Edit Safety** | Major | Saat admin dan karyawan edit data bersamaan, ada risiko salah satu overwrite data yang lain. Implementasi optimistic locking dengan Firestore transactions untuk operasi kritis (simpan invoice, update stok). |

### 🟡 MEDIUM

| # | Item | Tipe | Detail |
|---|------|------|--------|
| 21 | Custom Domain Setup | Infrastructure | Ganti URL Firebase default (`optik-zada1127.web.app`) ke domain sendiri (misal `optikzada.com`). Lebih profesional untuk client. |
| 22 | Mobile Responsive Audit | Polish | Pastikan semua halaman — terutama Invoice form dan Riwayat — dapat digunakan nyaman di layar HP/tablet (karyawan jaga sendiri). |
| 23 | Kompresi Aset | Performance | `assets/logo.png` ~1MB → target <100KB. Gunakan [squoosh.app](https://squoosh.app) untuk kompresi manual. Percepat loading awal. |
| 24 | Konfirmasi Email Akun Baru | Security | Saat ini karyawan bisa daftar dengan email apapun tanpa verifikasi. Tambah email verification sebelum akun aktif. |

### 🟢 NICE TO HAVE

| # | Item | Tipe | Detail |
|---|------|------|--------|
| 25 | Laporan Profit per Produk | Feature | Di halaman Laporan: breakdown margin keuntungan per kategori produk (frame, lensa, softlens). |
| 26 | Diskon Global / Promo | Feature | Setting diskon persentase global yang bisa diaktifkan sementara (misal promo Lebaran). |
| 27 | Dark/Light Mode Toggle Otomatis | Enhancement | Ikuti preferensi sistem (prefers-color-scheme) secara default. |
| 28 | Tooltip / Help Onboarding | UX | Tooltip singkat di setiap field kompleks (Rx, DP amount) untuk bantu user baru. |

---

## 🚀 Launch Week — Go-Live (18–20 Juni)

| # | Item | Detail |
|---|------|--------|
| L1 | Final Testing End-to-End | Simulasi skenario lengkap: buat invoice, DP, lunaskan, print, export CSV, backup |
| L2 | Data Migration (jika #15 dikerjakan) | Migrasi data dari single-doc ke per-doc Firestore dengan validasi tidak ada data hilang |
| L3 | Onboarding Client | Buat akun admin + karyawan untuk client; demo singkat alur kerja utama |
| L4 | Monitor Firebase Usage 24 jam | Pantau Firestore reads/writes, hosting bandwidth di Firebase Console |
| L5 | Hotfix Standby | Siap deploy fix darurat jika ada bug yang ditemukan saat pertama kali dipakai |

---

## 📌 Catatan Penting

### Risk Register

| Risk | Severity | Mitigasi |
|------|----------|---------|
| Firestore 1MB limit (item #15) | 🔴 High | Segera restructure sebelum data production masuk banyak |
| Auth logout setiap refresh (item #10) | 🔴 High | Fix di Week 2 sebelum client mulai pakai |
| Concurrent edit overwrite (item #20) | 🟡 Medium | Mitigasi sementara: SOP internal "jangan edit bersamaan"; fix proper di Week 4 |
| Firebase Spark quota (item #14) | 🟡 Medium | Upgrade Blaze sebelum launch |

### Cara Update Roadmap Ini
Setiap ada tambahan request dari client atau kebutuhan baru:
1. Tambahkan item baru ke section yang relevan
2. Beri nomor lanjutan
3. Update status tabel di bagian atas
4. Commit dengan message: `docs: update roadmap - tambah [nama item]`

---

*Last updated: 28 Mei 2026 · Optik Zada Management System v7.7 Beta*
