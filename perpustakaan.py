class Buku:
    def __init__(self, judul):
        self.judul = judul
        self.peminjam = None
        self.tersedia = True

    def pinjam(self, nama_peminjam):
        if self.tersedia:
            self.peminjam = nama_peminjam
            self.tersedia = False
            print(f"Buku '{self.judul}' berhasil dipinjam oleh {nama_peminjam}.")
        else:
            print(f"Buku '{self.judul}' sedang dipinjam.")

    def kembalikan(self):
        if not self.tersedia:
            print(f"Buku '{self.judul}' dikembalikan oleh {self.peminjam}.")
            self.peminjam = None
            self.tersedia = True
        else:
            print(f"Buku '{self.judul}' sudah tersedia.")

    def info_buku(self):
        print("\n=== INFORMASI BUKU ===")
        print(f"Judul     : {self.judul}")
        print(f"Peminjam  : {self.peminjam or '-'}")
        print(f"Tersedia  : {self.tersedia}")


# Pengujian objek
buku1 = Buku("Naruto: Shippūden")

buku1.info_buku()
buku1.pinjam("Patrio")
buku1.info_buku()
buku1.kembalikan()
buku1.info_buku()
