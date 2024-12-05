class DaftarNilaiMahasiswa:
    def __init__(self):
        self.mahasiswa = []  # Menyimpan data mahasiswa dalam bentuk list

    def tambah(self):
        # Input data mahasiswa
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM mahasiswa: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))
        
        # Menambah data mahasiswa ke dalam list
        self.mahasiswa.append({"nama": nama, "nim": nim, "nilai": nilai})
        print("Data mahasiswa berhasil ditambahkan!\n")

    def tampilkan(self):
        # Menampilkan data mahasiswa
        if not self.mahasiswa:
            print("Tidak ada data mahasiswa.\n")
        else:
            print("Daftar Nilai Mahasiswa:")
            for mhs in self.mahasiswa:
                print(f"Nama: {mhs['nama']}, NIM: {mhs['nim']}, Nilai: {mhs['nilai']}")
            print()

    def hapus(self, nama):
        # Menghapus data mahasiswa berdasarkan nama
        found = False
        for mhs in self.mahasiswa:
            if mhs['nama'].lower() == nama.lower():
                self.mahasiswa.remove(mhs)
                found = True
                print(f"Data mahasiswa dengan nama {nama} berhasil dihapus!\n")
                break
        if not found:
            print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.\n")

    def ubah(self, nama):
        # Mengubah data mahasiswa berdasarkan nama
        found = False
        for mhs in self.mahasiswa:
            if mhs['nama'].lower() == nama.lower():
                print(f"Data mahasiswa ditemukan: Nama: {mhs['nama']}, NIM: {mhs['nim']}, Nilai: {mhs['nilai']}")
                # Input nilai baru
                new_nilai = float(input("Masukkan nilai baru: "))
                mhs['nilai'] = new_nilai
                found = True
                print(f"Data nilai mahasiswa {nama} berhasil diubah!\n")
                break
        if not found:
            print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.\n")


# Program utama
def main():
    daftar_nilai = DaftarNilaiMahasiswa()
    
    while True:
        print("Menu:")
        print("1. Tambah data mahasiswa")
        print("2. Tampilkan data mahasiswa")
        print("3. Hapus data mahasiswa")
        print("4. Ubah data mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            daftar_nilai.tambah()
        elif pilihan == '2':
            daftar_nilai.tampilkan()
        elif pilihan == '3':
            nama_hapus = input("Masukkan nama mahasiswa yang akan dihapus: ")
            daftar_nilai.hapus(nama_hapus)
        elif pilihan == '4':
            nama_ubah = input("Masukkan nama mahasiswa yang akan diubah: ")
            daftar_nilai.ubah(nama_ubah)
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu antara 1-5.")

if __name__ == "__main__":
    main()
