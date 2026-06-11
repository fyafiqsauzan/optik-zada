# Optik Zada — Claude Code Instructions

## Status Proyek

**PRODUCTION TESTING AKTIF** — Aplikasi saat ini sedang dipakai oleh client untuk testing production selama ±2 bulan (mulai ~Juni 2026). Setiap perubahan harus dipertimbangkan dampaknya terhadap pengguna yang sedang aktif.

### Konsekuensi:
- Jangan ubah skema data Firestore secara breaking (field rename, struktur rxHistory, invoice, config)
- Jangan hapus/rename function yang mungkin sedang dipanggil di data lama (backward compat)
- Tiap perubahan UI harus tetap intuitif — pengguna sudah familiar dengan layout existing
- Jangan bump major version tanpa diskusi
- Test logic secara mental sebelum push — tidak ada staging environment

---

## Git & Deploy

- **Branch kerja:** `claude/optimistic-darwin-qo3x8`
- **JANGAN PERNAH push ke `main`** — main = production client, hanya di-merge oleh user setelah review
- Push via PAT: `https://fyafiqsauzan:<PAT_TOKEN>@github.com/fyafiqsauzan/optik-zada.git`
  _(PAT tersimpan di environment/session — jangan hardcode di file ini)_
- Setelah push, sync tracking ref:
  ```
  git fetch https://fyafiqsauzan:<PAT>@github.com/fyafiqsauzan/optik-zada.git claude/optimistic-darwin-qo3x8:refs/remotes/origin/claude/optimistic-darwin-qo3x8
  ```
- Setelah setiap fix/fitur: update `ROADMAP.md` + release notes di dalam web app

## Workflow Rilis (WAJIB DIIKUTI)

```
1. Semua perubahan (fitur / bugfix / revisi) → push ke branch claude/optimistic-darwin-qo3x8
2. User review di dev environment (optik-zada1127)
3. Kalau sudah disetujui user → user sendiri yang merge + push ke main
4. JANGAN push ke main tanpa persetujuan eksplisit dari user
5. Boleh akumulasi beberapa fix/fitur di dev sebelum merge ke main — tidak perlu release satu-satu
```

**Firebase environments:**
- `optik-zada1127` → dev/testing (branch claude/...) — data dummy, aman untuk eksperimen
- `optik-zadaa` → production client (branch main) — data real, hati-hati

## Skema Versi

| Tipe | Kapan |
|------|-------|
| patch (x.x.Y) | bugfix kecil, perubahan teks/UI minor |
| minor (x.Y.0) | fitur baru |
| major (Y.0.0) | perubahan arsitektur besar — diskusi dulu |

---

## File Utama

- **App:** `/home/user/optik-zada/index.html` — single-file SPA (di-rename dari "Optik-Zada v7.7 (Beta Version).html" pada v8.9.46 agar rapi & selaras dengan artifact deploy `public/index.html`)
- **Roadmap:** `/home/user/optik-zada/ROADMAP.md`

---

## Arsitektur Singkat

- Single-file HTML SPA, Firebase Firestore v10 (modular)
- `onSnapshot` untuk real-time updates
- `persist()` → `Store.save()` → simpan config ke `optik-zada/config`; invoices ke `invoices/{id}`
- `currentRole` = `'admin'` | `'keluarga'` | `'karyawan'`
- `_isAdminLike()` = `currentRole==='admin' || currentRole==='keluarga'`

### Role Hierarchy
| Role | Label UI | Akses |
|------|----------|-------|
| `admin` | Admin | Full access |
| `keluarga` | Keluarga | Full minus Cashflow & setting sensitif |
| `karyawan` | Staff | Operasional only |

### CSS Class Permissions
- `.admin-only` — tersembunyi untuk karyawan; tampil untuk admin & keluarga
- `.admin-strict` — hanya tampil untuk admin (tersembunyi untuk keluarga & karyawan)

---

## Data Penting — Jangan Breaking

- `customer.rxHistory[]` — data resep mata dari import Excel (BUKAN transaksi)
- `db.invoices[]` / Firestore `invoices/{id}` — transaksi aktif
- `db.customers[]` — master data customer
- `db.config` / Firestore `optik-zada/config` — konfigurasi toko & users

---

## Pending / Backlog

- Template WA untuk supplier — menunggu info dari client
- Garansi frame — menunggu keputusan client
- Custom format nomor BON — sudah disepakati, belum diimplementasi
- PDF export setelah Tutup Buku di Cashflow — sudah disepakati, belum diimplementasi
