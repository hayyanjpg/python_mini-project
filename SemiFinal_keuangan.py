def format_rupiah(angka):
    """
    Mengubah angka menjadi format Rupiah.
    """
    return f"Rp{angka:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")

def hitung_keuangan_harian_mingguan():
    """
    Menghitung pemasukan dan pengeluaran harian untuk ringkasan mingguan.
    """
    hari_dalam_seminggu = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    total_pemasukan_mingguan = 0
    total_pengeluaran_mingguan = 0
    catatan_transaksi = []

    print("\n--- Perhitungan Keuangan Harian (Mingguan) ---")
    print("Masukkan pemasukan dan pengeluaran Anda setiap hari.")
    print("Masukkan 0 jika tidak ada transaksi.")
    print("-" * 40)

    for hari in hari_dalam_seminggu:
        print(f"\nHari: {hari}")
        try:
            pemasukan_harian = float(input(f"  Pemasukan untuk {hari} (Rp): "))
            if pemasukan_harian < 0:
                print("  Pemasukan tidak boleh negatif. Mengatur ke 0.")
                pemasukan_harian = 0

            pengeluaran_harian = float(input(f"  Pengeluaran untuk {hari} (Rp): "))
            if pengeluaran_harian < 0:
                print("  Pengeluaran tidak boleh negatif. Mengatur ke 0.")
                pengeluaran_harian = 0

            total_pemasukan_mingguan += pemasukan_harian
            total_pengeluaran_mingguan += pengeluaran_harian

            catatan_transaksi.append({
                "hari": hari,
                "pemasukan": pemasukan_harian,
                "pengeluaran": pengeluaran_harian
            })
        except ValueError:
            print("  Input tidak valid. Harap masukkan angka. Transaksi hari ini diatur ke 0.")
            catatan_transaksi.append({"hari": hari, "pemasukan": 0, "pengeluaran": 0})

    print("\n" + "=" * 40)
    print("RINGKASAN KEUANGAN MINGGUAN")
    print("=" * 40)

    for catatan in catatan_transaksi:
        saldo_harian = catatan["pemasukan"] - catatan["pengeluaran"]
        print(f"[{catatan['hari']}] Pemasukan: {format_rupiah(catatan['pemasukan'])} | "
              f"Pengeluaran: {format_rupiah(catatan['pengeluaran'])} | "
              f"Saldo Harian: {format_rupiah(saldo_harian)}")

    print("-" * 40)
    print(f"Total Pemasukan Mingguan : {format_rupiah(total_pemasukan_mingguan)}")
    print(f"Total Pengeluaran Mingguan: {format_rupiah(total_pengeluaran_mingguan)}")
    print("-" * 40)

    saldo_bersih = total_pemasukan_mingguan - total_pengeluaran_mingguan
    print(f"Saldo Bersih Mingguan    : {format_rupiah(saldo_bersih)}")
    print("=" * 40)

    if saldo_bersih >= 0:
        print("Selamat! Keuangan Anda dalam kondisi positif minggu ini.")
    else:
        print("Perhatian! Pengeluaran Anda melebihi pemasukan minggu ini.")
        print("Pertimbangkan untuk meninjau pengeluaran Anda.")

def hitung_keuangan_bulanan():
    """
    Menghitung pemasukan dan pengeluaran bulanan berdasarkan input mingguan.
    """
    jumlah_minggu = 4
    total_pemasukan_bulanan = 0
    total_pengeluaran_bulanan = 0
    catatan_transaksi_mingguan = []

    print("\n--- Perhitungan Keuangan Bulanan ---")
    print("Masukkan total pemasukan dan pengeluaran Anda untuk setiap minggu.")
    print("Masukkan 0 jika tidak ada transaksi.")
    print("-" * 40)

    for i in range(1, jumlah_minggu + 1):
        print(f"\nMinggu ke-{i}:")
        try:
            pemasukan_mingguan = float(input(f"  Total Pemasukan Minggu {i} (Rp): "))
            if pemasukan_mingguan < 0:
                print("  Pemasukan tidak boleh negatif. Mengatur ke 0.")
                pemasukan_mingguan = 0

            pengeluaran_mingguan = float(input(f"  Total Pengeluaran Minggu {i} (Rp): "))
            if pengeluaran_mingguan < 0:
                print("  Pengeluaran tidak boleh negatif. Mengatur ke 0.")
                pengeluaran_mingguan = 0

            total_pemasukan_bulanan += pemasukan_mingguan
            total_pengeluaran_bulanan += pengeluaran_mingguan

            catatan_transaksi_mingguan.append({
                "minggu": i,
                "pemasukan": pemasukan_mingguan,
                "pengeluaran": pengeluaran_mingguan
            })
        except ValueError:
            print("  Input tidak valid. Harap masukkan angka. Transaksi minggu ini diatur ke 0.")
            catatan_transaksi_mingguan.append({"minggu": i, "pemasukan": 0, "pengeluaran": 0})

    print("\n" + "=" * 50)
    print("RINGKASAN KEUANGAN BULANAN")
    print("=" * 50)

    for catatan in catatan_transaksi_mingguan:
        saldo_mingguan = catatan["pemasukan"] - catatan["pengeluaran"]
        print(f"[Minggu {catatan['minggu']}] Pemasukan: {format_rupiah(catatan['pemasukan'])} | "
              f"Pengeluaran: {format_rupiah(catatan['pengeluaran'])} | "
              f"Saldo Minggu: {format_rupiah(saldo_mingguan)}")

    print("-" * 50)
    print(f"Total Pemasukan Bulanan : {format_rupiah(total_pemasukan_bulanan)}")
    print(f"Total Pengeluaran Bulanan: {format_rupiah(total_pengeluaran_bulanan)}")
    print("-" * 50)

    saldo_bersih_bulanan = total_pemasukan_bulanan - total_pengeluaran_bulanan
    print(f"Saldo Bersih Bulanan    : {format_rupiah(saldo_bersih_bulanan)}")
    print("=" * 50)

    if saldo_bersih_bulanan >= 0:
        print("Selamat! Keuangan Anda dalam kondisi positif bulan ini.")
    else:
        print("Perhatian! Pengeluaran Anda melebihi pemasukan bulan ini.")
        print("Pertimbangkan untuk meninjau pengeluaran Anda.")

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
    catatan_transaksi_bulanan = []

    print("\n--- Perhitungan Keuangan Tahunan ---")
    print("Masukkan total pemasukan dan pengeluaran Anda untuk setiap bulan.")
    print("Masukkan 0 jika tidak ada transaksi.")
    print("-" * 50)

    for i, bulan in enumerate(nama_bulan):
        print(f"\nBulan: {bulan}")
        try:
            pemasukan_bulanan = float(input(f"  Total Pemasukan Bulan {bulan} (Rp): "))
            if pemasukan_bulanan < 0:
                print("  Pemasukan tidak boleh negatif. Mengatur ke 0.")
                pemasukan_bulanan = 0

            pengeluaran_bulanan = float(input(f"  Total Pengeluaran Bulan {bulan} (Rp): "))
            if pengeluaran_bulanan < 0:
                print("  Pengeluaran tidak boleh negatif. Mengatur ke 0.")
                pengeluaran_bulanan = 0

            total_pemasukan_tahunan += pemasukan_bulanan
            total_pengeluaran_tahunan += pengeluaran_bulanan

            catatan_transaksi_bulanan.append({
                "bulan": bulan,
                "pemasukan": pemasukan_bulanan,
                "pengeluaran": pengeluaran_bulanan
            })
        except ValueError:
            print("  Input tidak valid. Harap masukkan angka. Transaksi bulan ini diatur ke 0.")
            catatan_transaksi_bulanan.append({"bulan": bulan, "pemasukan": 0, "pengeluaran": 0})

    print("\n" + "=" * 60)
    print("RINGKASAN KEUANGAN TAHUNAN")
    print("=" * 60)

    for catatan in catatan_transaksi_bulanan:
        saldo_bulanan = catatan["pemasukan"] - catatan["pengeluaran"]
        print(f"[{catatan['bulan']}] Pemasukan: {format_rupiah(catatan['pemasukan'])} | "
              f"Pengeluaran: {format_rupiah(catatan['pengeluaran'])} | "
              f"Saldo Bulan: {format_rupiah(saldo_bulanan)}")

    print("-" * 60)
    print(f"Total Pemasukan Tahunan : {format_rupiah(total_pemasukan_tahunan)}")
    print(f"Total Pengeluaran Tahunan: {format_rupiah(total_pengeluaran_tahunan)}")
    print("-" * 60)

    saldo_bersih_tahunan = total_pemasukan_tahunan - total_pengeluaran_tahunan
    print(f"Saldo Bersih Tahunan    : {format_rupiah(saldo_bersih_tahunan)}")
    print("=" * 60)

    if saldo_bersih_tahunan >= 0:
        print("Selamat! Keuangan Anda dalam kondisi positif tahun ini.")
    else:
        print("Perhatian! Pengeluaran Anda melebihi pemasukan tahun ini.")
        print("Pertimbangkan untuk meninjau pengeluaran Anda.")

def tampilkan_menu():
    """
    Menampilkan menu utama dan meminta pilihan pengguna.
    """
    while True:
        print("\n" + "#" * 30)
        print("APLIKASI KEUANGAN PRIBADI")
        print("#" * 30)
        print("Pilih rentang waktu perhitungan:")
        print("1. Mingguan (Input Harian)")
        print("2. Bulanan (Input Mingguan)")
        print("3. Tahunan (Input Bulanan)")
        print("4. Keluar")
        print("-" * 30)

        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

        if pilihan == '1':
            hitung_keuangan_harian_mingguan()
        elif pilihan == '2':
            hitung_keuangan_bulanan()
        elif pilihan == '3':
            hitung_keuangan_tahunan()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi keuangan pribadi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
        input("\nTekan Enter untuk kembali ke menu utama...") # Menunggu input sebelum kembali ke menu

# Memanggil fungsi menu utama untuk menjalankan aplikasi
if __name__ == "__main__":
    tampilkan_menu()1