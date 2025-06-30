def hitung_keuangan_mingguan():
    """
    Menghitung pemasukan dan pengeluaran mingguan untuk merangkum keuangan.
    """
    hari_dalam_seminggu = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    total_pemasukan_mingguan = 0
    total_pengeluaran_mingguan = 0
    catatan_transaksi = [] # Untuk menyimpan detail transaksi

    print("--- Aplikasi Keuangan Pribadi Mingguan ---")
    print("Masukkan pemasukan dan pengeluaran Anda setiap hari.")
    print("Masukkan 0 jika tidak ada transaksi untuk kategori tertentu.")
    print("-" * 40)

    for hari in hari_dalam_seminggu:
        print(f"\nHari: {hari}")
        try:
            # Meminta pemasukan harian
            pemasukan_harian = float(input(f"  Pemasukan untuk {hari} (Rp): "))
            if pemasukan_harian < 0:
                print("  Pemasukan tidak boleh negatif. Mengatur ke 0.")
                pemasukan_harian = 0

            # Meminta pengeluaran harian
            pengeluaran_harian = float(input(f"  Pengeluaran untuk {hari} (Rp): "))
            if pengeluaran_harian < 0:
                print("  Pengeluaran tidak boleh negatif. Mengatur ke 0.")
                pengeluaran_harian = 0

            # Menambahkan ke total mingguan
            total_pemasukan_mingguan += pemasukan_harian
            total_pengeluaran_mingguan += pengeluaran_harian

            # Menyimpan detail transaksi
            catatan_transaksi.append({
                "hari": hari,
                "pemasukan": pemasukan_harian,
                "pengeluaran": pengeluaran_harian
            })

        except ValueError:
            print("  Input tidak valid. Harap masukkan angka. Transaksi hari ini diatur ke 0.")
            catatan_transaksi.append({
                "hari": hari,
                "pemasukan": 0,
                "pengeluaran": 0
            })

    # --- Ringkasan Keuangan ---
    print("\n" + "=" * 40)
    print("RINGKASAN KEUANGAN MINGGUAN")
    print("=" * 40)

    for catatan in catatan_transaksi:
        saldo_harian = catatan["pemasukan"] - catatan["pengeluaran"]
        print(f"[{catatan['hari']}] Pemasukan: Rp{catatan['pemasukan']:,.2f} | "
              f"Pengeluaran: Rp{catatan['pengeluaran']:,.2f} | "
              f"Saldo Harian: Rp{saldo_harian:,.2f}")

    print("-" * 40)
    print(f"Total Pemasukan Mingguan : Rp{total_pemasukan_mingguan:,.2f}")
    print(f"Total Pengeluaran Mingguan: Rp{total_pengeluaran_mingguan:,.2f}")
    print("-" * 40)

    saldo_bersih = total_pemasukan_mingguan - total_pengeluaran_mingguan
    print(f"Saldo Bersih Mingguan    : Rp{saldo_bersih:,.2f}")
    print("=" * 40)

    if saldo_bersih >= 0:
        print("Selamat! Keuangan Anda dalam kondisi positif minggu ini.")
    else:
        print("Perhatian! Pengeluaran Anda melebihi pemasukan minggu ini.")
        print("Pertimbangkan untuk meninjau pengeluaran Anda.")

# Memanggil fungsi untuk menjalankan aplikasi
if __name__ == "__main__":
    hitung_keuangan_mingguan()