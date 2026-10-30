# Proyek Akhir - Rekap dan Analisis Nilai Matematika Kelas

Tim: solo
Anggota: Wulan Nur'aini 2225250131
Kelas: 3E
Repository: https://github.com/wulannuraini699/proyek-akhir-wulan-nuraini-solo.git

## Deskripsi

Program console Python untuk guru matematika: membaca data nilai dari file, memvalidasi isinya,
menghitung statistik kelas, menentukan status ketuntasan berdasarkan KKM, dan menyimpan laporan.
Masalah, kebutuhan, dan rancangan lengkap ada di [proposal.md](proposal.md).

## Fitur

| ID | Fitur | Status |
|----|-------|--------|
| F01 | Membaca data nilai dari file | Selesai |
| F02 | Validasi format baris dan nilai 0-100 | Selesai |
| F03 | Rata-rata, minimum, maksimum | Selesai |
| F04 | Status tuntas/belum tuntas berdasarkan KKM | Selesai |
| F05 | Menyimpan laporan ke `output/laporan.txt` | Selesai |
| F06 | Statistik per kategori | Belum (fitur tambahan) |

## Persyaratan

- Python 3.8 atau lebih baru
- Tidak ada library tambahan (hanya pustaka standar Python)

## Cara Menjalankan

Dari root folder proyek:

```
git clone https://github.com/wulannuraini699/proyek-akhir-wulan-nuraini-solo.git
cd proyek-akhir-wulan-nuraini-solo
python3 src/main.py
```

Dengan file data dan KKM sendiri (argumen opsional: path data, lalu KKM):

```
python3 src/main.py data/nilai_contoh.txt 75
```

Tanpa argumen, program memakai `data/nilai_contoh.txt` dan KKM 70. Hasil laporan ditulis ke
`output/laporan.txt`. Di Windows, gunakan `python` atau `py` jika `python3` tidak dikenali.

## Format File Data

Satu siswa per baris dengan format `NIM,nama,nilai`. Gunakan titik untuk desimal (`85.5`).
Baris kosong dilewati. Baris yang formatnya salah, nilainya bukan angka, di luar 0-100, atau
NIM-nya ganda akan ditolak dengan pesan nomor baris dan alasan; baris lain tetap diproses.

```
A001,Ayu,85
A002,Budi,78
```

## Contoh Keluaran

Lihat [docs/contoh_keluaran.txt](docs/contoh_keluaran.txt) (hasil `python3 src/main.py` dengan data contoh).

## Struktur Folder

```
proyek-akhir-nama-tim/
|-- README.md
|-- proposal.md
|-- .gitignore
|-- data/nilai_contoh.txt
|-- src/
|   |-- main.py        (alur program)
|   |-- data_io.py     (baca data, simpan laporan)
|   |-- analisis.py    (statistik, ketuntasan)
|   `-- utilitas.py    (validasi, format laporan)
|-- tests/
|   |-- test_case.md       (rancangan, hasil awal, dan hasil akhir test case)
|   `-- test_otomatis.py   (menjalankan TC01-TC20)
|-- docs/
|   |-- bug_log.md         (catatan bug dan perbaikan)
|   `-- contoh_keluaran.txt
`-- output/.gitkeep
```

## Test Case

Dijalankan dengan:

```
python3 tests/test_otomatis.py
```

Hasil terakhir: **20 test, 20 PASS, 0 FAIL**. Rincian (termasuk hasil awal sebelum perbaikan)
ada di [tests/test_case.md](tests/test_case.md).

| ID | Kategori | Input/Kondisi | Expected | Status |
|----|----------|---------------|----------|--------|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80.0 | PASS |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid | PASS |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid | PASS |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan "di luar rentang 0-100" | PASS |
| TC05 | Invalid | File tidak ada | Pesan "tidak ditemukan", program tidak crash | PASS |
| TC06 | Normal | Semua nilai >= KKM (80, 90, 70) | Tuntas = 3, belum tuntas = 0 | PASS |
| TC07 | Batas | Nilai tepat sama dengan KKM (70) | Status Tuntas | PASS |
| TC08 | Invalid | Satu nilai "abc" di antara data valid | Baris "abc" ditolak, 2 data lain diproses | PASS |
| TC09 | Batas | File berisi baris kosong | Baris kosong dilewati, tidak dihitung ditolak | PASS |
| TC10 | Invalid | Semua baris tidak valid | Pesan "tidak ada data valid", laporan tidak dibuat | PASS |
| TC11 | Invalid | NIM duplikat | Baris kedua ditolak, data pertama dipertahankan | PASS |
| TC12 | Normal | Data valid (80 dan 60) | File laporan tersimpan, memuat rata-rata 70.00 | PASS |
| TC13 | Kosong | File kosong (0 byte) | Pesan "Tidak ada data valid", program tidak crash | PASS |
| TC14 | Invalid | File UTF-8 dengan BOM (disimpan Notepad) | NIM terbaca bersih: A1, A2 | PASS |
| TC15 | Invalid | Path menunjuk ke folder, bukan file | Pesan "File tidak dapat dibaca", tidak crash | PASS |
| TC16 | Invalid | File bukan teks UTF-8 (biner) | Pesan file harus UTF-8, tidak crash | PASS |
| TC17 | Normal | Nama panjang pada tabel laporan | Kolom nilai pada tabel sejajar | PASS |
| TC18 | Invalid | Argumen KKM "abc" atau "150" | Ditolak dengan pesan, KKM 75 diterima | PASS |
| TC19 | Normal | Nilai desimal 85.5 dan 74.5 | Diterima; rata-rata 80.0 | PASS |
| TC20 | Invalid | Nilai "nan" dan "inf" | Keduanya ditolak | PASS |

## Bug yang Ditemukan dan Diperbaiki

Tiga bug ditemukan pada pengujian lanjutan Pertemuan 15 (TC14 sampai TC17) dan sudah diperbaiki:
BUG-01 (BOM pada file data), BUG-02 (error tidak tertangani pada path folder dan file non-UTF-8),
dan BUG-03 (tabel laporan tidak sejajar). Rincian ada di [docs/bug_log.md](docs/bug_log.md).

## Known Issues

- File data tidak boleh memuat baris judul (header).
- Pemisah desimal harus titik, bukan koma.
- Nama tidak boleh mengandung koma.
- NIM peka huruf besar/kecil.
- F06 (statistik per kategori) belum diimplementasikan.

## Anggota dan Kontribusi

| Peran | PIC | Kontribusi |
|-------|-----|------------|
| Koordinator | Wulan Nur'aini | `main.py` (BUG-02), `utilitas.py` (BUG-03), `proposal.md`, integrasi |
| Programmer Data I/O | Wulan Nur'aini | `data_io.py` (BUG-01) |
| Programmer Logika | Wulan Nur'aini | `analisis.py`, regression check fungsi statistik |
| Tester/QA | Wulan Nur'aini | `tests/` (TC13-TC20), `docs/bug_log.md` |
| Dokumentasi | Wulan Nur'aini | `README.md`, `docs/contoh_keluaran.txt` |

## Referensi dan Bantuan

docs/screenshot/hasil_test.png

Penyusunan tugas akhir ini dibantu oleh claude.ai dan gemini.ai
