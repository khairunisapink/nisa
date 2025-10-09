# Program Kalkulator Sederhana Menggunakan Percabangan

print("=== KALKULATOR SEDERHANA ===")
print("Pilih operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

# Meminta input dari pengguna
pilihan = input("Masukkan pilihan (1/2/3/4): ")

# Meminta dua angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Menggunakan percabangan untuk menentukan operasi
if pilihan == '1':
    hasil = angka1 + angka2
    print(f"Hasil dari {angka1} + {angka2} = {hasil}")
elif pilihan == '2':
    hasil = angka1 - angka2
    print(f"Hasil dari {angka1} - {angka2} = {hasil}")
elif pilihan == '3':
    hasil = angka1 * angka2
    print(f"Hasil dari {angka1} * {angka2} = {hasil}")
elif pilihan == '4':
    if angka2 != 0:  # Mengecek agar tidak membagi dengan nol
        hasil = angka1 / angka2
        print(f"Hasil dari {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")
else:
    print("Pilihan tidak valid! Silakan coba lagi.")