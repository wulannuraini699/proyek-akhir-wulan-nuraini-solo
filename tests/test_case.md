# Test Case Proyek: Rekap dan Analisis Nilai Matematika Kelas

Test case dirancang sebelum implementasi penuh agar definisi berhasil dan gagal sudah jelas.
Hasil pengujian dicatat setelah implementasi (dijalankan dengan `python3 tests/test_otomatis.py`: 12 test, 12 PASS, 0 FAIL).
KKM yang dipakai pada pengujian: 70 (kecuali dinyatakan lain).

| ID | Kategori | Fitur | Input/Kondisi | Expected Result | Actual | Status |
|----|----------|-------|---------------|-----------------|--------|--------|
| TC01 | Normal | F03 | Nilai 80, 70, 90 | Rata-rata 80.0 | sesuai expected | PASS |
| TC02 | Batas | F02 | Nilai 0 | Diterima sebagai nilai valid | sesuai expected | PASS |
| TC03 | Batas | F02 | Nilai 100 | Diterima sebagai nilai valid | sesuai expected | PASS |
| TC04 | Invalid | F02 | Nilai 105 | Ditolak dengan pesan "di luar rentang 0-100" | sesuai expected | PASS |
| TC05 | Invalid | F01 | File tidak ada | `FileNotFoundError` ditangani, muncul pesan, program tidak crash | sesuai expected | PASS |
| TC06 | Normal | F04 | Semua nilai >= KKM (80, 90, 70) | Tuntas = 3, belum tuntas = 0 | sesuai expected | PASS |
| TC07 | Batas | F04 | Nilai tepat sama dengan KKM (70) | Status Tuntas | sesuai expected | PASS |
| TC08 | Invalid | F02 | Satu nilai "abc" di antara data valid | Baris "abc" ditolak, 2 data lain diproses | sesuai expected | PASS |
| TC09 | Batas | F01 | File berisi baris kosong | Baris kosong dilewati, tidak dihitung sebagai ditolak | sesuai expected | PASS |
| TC10 | Invalid | F01, F05 | Semua baris tidak valid | Pesan "tidak ada data valid", laporan tidak dibuat, tidak crash | sesuai expected | PASS |
| TC11 | Invalid | F02 | NIM duplikat | Baris kedua ditolak, data pertama dipertahankan | sesuai expected | PASS |
| TC12 | Normal | F05 | Data valid (80 dan 60) | File laporan tersimpan dan memuat rata-rata 70.00 | sesuai expected | PASS |

## Definition of Done

- [x] Semua fitur wajib (F01 sampai F05) berjalan.
- [x] Semua test case wajib lulus.
- [x] Program tidak berhenti karena error yang sudah diprediksi.
- [x] Output mudah dibaca.
- [x] README menjelaskan cara menjalankan.
- [ ] Commit proyek menunjukkan kontribusi tim.