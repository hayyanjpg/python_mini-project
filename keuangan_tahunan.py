def hitung_keuangan_tahunan():
    """
    Menghitung pemasukan dan pengeluaran tahunan berdasarkan input bulanan.
    """
    nama_bulan = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]
    total_pemasukan_tahunan = 0
    total_pengeluaran_tahunan = 0
    catatan_transaksi_bulanan = [] # Untuk menyimpan detail transaksi per bulan

    print("--- Aplikasi Keuangan Pribadi Tahunan ---")
    print("Masukkan total pemasukan dan pengeluaran Anda untuk setiap bulan.")
    print("Masukkan 0 jika tidak ada transaksi untuk kategori tertentu.")
    print("-" * 50)

    for i, bulan in enumerate(nama_bulan): # Loop untuk setiap bulan
        print(f"\nBulan: {bulan}")
        try:
            # Meminta pemasukan bulanan
            pemasukan_bulanan = float(input(f"  Total Pemasukan Bulan {bulan} (Rp): "))
            if pemasukan_bulanan < 0:
                print("  Pemasukan tidak boleh negatif. Mengatur ke 0.")
                pemasukan_bulanan = 0

            # Meminta pengeluaran bulanan
            pengeluaran_bulanan = float(input(f"  Total Pengeluaran Bulan {bulan} (Rp): "))
            if pengeluaran_bulanan < 0:
                print("  Pengeluaran tidak boleh negatif. Mengatur ke 0.")
                pengeluaran_bulanan = 0

            # Menambahkan ke total tahunan
            total_pemasukan_tahunan += pemasukan_bulanan
            total_pengeluaran_tahunan += pengeluaran_bulanan

            # Menyimpan detail transaksi bulanan
            catatan_transaksi_bulanan.append({
                "bulan": bulan,
                "pemasukan": pemasukan_bulanan,
                "pengeluaran": pengeluaran_bulanan
            })

        except ValueError:
            print("  Input tidak valid. Harap masukkan angka. Transaksi bulan ini diatur ke 0.")
            catatan_transaksi_bulanan.append({
                "bulan": bulan,
                "pemasukan": 0,
                "pengeluaran": 0
            })

    # --- Ringkasan Keuangan Tahunan ---
    print("\n" + "=" * 60)
    print("RINGKASAN KEUANGAN TAHUNAN")
    print("=" * 60)

    for catatan in catatan_transaksi_bulanan:
        saldo_bulanan = catatan["pemasukan"] - catatan["pengeluaran"]
        print(f"[{catatan['bulan']}] Pemasukan: Rp{catatan['pemasukan']:,.2f} | "
              f"Pengeluaran: Rp{catatan['pengeluaran']:,.2f} | "
              f"Saldo Bulan: Rp{saldo_bulanan:,.2f}")

    print("-" * 60)
    print(f"Total Pemasukan Tahunan : Rp{total_pemasukan_tahunan:,.2f}")
    print(f"Total Pengeluaran Tahunan: Rp{total_pengeluaran_tahunan:,.2f}")
    print("-" * 60)

    saldo_bersih_tahunan = total_pemasukan_tahunan - total_pengeluaran_tahunan
    print(f"Saldo Bersih Tahunan    : Rp{saldo_bersih_tahunan:,.2f}")
    print("=" * 60)

    if saldo_bersih_tahunan >= 0:
        print("Selamat! Keuangan Anda dalam kondisi positif tahun ini.")
    else:
        print("Perhatian! Pengeluaran Anda melebihi pemasukan tahun ini.")
        print("Pertimbangkan untuk meninjau pengeluaran Anda.")

# Memanggil fungsi untuk menjalankan aplikasi
if __name__ == "__main__":
    hitung_keuangan_tahunan()