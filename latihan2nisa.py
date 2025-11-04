# Class Induk
class Kendaraan:
    def __init__(self, merk, kecepatan):
        self.merk = merk
        self.kecepatan = kecepatan

# Subclass Mobil
class Mobil(Kendaraan):
    def info(self):
        print(f"Mobil {self.merk} melaju {self.kecepatan} km/jam.")

# Subclass Motor
class Motor(Kendaraan):
    def info(self):
        print(f"Motor {self.merk} melaju {self.kecepatan} km/jam.")


# Membuat objek dari subclass
m1 = Mobil("Toyota", 120)
mo1 = Motor("Honda", 80)

# Memanggil method info()
m1.info()
mo1.info()