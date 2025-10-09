# Program Kalkulator Sederhana
# Menggunakan konsep percabangan (if-elif-else) dan perulangan (while)

print("=== KALKULATOR SEDERHANA ===")

# Perulangan agar program bisa dijalankan berulang kali
while True:
    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    # Jika pengguna memilih keluar, hentikan program
    if pilihan == '5':
        print("Terima kasih telah menggunakan kalkulator!")
        break

    # Meminta dua angka dari pengguna
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    # Percabangan untuk menentukan operasi
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
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"Hasil dari {angka1} / {angka2} = {hasil}")
        else:
            print("Error: Tidak bisa membagi dengan nol!")
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

    # Tanya apakah ingin menghitung lagi
    ulang = input("\nApakah ingin menghitung lagi? (y/n): ")
    if ulang.lower() != 'y':
        print("Program selesai. Terima kasih!")
        break