Link Website PCM Gemolong Demo 🔗pcm-gemolong.web.id

# Website PCM Gemolong

Website Pimpinan Cabang Muhammadiyah (PCM) Gemolong, dikembangkan dengan Django untuk menyajikan profil organisasi, pimpinan, ranting, amal usaha, berita, dan agenda kegiatan.

> Website ini dibuat untuk tugas kuliah Pemrograman Web berbasis Framework (TIF1336), **bukan website resmi PCM Gemolong**.

## Anggota Tim & Kontribusi

| Nama | NIM | Kontribusi |
|------|-----|------------|
| Galih Wiku Dhamar Aji | L200240164 | Pengambangan Beranda, Navbar, Footer, Integrasi dan pengelolaan halaman admin  |
| Muhammad Annas Ardiansyah | L200240166 | Pengembangan Halaman Berita |
| Dzaky Naufal Hakim | L200240159 | Pengembangan Halaman profil, kontak, formulir pesan masuk, dan admin pesan masuk |
| Akhyar Khairun Wahyudin | L200240208 | Pengembangan Halaman ranting dan amal usaha |
| Risky Nur Apriliyan | L200240165 | Pengembangan agenda mendatang |

## Halaman yang Tersedia

| Alamat | Isi |
|---|---|
| `/` | Beranda: hero, statistik, berita terbaru, agenda mendatang |
| `/profil/` | Tentang, sejarah, visi, dan misi |
| `/pimpinan/` | Daftar pimpinan |
| `/ranting/` | Daftar ranting |
| `/amal-usaha/` | Daftar amal usaha dengan filter bidang |
| `/berita/` | Daftar berita dan halaman detail per berita |
| `/agenda/` | Agenda mendatang dan yang sudah lewat |
| `/admin/` | Pengelolaan seluruh data (perlu akun administrator) |

## Teknologi

- **Python 3.14** dan **Django 6.1**
- **uv** untuk mengelola environment dan dependency
- **SQLite** sebagai database lokal
- **Pillow** untuk gambar, **python-dotenv** untuk membaca `.env`
- **Bootstrap 5.3** untuk antarmuka

## Prasyarat

- [Git](https://git-scm.com/)
- [uv](https://docs.astral.sh/uv/)

Python tidak perlu dipasang manual. uv mengunduh versi yang sesuai dari file `.python-version`.

Memasang uv di Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Instalasi

### 1. Clone repository

```bash
git clone https://github.com/galihwikuu/tugas-pcm.git
cd tugas-pcm
```

### 2. Pasang dependency

```bash
uv sync
```

Perintah ini membuat folder `.venv` dan memasang semua paket sesuai `uv.lock`, sehingga versinya sama dengan milik developer lain.

### 3. Siapkan file `.env`

Konfigurasi rahasia disimpan di file `.env` yang **tidak ikut repository**. Salin dari contoh:

```powershell
Copy-Item .env.example .env
```

Di macOS atau Linux: `cp .env.example .env`

Buat secret key baru:

```bash
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Buka `.env`, lalu ganti `isi-dengan-kunci-acak` dengan hasilnya, diapit tanda kutip tunggal:

```text
SECRET_KEY='kunci-hasil-salinan'
```

Tanda kutip tunggal wajib dipakai karena kunci Django sering memuat karakter seperti `#` atau `$`.

| Variabel | Fungsi |
|---|---|
| `SECRET_KEY` | Wajib diisi. Kunci rahasia Django |
| `DEBUG` | `True` untuk lokal. Bernilai `False` jika tidak diisi |
| `ALLOWED_HOSTS` | Daftar host yang diizinkan, dipisah koma |
| `DATABASE_URL` | Dikosongkan, berarti memakai SQLite |

## 4. Konfigurasi Environment

Buat file `.env` berdasarkan template yang tersedia:

```powershell
Copy-Item .env.example .env
```

Buka file `.env`, kemudian sesuaikan konfigurasi database:

```dotenv
DB_NAME=pcm_django
DB_USER=pcm_user
DB_PASSWORD=password_lokal_kamu
DB_HOST=127.0.0.1
DB_PORT=5433
```

**Catatan:**
- dapat menggunakan password lokal masing-masing.
- File `.env` tidak boleh diunggah ke GitHub.
- Jangan mengubah nama database dan username tanpa menyesuaikan konfigurasi Docker.

## 5. Menjalankan PostgreSQL dengan Docker

Buka Docker Desktop
Pastikan Docker Desktop sudah aktif.

Jalankan PostgreSQL:

```powershell
docker compose up -d
```

Periksa status container:

```powershell
docker compose ps
```

Pastikan container PostgreSQL menunjukkan status `healthy`.

PostgreSQL berjalan dengan konfigurasi:

| Konfigurasi | Nilai |
|---|---|
| Database | pcm_django |
| Username | pcm_user |
| Port komputer | 5433 |
| Port container | 5432 |
| Image | postgres:17-alpine |

Port komputer menggunakan 5433 agar tidak bertabrakan dengan PostgreSQL proyek lain.

Jika port 5433 sudah digunakan, ubah port host pada `compose.yaml` dan sesuaikan `DB_PORT` pada `.env`.

## 6. Migrasi Database

Setelah PostgreSQL berjalan, jalankan migrasi Django:

```powershell
uv run python manage.py migrate
```

Perintah tersebut akan membuat tabel database berdasarkan migration yang tersedia di proyek.

Untuk memeriksa status migrasi:

```powershell
uv run python manage.py showmigrations
```


### 7. Buat tabel database

```bash
uv run python manage.py migrate
```

Perintah ini membuat file `db.sqlite3` di folder proyek.

### 8. Muat data awal

```bash
uv run python manage.py seed_pcm
```

Command ini memuat data awal (profil, pimpinan, ranting, amal usaha, berita, agenda) dari `pcm/fixtures/data_awal.json`. Gunakan database yang masih kosong. Jika database sudah berisi data dengan ID yang sama, datanya akan tertimpa.

> **Catatan:** foto yang dirujuk data awal tersimpan di folder `media/` dan ikut repository, jadi gambar di hero, kartu pimpinan, berita, dan amal usaha tampil setelah data dimuat. Foto yang diunggah lewat admin setelah itu hanya tersimpan di komputer yang mengunggahnya.

### 9. Buat akun administrator

```bash
uv run python manage.py createsuperuser
```

Ikuti instruksi untuk mengisi username, email, dan password. Akun ini hanya berlaku di database lokal masing-masing.

### 10. Jalankan server

```bash
uv run python manage.py runserver
```

Buka `http://127.0.0.1:8000/`. Panel admin ada di `http://127.0.0.1:8000/admin/`. Tekan `Ctrl + C` untuk menghentikan server.

## Perintah yang Sering Dipakai

| Kebutuhan | Perintah |
|---|---|
| Pasang dependency | `uv sync` |
| Migrasi database | `uv run python manage.py migrate` |
| Buat migrasi setelah mengubah model | `uv run python manage.py makemigrations pcm` |
| Muat data awal | `uv run python manage.py seed_pcm` |
| Jalankan server | `uv run python manage.py runserver` |
| Buat administrator | `uv run python manage.py createsuperuser` |
| Cek konfigurasi | `uv run python manage.py check` |
| Tambah paket baru | `uv add nama-paket` |

## Struktur Proyek

```text
tugas-pcm/
├── manage.py
├── pyproject.toml          # daftar dependency
├── uv.lock                 # versi dependency yang dikunci
├── .python-version
├── .env.example            # contoh konfigurasi (di-commit)
├── .env                    # konfigurasi asli (tidak di-commit)
├── config/                 # pengaturan Django (settings, urls)
├── pcm/                    # aplikasi utama
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── context_processors.py
│   ├── management/
│   │   └── commands/
│   │       └── seed_pcm.py # command pengisi data awal
│   └── fixtures/
│       └── data_awal.json
├── media/                  # foto yang dirujuk data awal
│   ├── profil/
│   ├── pimpinan/
│   ├── amal_usaha/
│   └── berita/
├── templates/
│   ├── base.html
│   └── pcm/
└── static/
    ├── css/style.css
    └── img/
```

## Alur Kerja Tim

1. Sebelum mulai bekerja: `git pull`.
2. Jika ada perubahan pada `pcm/models.py` atau folder `migrations`: `uv sync` lalu `uv run python manage.py migrate`.
3. Setelah selesai: `git add .`, `git commit -m "pesan perubahan"`, lalu `git push`.

Yang **tidak** ikut repository: `.venv/`, `db.sqlite3`, `.env`, dan `staticfiles/`. Data yang diisi lewat admin hanya tersimpan di database lokal masing-masing. Folder `media/` ikut repository, tetapi hanya berisi foto untuk data awal.

## Pemecahan Masalah

| Gejala | Penyebab dan solusi |
|---|---|
| `KeyError: 'SECRET_KEY'` | File `.env` belum dibuat atau `SECRET_KEY` kosong. Ulangi langkah 3. Pastikan `.env` sejajar dengan `manage.py` |
| `No module named 'dotenv'` | Dependency belum terpasang. Jalankan `uv sync` |
| `No installed app with label 'pcm'` | `'pcm'` belum ada di `INSTALLED_APPS` pada `config/settings.py` |
| Halaman menampilkan "Belum ada ..." | Data awal belum dimuat. Jalankan langkah 5 atau isi lewat admin |
| Gambar tidak tampil | Data awal belum dimuat (langkah 5), atau isi folder `media/` tidak lengkap setelah clone. Foto yang diunggah lewat admin di komputer lain juga tidak ikut |
| `TemplateDoesNotExist` | Nama atau letak file template tidak sesuai. `base.html` ada di `templates/`, sedangkan template halaman ada di `templates/pcm/` |
| Versi Python tidak sesuai | Jalankan `uv python install 3.14`, lalu `uv sync` |

## Keamanan

- Jangan memasukkan `SECRET_KEY`, password, atau kunci API ke repository, termasuk ke riwayat commit.
- Jangan membagikan isi file `.env`.
- `DEBUG=True` hanya untuk lokal.

## Dalam Pengembangan

- Halaman dokumen dan formulir kontak
- Pengujian otomatis
- Docker dengan PostgreSQL
- Deployment

## Atribusi

Logo Muhammadiyah: K. H. Siradj Dahlan, vektor oleh Hibensis, via Wikimedia Commons, lisensi CC BY-SA 4.0.
