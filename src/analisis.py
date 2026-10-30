"""Perhitungan statistik dan penentuan ketuntasan."""


def hitung_statistik(data):
    """Menghitung jumlah, rata-rata, minimum, dan maksimum dari data valid.

    data: dictionary {nim: {"nama": ..., "nilai": ...}}
    Melempar ValueError jika data kosong (pemanggil harus memeriksa lebih dulu).
    """
    if not data:
        raise ValueError("data kosong")

    nilai = [item["nilai"] for item in data.values()]
    nim_min = min(data, key=lambda k: data[k]["nilai"])
    nim_maks = max(data, key=lambda k: data[k]["nilai"])

    return {
        "jumlah": len(nilai),
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": data[nim_min]["nilai"],
        "nama_min": data[nim_min]["nama"],
        "maksimum": data[nim_maks]["nilai"],
        "nama_maks": data[nim_maks]["nama"],
    }


def tentukan_status(nilai, kkm):
    """Nilai yang sama dengan KKM dinyatakan tuntas."""
    if nilai >= kkm:
        return "Tuntas"
    return "Belum tuntas"


def hitung_ketuntasan(data, kkm):
    """Mengembalikan (jumlah_tuntas, jumlah_belum_tuntas)."""
    tuntas = sum(1 for item in data.values() if item["nilai"] >= kkm)
    return tuntas, len(data) - tuntas
