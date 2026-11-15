# PCM Gemolong — Django Website

Repository pengembangan website Pimpinan Cabang Muhammadiyah (PCM) Gemolong menggunakan Django dan PostgreSQL.

## 1. Teknologi yang Digunakan

- Python
- Django
- PostgreSQL 17
- Docker dan Docker Compose
- uv (Python package manager)

## 2. Persyaratan Instalasi

Sebelum menjalankan proyek, pastikan perangkat sudah memiliki:

1. Git
2. Python
3. uv
4. Docker Desktop
5. Visual Studio Code (disarankan)

Pastikan Docker Desktop sudah berjalan sebelum melanjutkan.

## 3. Clone Repository

Buka terminal PowerShell, kemudian jalankan:

```powershell
git clone https://github.com/l200240164-galihwikuu/tif1336-2026-tugas1-membangun-website-pcm-dengan-django-kelompokM.git
```

Masuk ke direktori proyek:

```powershell
cd tif1336-2026-tugas1-membangun-website-pcm-dengan-django-kelompokM
```

## 4. Instalasi Dependency

Install seluruh dependency berdasarkan konfigurasi proyek:

```powershell
uv sync
```

Perintah ini akan membuat virtual environment dan memasang dependency sesuai `uv.lock`.

## 5. Konfigurasi Environment

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
- Setiap anggota boleh menggunakan password lokal masing-masing.
- File `.env` tidak boleh diunggah ke GitHub.
- Jangan mengubah nama database dan username tanpa menyesuaikan konfigurasi Docker.

## 6. Menjalankan PostgreSQL dengan Docker

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

## 7. Migrasi Database

Setelah PostgreSQL berjalan, jalankan migrasi Django:

```powershell
uv run python manage.py migrate
```

Perintah tersebut akan membuat tabel database berdasarkan migration yang tersedia di proyek.

Untuk memeriksa status migrasi:

```powershell
uv run python manage.py showmigrations
```

## 8. Membuat Akun Administrator

Jika ingin mengakses halaman admin Django, buat akun administrator sendiri:

```powershell
uv run python manage.py createsuperuser
```

Ikuti instruksi untuk mengisi username, email, dan password.

## 9. Menjalankan Development Server

Jalankan server Django:

```powershell
uv run python manage.py runserver
```

Buka browser dan akses:

- Website: http://127.0.0.1:8000/
- Django Admin: http://127.0.0.1:8000/admin/

Untuk menghentikan server, tekan `CTRL + C` pada terminal.

## 10. Menghentikan PostgreSQL

Untuk menghentikan container:

```powershell
docker compose stop
```

Untuk menjalankan kembali:

```powershell
docker compose start
```

Atau jika ingin menghentikan dan menghapus container beserta network proyek:

```powershell
docker compose down
```

**Penting:** Jangan menggunakan `docker compose down -v` jika masih ingin mempertahankan data database lokal. Opsi `-v` akan menghapus volume PostgreSQL.

## 11. Sinkronisasi Perubahan dari GitHub

Sebelum mulai mengerjakan fitur, pastikan mengambil perubahan terbaru:

```powershell
git pull origin main
```

Jika ada perubahan dependency dari anggota lain, jalankan:

```powershell
uv sync
```

Jika terdapat perubahan struktur database atau migration baru, jalankan:

```powershell
uv run python manage.py migrate
```
