"""Program Rekap dan Analisis Nilai Matematika Kelas.

Jalankan dari root proyek:
    python3 src/main.py
    python3 src/main.py data/nilai_contoh.txt 75
(argumen opsional: path file data, lalu nilai KKM)
"""

import os
import sys

from analisis import hitung_ketuntasan, hitung_statistik
from data_io import baca_data, simpan_laporan
from utilitas import KKM_DEFAULT, format_laporan, validasi_nilai

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DEFAULT = os.path.join(ROOT, "data", "nilai_contoh.txt")
LAPORAN_DEFAULT = os.path.join(ROOT, "output", "laporan.txt")


def main(path_data=DATA_DEFAULT, kkm=KKM_DEFAULT, path_laporan=LAPORAN_DEFAULT):
    """Mengatur alur program. Mengembalikan 0 jika sukses, 1 jika gagal."""
    try:
        data, ditolak = baca_data(path_data)
    except FileNotFoundError:
        print(f"File tidak ditemukan: {path_data}")
        return 1
    except PermissionError:
        print(f"Tidak ada izin membaca file: {path_data}")
        return 1

    for nomor, baris, alasan in ditolak:
        print(f"Baris {nomor} ditolak ({alasan}): {baris}")

    if not data:
        print("Tidak ada data valid untuk direkap.")
        return 1

    statistik = hitung_statistik(data)
    tuntas, belum_tuntas = hitung_ketuntasan(data, kkm)
    laporan = format_laporan(data, statistik, tuntas, belum_tuntas, kkm, len(ditolak))
    print()
    print(laporan)

    try:
        simpan_laporan(path_laporan, laporan)
    except OSError as galat:
        print(f"Laporan gagal disimpan: {galat}")
        return 1

    print(f"Laporan disimpan ke {path_laporan}")
    return 0


def baca_argumen(argv):
    """Membaca argumen opsional: [path_data] [kkm]. Mengembalikan (path, kkm) atau None."""
    path_data = argv[1] if len(argv) > 1 else DATA_DEFAULT
    kkm = KKM_DEFAULT
    if len(argv) > 2:
        try:
            kkm = float(argv[2])
        except ValueError:
            print("KKM harus berupa angka.")
            return None
        if not validasi_nilai(kkm):
            print("KKM harus berada pada rentang 0-100.")
            return None
    return path_data, kkm


if __name__ == "__main__":
    argumen = baca_argumen(sys.argv)
    if argumen is None:
        sys.exit(2)
    sys.exit(main(argumen[0], argumen[1]))
