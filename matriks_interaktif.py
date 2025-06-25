import numpy as np

def get_matrix_from_user(matrix_name):
    """
    Meminta pengguna untuk memasukkan dimensi dan elemen matriks.
    """
    while True:
        try:
            rows = int(input(f"Masukkan jumlah baris untuk Matriks {matrix_name}: "))
            cols = int(input(f"Masukkan jumlah kolom untuk Matriks {matrix_name}: "))
            if rows <= 0 or cols <= 0:
                print("Jumlah baris dan kolom harus lebih dari 0. Coba lagi.")
                continue

            print(f"Masukkan elemen-elemen untuk Matriks {matrix_name} ({rows}x{cols}):")
            matrix_elements = []
            for i in range(rows):
                while True:
                    row_str = input(f"Baris {i+1} (pisahkan dengan spasi, contoh: 1 2 3): ")
                    try:
                        row_elements = list(map(float, row_str.split()))
                        if len(row_elements) != cols:
                            print(f"Jumlah elemen tidak sesuai dengan kolom ({cols}). Coba lagi.")
                        else:
                            matrix_elements.append(row_elements)
                            break
                    except ValueError:
                        print("Input tidak valid. Pastikan semua elemen adalah angka dan dipisahkan spasi.")
            return np.array(matrix_elements)
        except ValueError:
            print("Input tidak valid. Harap masukkan angka untuk dimensi.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}. Coba lagi.")

def main_operasi_matriks_interaktif():
    """
    Fungsi utama untuk kalkulator operasi matriks interaktif.
    """
    print("--- Kalkulator Operasi Matriks Interaktif ---")

    while True:
        print("\nPilih operasi:")
        print("1. Penjumlahan Matriks (A + B)")
        print("2. Perkalian Matriks (A @ B)")
        print("3. Transpose Matriks (A.T)")
        print("4. Invers Matriks (A_inv)")
        print("5. Selesai")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            print("\n--- Penjumlahan Matriks ---")
            mat_A = get_matrix_from_user("A")
            mat_B = get_matrix_from_user("B")
            
            if mat_A.shape != mat_B.shape:
                print("Error: Dimensi matriks harus sama untuk penjumlahan.")
            else:
                hasil = mat_A + mat_B
                print("\nHasil Penjumlahan (A + B):\n", hasil)

        elif pilihan == '2':
            print("\n--- Perkalian Matriks ---")
            mat_A = get_matrix_from_user("A")
            mat_B = get_matrix_from_user("B")
            
            # Cek kompatibilitas dimensi untuk perkalian
            if mat_A.shape[1] != mat_B.shape[0]:
                print("Error: Jumlah kolom Matriks A harus sama dengan jumlah baris Matriks B untuk perkalian.")
            else:
                hasil = mat_A @ mat_B # Atau np.dot(mat_A, mat_B)
                print("\nHasil Perkalian (A @ B):\n", hasil)

        elif pilihan == '3':
            print("\n--- Transpose Matriks ---")
            mat_A = get_matrix_from_user("A")
            hasil = mat_A.T
            print("\nHasil Transpose Matriks A:\n", hasil)

        elif pilihan == '4':
            print("\n--- Invers Matriks ---")
            mat_A = get_matrix_from_user("A")
            
            if mat_A.shape[0] != mat_A.shape[1]:
                print("Error: Matriks harus persegi (jumlah baris == jumlah kolom) untuk diinvers.")
            else:
                try:
                    hasil = np.linalg.inv(mat_A)
                    print("\nHasil Invers Matriks A:\n", hasil)
                    # Verifikasi: A @ A_inv seharusnya mendekati matriks identitas
                    print("Verifikasi (A @ A_inv, harus mendekati matriks identitas):\n", mat_A @ hasil)
                except np.linalg.LinAlgError:
                    print("Error: Matriks tidak bisa diinvers (mungkin singular atau determinan nol).")
                except Exception as e:
                    print(f"Terjadi kesalahan: {e}")

        elif pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator matriks!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan fungsi utama
if __name__ == "__main__":
    main_operasi_matriks_interaktif()