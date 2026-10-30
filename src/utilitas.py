"""Fungsi pendukung: konstanta, validasi nilai, dan format laporan."""

from analisis import tentukan_status

NILAI_MIN = 0
NILAI_MAX = 100
KKM_DEFAULT = 70


def validasi_nilai(nilai):
    """Mengembalikan True jika nilai berada pada rentang 0-100 (inklusif)."""
    return NILAI_MIN <= nilai <= NILAI_MAX


def format_laporan(data, statistik, tuntas, belum_tuntas, kkm, jumlah_ditolak):
    """Menyusun teks laporan rekap nilai (satu string)."""
    baris = [
        "=== LAPORAN REKAP NILAI ===",
        f"KKM           : {kkm:g}",
        f"Data valid    : {statistik['jumlah']}",
        f"Baris ditolak : {jumlah_ditolak}",
        f"Rata-rata     : {statistik['rata_rata']:.2f}",
        f"Minimum       : {statistik['minimum']:.2f} ({statistik['nama_min']})",
        f"Maksimum      : {statistik['maksimum']:.2f} ({statistik['nama_maks']})",
        f"Tuntas        : {tuntas}",
        f"Belum tuntas  : {belum_tuntas}",
        "",
        f"{'NIM':<8}{'Nama':<12}{'Nilai':>7}  Status",
    ]
    for nim, item in data.items():
        status = tentukan_status(item["nilai"], kkm)
        baris.append(f"{nim:<8}{item['nama']:<12}{item['nilai']:>7.2f}  {status}")
    return "\n".join(baris) + "\n"
