def hitung_keuangan_bulanan():
    """
    Menghitung pemasukan dan pengeluaran bulanan berdasarkan input mingguan.
    """
    jumlah_minggu = 4 # Asumsi 4 minggu dalam sebulan untuk kesederhanaan
    total_pemasukan_bulanan = 0
    total_pengeluaran_bulanan = 0
    catatan_transaksi_mingguan = [] # Untuk menyimpan detail transaksi per minggu

    print("--- Aplikasi Keuangan Pribadi Bulanan ---")
    print("Masukkan total pemasukan dan pengeluaran Anda untuk setiap minggu.")
    print("Masukkan 0 jika tidak ada transaksi untuk kategori tertentu.")
    print("-" * 40)

    for i in range(1, jumlah_minggu + 1): # Loop untuk Minggu 1, 2, 3, 4
        print(f"\nMinggu ke-{i}:")
        try:
            # Meminta pemasukan mingguan
            pemasukan_mingguan = float(input(f"  Total Pemasukan Minggu {i} (Rp): "))
            if pemasukan_mingguan < 0:
                print("  Pemasukan tidak boleh negatif. Mengatur ke 0.")
                pemasukan_mingguan = 0

            # Meminta pengeluaran mingguan
            pengeluaran_mingguan = float(input(f"  Total Pengeluaran Minggu {i} (Rp): "))
            if pengeluaran_mingguan < 0:
                print("  Pengeluaran tidak boleh negatif. Mengatur ke 0.")
                pengeluaran_mingguan = 0

            # Menambahkan ke total bulanan
            total_pemasukan_bulanan += pemasukan_mingguan
            total_pengeluaran_bulanan += pengeluaran_mingguan

            # Menyimpan detail transaksi mingguan
            catatan_transaksi_mingguan.append({
                "minggu": i,
                "pemasukan": pemasukan_mingguan,
                "pengeluaran": pengeluaran_mingguan
            })

        except ValueError:
            print("  Input tidak valid. Harap masukkan angka. Transaksi minggu ini diatur ke 0.")
            catatan_transaksi_mingguan.append({
                "minggu": i,
                "pemasukan": 0,
                "pengeluaran": 0
            })

    # --- Ringkasan Keuangan Bulanan ---
    print("\n" + "=" * 50)
    print("RINGKASAN KEUANGAN BULANAN")
    print("=" * 50)

    for catatan in catatan_transaksi_mingguan:
        saldo_mingguan = catatan["pemasukan"] - catatan["pengeluaran"]
        print(f"[Minggu {catatan['minggu']}] Pemasukan: Rp{catatan['pemasukan']:,.2f} | "
              f"Pengeluaran: Rp{catatan['pengeluaran']:,.2f} | "
              f"Saldo Minggu: Rp{saldo_mingguan:,.2f}")

    print("-" * 50)
    print(f"Total Pemasukan Bulanan : Rp{total_pemasukan_bulanan:,.2f}")
    print(f"Total Pengeluaran Bulanan: Rp{total_pengeluaran_bulanan:,.2f}")
    print("-" * 50)

    saldo_bersih_bulanan = total_pemasukan_bulanan - total_pengeluaran_bulanan
    print(f"Saldo Bersih Bulanan    : Rp{saldo_bersih_bulanan:,.2f}")
    print("=" * 50)

    if saldo_bersih_bulanan >= 0:
        print("Selamat! Keuangan Anda dalam kondisi positif bulan ini.")
    else:
        print("Perhatian! Pengeluaran Anda melebihi pemasukan bulan ini.")
        print("Pertimbangkan untuk meninjau pengeluaran Anda.")

# Memanggil fungsi untuk menjalankan aplikasi
if __name__ == "__main__":
    hitung_keuangan_bulanan()