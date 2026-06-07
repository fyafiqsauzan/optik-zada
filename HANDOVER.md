# 📦 Panduan Handover Optik Zada ke Client

> Dokumen ini panduan lengkap nyerahin aplikasi ke client, tapi lu tetap bisa
> maintenance dari GitHub tanpa bisa lihat data rahasia client.

---

## 🎯 Tujuan Akhir

Setelah semua step selesai:

| Siapa | Punya apa |
|-------|-----------|
| **Client** | Data Firestore, billing Firebase, domain `.store`, akun admin app |
| **Lu (dev)** | Code di GitHub, akses deploy (TANPA bisa baca data client) |

**Analogi:** Lu kayak tukang yang bangun & renovasi rumah. Lu pegang kunci pintu
depan buat masuk benerin sesuatu (deploy code), tapi lu GA punya kunci brankas
di dalam rumah (data Firestore client). 

---

## 🗺️ Peta Besar (5 Fase)

```
FASE 1 — Client siapin akun (Google + Hostinger)
FASE 2 — Bikin Firebase project baru punya client
FASE 3 — Setup akses deploy buat lu (Hosting-only)
FASE 4 — Masukin rahasia ke GitHub Secrets
FASE 5 — Deploy pertama + serah terima
```

Santai, dikerjain satu-satu. Ga harus sehari kelar.

---

# FASE 1 — Client Siapin Akun

### 1.1 Client bikin akun Google (kalau belum punya)
- Buat Gmail baru khusus bisnis, misal `optikzada.official@gmail.com`
- **JANGAN pakai Gmail pribadi lu** — ini bakal jadi pemilik semua data

### 1.2 Client bikin akun Hostinger (buat domain nanti)
- Daftar di hostinger.com pakai email bisnis tadi

> ✅ **Output Fase 1:** Client punya 1 email Google + 1 akun Hostinger

---

# FASE 2 — Bikin Firebase Project Client

> Ini dikerjain sambil **screen-share sama client**, atau lu yang pegang
> sementara terus nanti transfer ownership ke client.

### 2.1 Buat project baru
1. Buka https://console.firebase.google.com
2. Login pakai **email Google client**
3. Klik **"Add project"**
4. Nama project: `optik-zada-client` (atau bebas)
5. Matikan Google Analytics (ga perlu) → **Create project**

### 2.2 Aktifkan Firestore Database
1. Sidebar kiri → **Build → Firestore Database**
2. Klik **Create database**
3. Pilih lokasi: **asia-southeast2 (Jakarta)** ← penting, biar cepat
4. Mode: pilih **Production mode**
5. Klik **Enable**

### 2.3 Aktifkan Authentication
1. Sidebar → **Build → Authentication**
2. Klik **Get started**
3. Tab **Sign-in method** → klik **Email/Password** → **Enable** → Save

### 2.4 Aktifkan Hosting
1. Sidebar → **Build → Hosting**
2. Klik **Get started** → Next → Next → Continue
   (ga usah jalanin command apa-apa, cukup di-enable aja)

### 2.5 Upgrade ke Blaze plan (WAJIB, pakai kartu client)
> Firestore butuh Blaze plan. Tenang, ada free tier gede — biaya bulanan
> biasanya Rp0 untuk toko kecil.

1. Pojok kiri bawah → klik **Spark/Upgrade**
2. Pilih **Blaze (Pay as you go)**
3. **Client yang masukin kartu kredit/debit mereka** ← BUKAN kartu lu
4. Set budget alert: $5 (biar dapat email kalau ada tagihan ga wajar)

> ✅ **Output Fase 2:** Firebase project client jadi, Firestore + Auth +
> Hosting aktif, billing pakai kartu client

---

# FASE 3 — Setup Akses Deploy Buat Lu

> Di sini kunci pentingnya: lu dikasih akses yang **cuma bisa deploy code**,
> ga bisa baca data Firestore.

### 3.1 Ambil Firebase Config (ini BUKAN rahasia)
1. Firebase Console → ⚙️ **Project Settings** (pojok kiri atas)
2. Scroll ke bawah bagian **"Your apps"**
3. Klik icon **`</>`** (Web app)
4. Nama app: `Optik Zada Web` → **Register app**
5. Bakal muncul kode kayak gini — **COPY yang bagian `firebaseConfig`:**
   ```javascript
   const firebaseConfig = {
     apiKey: "AIzaSy....",
     authDomain: "optik-zada-client.firebaseapp.com",
     projectId: "optik-zada-client",
     storageBucket: "optik-zada-client.firebasestorage.app",
     messagingSenderId: "123456789",
     appId: "1:123:web:abc123"
   };
   ```
6. Simpan dulu di notepad. Nanti dipakai di Fase 4.

### 3.2 Buat Service Account khusus Hosting (INI yang penting)
> Service account = "robot akun" yang dipakai GitHub buat deploy.
> Kita kasih dia izin **cuma deploy hosting**, ga bisa sentuh Firestore.

1. Firebase Console → ⚙️ **Project Settings** → tab **Service accounts**
2. Klik link **"Manage service account permissions"**
   (ini buka Google Cloud Console di tab baru)
3. Di Google Cloud Console:
   - Klik **+ Create Service Account** (atas)
   - Nama: `github-deploy`
   - Klik **Create and Continue**
4. Bagian **"Grant this service account access"** → pilih role:
   - Ketik & pilih: **Firebase Hosting Admin**
   - ⚠️ **JANGAN kasih role Firestore atau Editor/Owner**
   - Klik **Continue** → **Done**
5. Sekarang bikin kunci-nya:
   - Klik service account `github-deploy` yang baru dibuat
   - Tab **Keys** → **Add Key** → **Create new key**
   - Pilih **JSON** → **Create**
   - File JSON otomatis ke-download → simpan baik-baik (jangan share sembarangan)

> ✅ **Output Fase 3:** Lu punya (1) Firebase config client, (2) file JSON
> service account hosting-only

---

# FASE 4 — Masukin Rahasia ke GitHub Secrets

> GitHub Secrets = brankas di GitHub buat nyimpen info sensitif. Aman, ga
> kelihatan di code.

### 4.1 Buka halaman Secrets
1. Buka repo lu: https://github.com/fyafiqsauzan/optik-zada
2. **Settings** (tab atas) → sidebar kiri **Secrets and variables** → **Actions**
3. Klik tombol **New repository secret** buat tiap item di bawah

### 4.2 Tambah 4 secrets ini satu per satu

| Name (persis huruf besar) | Value yang diisi |
|---------------------------|------------------|
| `PROD_FIREBASE_SERVICE_ACCOUNT` | Buka file JSON dari Fase 3.2, copy **SELURUH ISI**-nya, paste |
| `PROD_FIREBASE_CONFIG` | Lihat format di bawah ⬇️ |
| `PROD_FIREBASE_PROJECT_ID` | `optik-zada-client` (sesuai projectId lu) |
| `PROD_ADMIN_EMAIL` | Email Google client (yg jadi admin), misal `optikzada.official@gmail.com` |

**Format `PROD_FIREBASE_CONFIG`** — tulis sebagai satu baris JSON (pakai kurung kurawal, kutip ganda):
```json
{"apiKey":"AIzaSy....","authDomain":"optik-zada-client.firebaseapp.com","projectId":"optik-zada-client","storageBucket":"optik-zada-client.firebasestorage.app","messagingSenderId":"123456789","appId":"1:123:web:abc123"}
```
> ⚠️ Ambil angka dari config Fase 3.1. Perhatiin: pakai `"` (kutip ganda),
> ga ada koma di akhir, semua dalam satu baris.

> ✅ **Output Fase 4:** 4 secrets ke-set di GitHub

---

# FASE 5 — Deploy Pertama + Serah Terima

### 5.1 Deploy ke prod (push ke branch main)
Dari komputer lu, jalankan:
```bash
git checkout main
git merge claude/optimistic-darwin-qo3x8
git push origin main
```
- GitHub Actions otomatis jalan
- Cek progress: repo → tab **Actions** → lihat job **deploy-prod** hijau ✅
- CI bakal otomatis ganti config dev jadi config client sebelum deploy

### 5.2 Deploy Firestore Rules (manual, sekali aja)
> Ini ga lewat CI biar lu ga butuh akses Firestore. Cukup copy-paste.

1. Firebase Console client → **Firestore Database** → tab **Rules**
2. Buka file `firestore.rules` di repo, copy semua isinya
3. Paste ke editor rules di console → klik **Publish**

### 5.3 Hubungkan domain (kalau client mau pakai domain sendiri)
**Opsi A — domain baru beli di Hostinger client:**
1. Firebase Console → **Hosting** → **Add custom domain**
2. Masukin domain client, misal `optikzada.com`
3. Firebase kasih DNS records (A record / TXT)
4. Client masukin DNS itu di panel Hostinger mereka
5. Tunggu propagasi (bisa beberapa jam)

**Opsi B — transfer domain `optik-zada.store` lu ke client:**
1. Di Hostinger lu: **Domains → optik-zada.store → Transfer/Move**
2. Pindahin ke akun Hostinger client
3. Update DNS nunjuk ke Firebase Hosting client

### 5.4 Bikin akun admin buat client
1. Client buka URL app (domain-nya)
2. Login pakai email Google yang di-set sebagai `PROD_ADMIN_EMAIL`
   - Pertama kali, klik **"Lupa password?"** dulu buat set password
   - Karena email ini = `ADMIN_BOOTSTRAP_EMAIL`, otomatis dapat role Admin
3. Setelah masuk, client bisa tambah akun karyawan dari **Pengaturan**

### 5.5 Test akhir (checklist)
- [ ] App kebuka di domain client
- [ ] Client bisa login sebagai admin
- [ ] Bisa simpan invoice
- [ ] Data muncul di Firestore Console client
- [ ] **Lu coba akses Firestore client → DITOLAK** (ini yang diharapkan ✅)

> ✅ **Output Fase 5:** App live di tangan client, data aman, lu tetap bisa deploy

---

# 🔧 Workflow Maintenance Sehari-hari (Setelah Handover)

Kerjaan lu ga berubah banget:

```
1. Client lapor bug / minta fitur
        ↓
2. Lu kerja di branch claude/optimistic-darwin-qo3x8
   → test di Firebase LU sendiri (data dummy, aman)
        ↓
3. Kalau udah oke, merge ke main:
   git checkout main
   git merge claude/optimistic-darwin-qo3x8
   git push origin main
        ↓
4. CI otomatis deploy ke Firebase CLIENT
        ↓
5. App client update — lu ga pernah lihat data mereka
```

**Bedanya dari sekarang:**
- Branch `claude/...` → deploy ke Firebase **lu** (testing)
- Branch `main` → deploy ke Firebase **client** (produksi)

---

# ❓ FAQ

**Q: Kalau lu tau apiKey client, bukannya lu bisa akses data?**
A: Ga bisa. apiKey itu cuma "alamat" project, bukan password. Buat baca data
   butuh LOGIN ke akun yang terdaftar di Auth client — dan lu ga punya akun di
   situ. Firestore Rules `if request.auth != null` yang blok.

**Q: Kalau client ganti developer, gimana?**
A: Client tinggal cabut akses lu: hapus service account `github-deploy` di
   Google Cloud Console + ganti GitHub Secrets. Data tetap aman di tangan mereka.

**Q: Tagihan Firebase siapa yang bayar?**
A: Client, karena billing pakai kartu mereka (Fase 2.5). Toko kecil biasanya
   masih masuk free tier = Rp0.

**Q: Kalau gua mau lihat data buat debugging gimana?**
A: Minta client export backup JSON (tombol Backup di Pengaturan), atau client
   kasih akses Firestore sementara. Tapi defaultnya lu ga punya akses —
   itu memang sengaja buat jaga kerahasiaan data client.

**Q: File `firestore.rules` di GitHub kan kelihatan, aman ga?**
A: Aman. Rules itu memang harus "publik" sifatnya — dia aturan keamanan, bukan
   data. Tau aturannya ga bikin orang bisa bobol.

---

*Dibuat untuk handover Optik Zada · simpan dokumen ini baik-baik*
