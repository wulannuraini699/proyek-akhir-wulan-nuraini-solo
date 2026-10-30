"""Membaca data nilai dari file dan menyimpan laporan ke file."""

import os

from utilitas import validasi_nilai


def baca_data(path):
    """Membaca file berformat NIM,nama,nilai (satu record per baris).

    Mengembalikan (data, ditolak):
      data    : dictionary {nim: {"nama": ..., "nilai": ...}} untuk baris valid
      ditolak : list of (nomor_baris, isi_baris, alasan) untuk baris tidak valid
    Baris kosong dilewati. FileNotFoundError diteruskan ke pemanggil.
    File dibaca dengan utf-8-sig agar BOM (penanda awal file dari Notepad
    Windows) dibuang dan tidak menempel pada NIM baris pertama.
    """
    data = {}
    ditolak = []

    with open(path, "r", encoding="utf-8-sig") as file:
        for nomor, baris in enumerate(file, start=1):
            baris = baris.strip()
            if not baris:
                continue

            bagian = [b.strip() for b in baris.split(",")]
            if len(bagian) != 3:
                ditolak.append((nomor, baris, "format harus NIM,nama,nilai"))
                continue

            nim, nama, teks_nilai = bagian
            if not nim or not nama:
                ditolak.append((nomor, baris, "NIM atau nama kosong"))
                continue

            try:
                nilai = float(teks_nilai)
            except ValueError:
                ditolak.append((nomor, baris, "nilai bukan angka"))
                continue

            if not validasi_nilai(nilai):
                ditolak.append((nomor, baris, "nilai di luar rentang 0-100"))
                continue

            if nim in data:
                ditolak.append((nomor, baris, "NIM duplikat"))
                continue

            data[nim] = {"nama": nama, "nilai": nilai}

    return data, ditolak


def simpan_laporan(path, teks):
    """Menulis teks laporan ke file; folder tujuan dibuat jika belum ada."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        file.write(teks)
