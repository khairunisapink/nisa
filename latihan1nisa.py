# Deklarasi Class
class Siswa:
    # Atribut Class (sama untuk semua objek)
    sekolah = "SMK PGRI 35 Solokanjeruk"

    # Konstruktor untuk inisialisasi atribut instance
    def __init__(self, nama, nis, kelas):
        self.nama = nama
        self.nis = nis
        self.kelas = kelas

    # Method untuk menampilkan profil siswa
    def tampilkan_profil_siswa(self):
        print(f"Nama    : {self.nama}")
        print(f"NIS     : {self.nis}")
        print(f"Kelas   : {self.kelas}")
        print(f"Sekolah : {Siswa.sekolah}")
        print("-" * 40)


# Membuat 3 objek dari class Siswa
s1 = Siswa("khairunisa", "12345", "XI RPL 3")
s2 = Siswa("tisna ana abdulah", "12346", "XI RPL 1")
s3 = Siswa("Ntiss", "12347", "XI RPL 8")

# Memanggil method untuk menampilkan profil masing-masing siswa
s1.tampilkan_profil_siswa()
s2.tampilkan_profil_siswa()
s3.tampilkan_profil_siswa()