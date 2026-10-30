# Bug Log

Bug ditemukan pada Pertemuan 15 saat pengujian lanjutan (TC13 sampai TC20) terhadap kode hasil Pertemuan 14.
Setiap bug dibuktikan dahulu dengan test case yang gagal sebelum diperbaiki.

| ID | Gejala | Test case | Lokasi | Akar penyebab | Perbaikan | Retest | Status |
|----|--------|-----------|--------|---------------|-----------|--------|--------|
| BUG-01 | NIM pada baris pertama menjadi `\ufeffA1` jika file data disimpan dari Notepad Windows sebagai UTF-8 dengan BOM | TC14 | `src/data_io.py`, fungsi `baca_data()`, baris `open(..., encoding="utf-8")` | Encoding `utf-8` tidak membuang BOM, sehingga karakter tersembunyi menempel pada NIM pertama (NIM tampak benar saat dicetak, tetapi tidak sama dengan `A1`) | (belum diperbaiki) | - | Open |
| BUG-02 | Program berhenti dengan traceback jika path berupa folder (`IsADirectoryError`) atau isi file bukan teks UTF-8 (`UnicodeDecodeError`) | TC15, TC16 | `src/main.py`, fungsi `main()`, blok `try-except` pada `baca_data()` | Hanya `FileNotFoundError` dan `PermissionError` yang ditangani. `UnicodeDecodeError` termasuk `ValueError`, sedangkan `IsADirectoryError` termasuk `OSError`, sehingga keduanya lolos | (belum diperbaiki) | - | Open |
| BUG-03 | Kolom nilai pada tabel laporan tidak sejajar jika ada nama yang panjang | TC17 | `src/utilitas.py`, fungsi `format_laporan()` | Lebar kolom ditulis tetap (8 untuk NIM dan 12 untuk nama), padahal panjang nama bervariasi (magic number) | (belum diperbaiki) | - | Open |
