# Program Data Nilai Mahasiswa Menggunakan Method Class
**Flowchart**

![Screenshot_23](https://github.com/user-attachments/assets/373fca6d-30f5-456a-bb9e-3efcaa8aae22)

**Diagram Kelas**

![Screenshot_24](https://github.com/user-attachments/assets/a3ccc43d-4ecd-47b0-8ea6-ecedb3cc0950)

**Kode Python**

![Screenshot_18](https://github.com/user-attachments/assets/3fe858fb-f17f-47ba-a6ce-a6d6ef28f626)
![Screenshot_19](https://github.com/user-attachments/assets/20456f24-d932-44ff-bf88-f6e031f71b93)
![Screenshot_20](https://github.com/user-attachments/assets/dd4ce545-e3ab-44e3-9d49-b14047c02e42)

**Input dan Output**

![Screenshot_21](https://github.com/user-attachments/assets/fbd714c9-380b-49a9-b781-9eab38662725)
![Screenshot_22](https://github.com/user-attachments/assets/3510eeba-f1c4-491e-bde5-f6f952ac9348)

# Penjelasan

**Konstruktor __init__**

o	Fungsi ini adalah konstruktor, dipanggil otomatis saat objek dibuat.

o	self.mahasiswa adalah sebuah list kosong yang akan digunakan untuk menyimpan data mahasiswa. Data akan disimpan dalam format dictionary.

	 
**Method tambah**
 
1.	Input Data:

o	input() digunakan untuk mengambil nama, NIM, dan nilai mahasiswa dari pengguna.

o	Nilai diubah ke tipe float agar dapat digunakan untuk operasi numerik (seperti perhitungan jika diperlukan).

3.	Menambahkan ke List:

o	Data yang dimasukkan pengguna disimpan dalam sebuah dictionary dengan kunci nama, nim, dan nilai.

o	Data ini ditambahkan ke list self.mahasiswa menggunakan fungsi append().

4.	Konfirmasi:

o	Pesan ditampilkan untuk memberi tahu bahwa data berhasil ditambahkan.

**Method tampilkan**

1.  Memeriksa Data:

o	if not self.mahasiswa: Mengecek apakah list mahasiswa kosong. Jika kosong, menampilkan pesan "Tidak ada data mahasiswa."

2. Menampilkan Data:

o	Jika ada data, menggunakan perulangan for untuk mengakses setiap item dalam list self.mahasiswa.

o	Setiap item (dictionary) memiliki kunci nama, nim, dan nilai, yang ditampilkan dengan format yang rapi.

**Method hapus** 

1.	Inisialisasi:

o	Variabel found diatur menjadi False untuk melacak apakah data ditemukan.

2.	Pencarian Data:

o	Menggunakan perulangan for untuk mencari nama mahasiswa dalam list self.mahasiswa.

o	Fungsi lower() digunakan untuk mengabaikan perbedaan huruf besar/kecil saat membandingkan nama.

3.	Menghapus Data:

o	Jika data ditemukan, fungsi remove() digunakan untuk menghapus item dari list.

o	found diubah menjadi True, dan pesan konfirmasi ditampilkan.

4.	Jika Tidak Ditemukan:
o	Jika perulangan selesai tanpa menemukan data (variabel found tetap False), pesan bahwa data tidak ditemukan akan ditampilkan.

	 

**Method ubah**

1.	Inisialisasi:

o	Sama seperti hapus, menggunakan variabel found untuk melacak apakah data ditemukan.

2.	Pencarian Data:

o	Perulangan for mencari data mahasiswa dengan nama yang sesuai.

o	Jika ditemukan, data mahasiswa tersebut ditampilkan.

3.	Mengubah Nilai:

o	Meminta pengguna memasukkan nilai baru menggunakan input() dan mengubahnya ke tipe float.

o	Data mhs['nilai'] diperbarui dengan nilai baru.

4.	Konfirmasi atau Error:

o	Jika data ditemukan, pesan konfirmasi ditampilkan.

o	Jika tidak ditemukan (found tetap False), pesan error ditampilkan.

# Fungsi Utama (main())

**1.	Objek daftar_nilai:**

o	Membuat objek dari class DaftarNilaiMahasiswa.

**2.	Menu Utama:**

o	Menampilkan opsi menu:


1.	Tambah data

2.	Tampilkan data

3.	Hapus data

4.	Ubah data

5.	Keluar dari program

o	Menggunakan input() untuk meminta pengguna memilih opsi.

**3.	Logika Pilihan:**

o	Setiap opsi (1-4) memanggil method dari class sesuai fungsi yang diminta.

o	Pilihan 5 mengakhiri program.

o	Jika input tidak valid, pesan error ditampilkan.
