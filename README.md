# Proyek Akhir - Rekap dan Analisis Nilai Matematika Kelas

Tim: solo
Anggota: Wulan Nur'aini 2225250131
Kelas: 3E
Repository: https://github.com/wulannuraini699/proyek-akhir-wulan-nuraini-solo.git

## Deskripsi

Program console Python untuk guru matematika: membaca data nilai dari file, memvalidasi isinya,
menghitung statistik kelas, menentukan status ketuntasan berdasarkan KKM, dan menyimpan laporan.
Rancangan lengkap ada di [proposal.md](proposal.md).

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

Python 3 (tanpa library tambahan).

## Cara Menjalankan

Jalankan dari root folder proyek:

```
python3 src/main.py
```

Dengan file data dan KKM sendiri (argumen opsional):

```
python3 src/main.py data/nilai_contoh.txt 75
```

Tanpa argumen, program memakai `data/nilai_contoh.txt` dan KKM 70.

## Format File Data

Satu siswa per baris dengan format `NIM,nama,nilai`. Baris kosong dilewati.

```
A001,Ayu,85
A002,Budi,78
```

Baris dengan format salah, nilai bukan angka, nilai di luar 0-100, atau NIM ganda akan ditolak
dengan pesan yang menyebut nomor baris dan alasannya, sedangkan baris lain tetap diproses.

## Contoh Keluaran

```
Baris 8 ditolak (nilai di luar rentang 0-100): A007,Gita,105
Baris 9 ditolak (nilai bukan angka): A008,Hadi,abc

LAPORAN REKAP NILAI 
KKM           : 70
Data valid    : 6
Baris ditolak : 2
Rata-rata     : 74.67
Minimum       : 58.00 (Fani)
Maksimum      : 92.00 (Citra)
Tuntas        : 4
Belum tuntas  : 2

NIM     Nama          Nilai  Status
A001    Ayu           85.00  Tuntas
A002    Budi          78.00  Tuntas
A003    Citra         92.00  Tuntas
A004    Dani          65.00  Belum tuntas
A005    Eka           70.00  Tuntas
A006    Fani          58.00  Belum tuntas
```

## Struktur Proyek

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
|   |-- test_case.md       (rancangan dan hasil test case)
|   `-- test_otomatis.py   (menjalankan test case)
`-- output/.gitkeep
```

## Pengujian

```
python3 tests/test_otomatis.py
```

Hasil terakhir: 12 test, 12 PASS, 0 FAIL. Daftar test case ada di [tests/test_case.md](tests/test_case.md).

## Pembagian Tugas

| Peran | PIC | File |
|-------|-----|------|
| Koordinator | ... | `main.py`, `utilitas.py`, `proposal.md` |
| Programmer Data I/O | ... | `data_io.py` |
| Programmer Logika | ... | `analisis.py` |
| Tester/QA | ... | `tests/` |
| Dokumentasi | ... | `README.md` |

## Catatan Sumber dan Bantuan

(Tuliskan sumber belajar dan bantuan AI yang berpengaruh pada rancangan, sesuai kebijakan kelas.)
