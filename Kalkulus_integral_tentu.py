from scipy.integrate import quad
import math

def hitung_integral_tentu_interaktif():
    """
    Menghitung integral tentu dari suatu fungsi secara numerik,
    dengan input fungsi dan batas dari pengguna.
    """
    print("Selamat datang di Kalkulator Integral Tentu Numerik!")
    print("Anda akan diminta untuk mendefinisikan fungsi f(x) dan batas integral.")
    print("Contoh fungsi: 'x**2', 'math.sin(x)', 'math.exp(-x**2)'")
    print("Pastikan untuk menggunakan 'x' sebagai variabel dan 'math.' untuk fungsi matematika.")

    while True:
        try:
            # Mengambil input fungsi dari pengguna
            fungsi_str = input("\nMasukkan fungsi f(x) (contoh: x**2, math.sin(x)): ")
            # Mengubah string menjadi fungsi lambda yang bisa dievaluasi
            # Menggunakan eval() harus hati-hati karena potensi keamanan,
            # tapi untuk kasus kalkulator personal ini, cukup.
            fungsi_eval = eval(f"lambda x: {fungsi_str}")

            # Mengambil input batas bawah
            batas_bawah = float(input("Masukkan batas bawah integral (a): "))

            # Mengambil input batas atas
            batas_atas = float(input("Masukkan batas atas integral (b): "))

            # Memanggil fungsi quad dari SciPy
            nilai_integral, estimasi_error = quad(fungsi_eval, batas_bawah, batas_atas)

            print(f"\n--- Hasil Integral ---")
            print(f"Fungsi: f(x) = {fungsi_str}")
            print(f"Batas: dari {batas_bawah} sampai {batas_atas}")
            print(f"Nilai Integral: {nilai_integral}")
            print(f"Estimasi Error: {estimasi_error}")
            
            lagi = input("\nHitung integral lagi? (ya/tidak): ").lower()
            if lagi != 'ya':
                break

        except ValueError:
            print("Input tidak valid. Pastikan Anda memasukkan angka untuk batas dan fungsi yang benar.")
        except NameError as e:
            print(f"Kesalahan dalam fungsi: {e}. Pastikan Anda menggunakan 'x' sebagai variabel dan 'math.' untuk fungsi seperti sin, cos, exp.")
        except Exception as e:
            print(f"Terjadi kesalahan yang tidak terduga: {e}. Coba lagi.")

if __name__ == "__main__":
    hitung_integral_tentu_interaktif()