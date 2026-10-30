# Bug Log

Bug ditemukan pada Pertemuan 15 saat pengujian lanjutan (TC13 sampai TC20) terhadap kode hasil Pertemuan 14.
Setiap bug dibuktikan dahulu dengan test case yang gagal sebelum diperbaiki.

| ID | Gejala | Test case | Lokasi | Akar penyebab | Perbaikan | Retest | Status |
|----|--------|-----------|--------|---------------|-----------|--------|--------|
| BUG-01 | NIM pada baris pertama menjadi `\ufeffA1` jika file data disimpan dari Notepad Windows sebagai UTF-8 dengan BOM | TC14 | `src/data_io.py`, fungsi `baca_data()`, baris `open(..., encoding="utf-8")` | Encoding `utf-8` tidak membuang BOM, sehingga karakter tersembunyi menempel pada NIM pertama (NIM tampak benar saat dicetak, tetapi tidak sama dengan `A1`) | Mengganti encoding menjadi `utf-8-sig`, yang membuang BOM jika ada dan berperilaku sama jika tidak ada | TC14 PASS; TC01 sampai TC13 tetap PASS | Closed |
| BUG-02 | Program berhenti dengan traceback jika path berupa folder (`IsADirectoryError`) atau isi file bukan teks UTF-8 (`UnicodeDecodeError`) | TC15, TC16 | `src/main.py`, fungsi `main()`, blok `try-except` pada `baca_data()` | Hanya `FileNotFoundError` dan `PermissionError` yang ditangani. `UnicodeDecodeError` termasuk `ValueError`, sedangkan `IsADirectoryError` termasuk `OSError`, sehingga keduanya lolos | Menambah `except UnicodeDecodeError` dan `except OSError` setelah `FileNotFoundError`; pesan menyebutkan penyebab dan program mengembalikan kode 1 | TC15 dan TC16 PASS; TC05 (file hilang) tetap PASS | Closed |
| BUG-03 | Kolom nilai pada tabel laporan tidak sejajar jika ada nama yang panjang | TC17 | `src/utilitas.py`, fungsi `format_laporan()` | Lebar kolom ditulis tetap (8 untuk NIM dan 12 untuk nama), padahal panjang nama bervariasi (magic number) | Lebar kolom dihitung dari data terpanjang ditambah 2 spasi | TC17 PASS; TC12 (isi laporan) tetap PASS | Closed |

## Known Issues (tidak diperbaiki, di luar ruang lingkup proposal)

- File data tidak boleh memuat baris judul (header). Baris judul akan ditolak sebagai "nilai bukan angka".
- Pemisah desimal harus titik (`85.5`). Koma (`85,5`) menambah kolom sehingga baris ditolak.
- Nama tidak boleh mengandung koma, karena koma adalah pemisah kolom.
- NIM peka huruf besar/kecil (`a001` dan `A001` dianggap NIM berbeda).
- F06 (statistik per kategori) belum diimplementasikan.
