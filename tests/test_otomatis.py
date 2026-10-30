"""
Test otomatis proyek (menjalankan test case TC01-TC12 pada tests/test_case.md).

Jalankan dari root proyek:
    python3 tests/test_otomatis.py
"""

import contextlib
import io
import os
import sys
import tempfile

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
sys.path.insert(0, SRC)

import main as program  # noqa: E402
from analisis import hitung_ketuntasan, hitung_statistik, tentukan_status  # noqa: E402
from data_io import baca_data  # noqa: E402
from utilitas import validasi_nilai  # noqa: E402


def tulis(folder, nama, isi):
    path = os.path.join(folder, nama)
    with open(path, "w", encoding="utf-8") as file:
        file.write(isi)
    return path


def jalankan_main(path_data, kkm=70, path_laporan=None):
    """Menjalankan main() dan menangkap teks yang ditampilkan."""
    keluaran = io.StringIO()
    with contextlib.redirect_stdout(keluaran):
        kode = program.main(path_data, kkm, path_laporan)
    return kode, keluaran.getvalue()


# Setiap test mengembalikan (aktual, expected).
def tc01():
    with tempfile.TemporaryDirectory() as t:
        data, _ = baca_data(tulis(t, "n.txt", "A1,Ani,80\nA2,Bo,70\nA3,Cici,90\n"))
        return hitung_statistik(data)["rata_rata"], 80.0


def tc02():
    return validasi_nilai(0), True


def tc03():
    return validasi_nilai(100), True


def tc04():
    with tempfile.TemporaryDirectory() as t:
        data, ditolak = baca_data(tulis(t, "n.txt", "A1,Ani,105\n"))
        return (len(data), len(ditolak), "0-100" in ditolak[0][2]), (0, 1, True)


def tc05():
    with tempfile.TemporaryDirectory() as t:
        kode, teks = jalankan_main(os.path.join(t, "tidak_ada.txt"))
        return (kode, "tidak ditemukan" in teks), (1, True)


def tc06():
    with tempfile.TemporaryDirectory() as t:
        data, _ = baca_data(tulis(t, "n.txt", "A1,Ani,80\nA2,Bo,90\nA3,Cici,70\n"))
        return hitung_ketuntasan(data, 70), (3, 0)


def tc07():
    return tentukan_status(70, 70), "Tuntas"


def tc08():
    with tempfile.TemporaryDirectory() as t:
        data, ditolak = baca_data(tulis(t, "n.txt", "A1,Ani,80\nA2,Bo,abc\nA3,Cici,90\n"))
        return (len(data), len(ditolak)), (2, 1)


def tc09():
    with tempfile.TemporaryDirectory() as t:
        data, ditolak = baca_data(tulis(t, "n.txt", "A1,Ani,80\n\n   \nA2,Bo,90\n"))
        return (len(data), len(ditolak)), (2, 0)


def tc10():
    with tempfile.TemporaryDirectory() as t:
        sumber = tulis(t, "n.txt", "A1,Ani,abc\nA2,Bo,150\n")
        laporan = os.path.join(t, "laporan.txt")
        kode, _ = jalankan_main(sumber, 70, laporan)
        return (kode, os.path.exists(laporan)), (1, False)


def tc11():
    with tempfile.TemporaryDirectory() as t:
        data, ditolak = baca_data(tulis(t, "n.txt", "A1,Ani,80\nA1,Ani,90\n"))
        return (len(data), len(ditolak)), (1, 1)


def tc12():
    with tempfile.TemporaryDirectory() as t:
        sumber = tulis(t, "n.txt", "A1,Ani,80\nA2,Bo,60\n")
        laporan = os.path.join(t, "keluaran", "laporan.txt")
        kode, _ = jalankan_main(sumber, 70, laporan)
        isi = open(laporan, encoding="utf-8").read() if os.path.exists(laporan) else ""
        return (kode, "Rata-rata     : 70.00" in isi), (0, True)


TESTS = [
    ("TC01", "Normal", "Rata-rata nilai 80, 70, 90", tc01),
    ("TC02", "Batas", "Nilai 0 valid", tc02),
    ("TC03", "Batas", "Nilai 100 valid", tc03),
    ("TC04", "Invalid", "Nilai 105 ditolak", tc04),
    ("TC05", "Invalid", "File tidak ada ditangani", tc05),
    ("TC06", "Normal", "Semua nilai >= KKM", tc06),
    ("TC07", "Batas", "Nilai tepat KKM tuntas", tc07),
    ("TC08", "Invalid", "Nilai 'abc' ditolak, lainnya diproses", tc08),
    ("TC09", "Batas", "Baris kosong dilewati", tc09),
    ("TC10", "Invalid", "Semua baris invalid", tc10),
    ("TC11", "Invalid", "NIM duplikat ditolak", tc11),
    ("TC12", "Normal", "Laporan tersimpan ke file", tc12),
]


def jalankan():
    gagal = 0
    print(f"{'ID':<6}{'Kategori':<10}{'Deskripsi':<42}Status")
    print("-" * 66)
    for id_test, kategori, deskripsi, fungsi in TESTS:
        try:
            aktual, harapan = fungsi()
            status = "PASS" if aktual == harapan else "FAIL"
            if status == "FAIL":
                print(f"      expected={harapan!r} actual={aktual!r}")
        except Exception as galat:  # test tetap berjalan walau ada exception
            status = f"ERROR {type(galat).__name__}"
        if status != "PASS":
            gagal += 1
        print(f"{id_test:<6}{kategori:<10}{deskripsi:<42}{status}")
    print("-" * 66)
    print(f"Total: {len(TESTS)} test | PASS: {len(TESTS) - gagal} | FAIL: {gagal}")
    return gagal

if __name__ == "__main__":
    sys.exit(1 if jalankan() else 0)