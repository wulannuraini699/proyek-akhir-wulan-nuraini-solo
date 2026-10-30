# Test Case Proyek: Rekap dan Analisis Nilai Matematika Kelas

Test case TC01 sampai TC12 dirancang pada Pertemuan 14. TC13 sampai TC20 ditambahkan pada
Pertemuan 15 untuk kondisi kosong, encoding, path tidak wajar, tampilan, dan argumen.
Dijalankan dengan `python3 tests/test_otomatis.py`. KKM pengujian: 70 (kecuali dinyatakan lain).

## Hasil sebelum perbaikan

Ringkasan: 20 test, 16 PASS, 4 FAIL (TC14, TC15, TC16, TC17). Bug dicatat di `docs/bug_log.md`.

| ID | Kategori | Fitur | Input/Kondisi | Expected Result | Actual | Status |
|----|----------|-------|---------------|-----------------|--------|--------|
| TC01 | Normal | F03 | Nilai 80, 70, 90 | Rata-rata 80.0 | sesuai expected | PASS |
| TC02 | Batas | F02 | Nilai 0 | Diterima sebagai nilai valid | sesuai expected | PASS |
| TC03 | Batas | F02 | Nilai 100 | Diterima sebagai nilai valid | sesuai expected | PASS |
| TC04 | Invalid | F02 | Nilai 105 | Ditolak dengan pesan "di luar rentang 0-100" | sesuai expected | PASS |
| TC05 | Invalid | F01 | File tidak ada | Pesan "tidak ditemukan", program tidak crash | sesuai expected | PASS |
| TC06 | Normal | F04 | Semua nilai >= KKM (80, 90, 70) | Tuntas = 3, belum tuntas = 0 | sesuai expected | PASS |
| TC07 | Batas | F04 | Nilai tepat sama dengan KKM (70) | Status Tuntas | sesuai expected | PASS |
| TC08 | Invalid | F02 | Satu nilai "abc" di antara data valid | Baris "abc" ditolak, 2 data lain diproses | sesuai expected | PASS |
| TC09 | Batas | F01 | File berisi baris kosong | Baris kosong dilewati, tidak dihitung ditolak | sesuai expected | PASS |
| TC10 | Invalid | F01, F05 | Semua baris tidak valid | Pesan "tidak ada data valid", laporan tidak dibuat | sesuai expected | PASS |
| TC11 | Invalid | F02 | NIM duplikat | Baris kedua ditolak, data pertama dipertahankan | sesuai expected | PASS |
| TC12 | Normal | F05 | Data valid (80 dan 60) | File laporan tersimpan, memuat rata-rata 70.00 | sesuai expected | PASS |
| TC13 | Kosong | F01 | File kosong (0 byte) | Pesan "Tidak ada data valid", program tidak crash | sesuai expected | PASS |
| TC14 | Invalid | F01 | File UTF-8 dengan BOM (disimpan Notepad) | NIM terbaca bersih: A1, A2 | NIM baris pertama tersimpan "\ufeffA1" (ada karakter tersembunyi) | FAIL |
| TC15 | Invalid | F01 | Path menunjuk ke folder, bukan file | Pesan "File tidak dapat dibaca", tidak crash | Program berhenti dengan traceback IsADirectoryError | FAIL |
| TC16 | Invalid | F01 | File bukan teks UTF-8 (biner) | Pesan file harus UTF-8, tidak crash | Program berhenti dengan traceback UnicodeDecodeError | FAIL |
| TC17 | Normal | F05 | Nama panjang pada tabel laporan | Kolom nilai pada tabel sejajar | Kolom nilai bergeser pada baris dengan nama panjang | FAIL |
| TC18 | Invalid | F04 | Argumen KKM "abc" atau "150" | Ditolak dengan pesan, KKM 75 diterima | sesuai expected | PASS |
| TC19 | Normal | F02, F03 | Nilai desimal 85.5 dan 74.5 | Diterima; rata-rata 80.0 | sesuai expected | PASS |
| TC20 | Invalid | F02 | Nilai "nan" dan "inf" | Keduanya ditolak | sesuai expected | PASS |
