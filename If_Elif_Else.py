'''
Penggunaan If, Elif & Else Dalam Bahasa Python
'''

# Penggunaan IF
nilai = 60

if (nilai >= 70):
    print("Selemat Anda Lulus Matakuliah Statistik")

if (nilai <=70):
    print("Anda Tidak Lulus Matakuliah Statistik")

'''
Pengambilan keputusan (kondisi if) digunakan untuk mengantisipasi kondisi yang
terjadi saat jalanya program dan menentukan tindakan apa yang akan diambil
sesuai dengan kondisi.
Kondisi IF digunakan untuk mengeksekusi kode jika kondisi bernilai benar (True)
Jika kondisi Bernilai salah (False) maka statment/kondisi IF tidak akan dieksekusi
'''


    
print(50*"=") # Ini hanya pembatas



# Penggunaan  IF,Else
nilai = 60

if (nilai >= 70):
    print("Selamat Anda Lulus Matakuliah Statistik")
else:
    print("Anda Tidak Lulus Matakuliah Statistik")

'''
Pengambilan keputusan (kondisi if else) tidak hanya digunakan untuk menentukan
tindakan apa yang akan diambil sesuai dengan kondisi, tetapi juga digunakan
untuk menentukan tindakan apa yang akan diambil/dijalankan jika kondisi tidak
sesuai.
Kondisi if else adalah kondisi dimana jika pernyataan benar (True) maka kode
dalam if akan dieksekusi, tetapi jika bernilai salah (False) maka akan
mengeksekusi kode di dalam else.
'''



print(50*"=") # Ini hanya pembatas



# Penggunaan IF, ELIF & ELSE
nilai = 60
if(nilai >= 90):
    print("Kamu Mendapatkan Nilai A")
elif(nilai >= 80):
    print("Kamu Mendapatkan Nilai B+")
elif (nilai >= 70):
    print("Kamu Mendapatkan Nilai B")
elif(nilai >= 65):
    print("Kamu Mendapatkan Nilai C+")
elif(nilai >= 60):
    print("Kamu Mendapatkan Nilai C")
elif (nilai >= 50):
    print("Kamu Mendapatkan Nilai D")
else:
    print("Kamu mendapatkan Nilai E")
    
'''
Pengambilan keputusan (kondisi if elif) merupakan lanjutan/percabangan logika
dari “kondisi if”. Dengan elif kita bisa membuat kode program yang akan
menyeleksi beberapa kemungkinan yang bisa terjadi. Hampir sama dengan kondisi
“else”, bedanya kondisi “elif” bisa banyak dan tidak hanya satu.
'''