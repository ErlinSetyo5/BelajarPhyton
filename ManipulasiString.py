'''
Operasi dan Manipulasi String dalam Python
'''

# 1. Menyambung string (concatenate)
nama_depan = "Choi"
nama_belakang = "Soojin"

# Penggabungan string
nama_lengkap = nama_depan +" "+ nama_belakang # Penggunaan kutip dan spasi ditengah berguna untuk memberikan spasi antar string (" ")
print(nama_lengkap)

# 2. Menghitung panjang string
panjang_str = len(nama_lengkap)
print("Panjang karakter dalam nama lengkap adalah :",panjang_str)

# 3. Operator untuk string

# Mengecek apakah ada komponen char atau string di dalam string
huruf = "S"
status = huruf in nama_lengkap # penggunaan in untu k mencari char atau string yg ada di dalam string
print(huruf + "ada di " + nama_lengkap +" = "+ str(status))

huruf = "S"
status = huruf not in nama_lengkap # penggunaan not in untuk mencari char atau string yg tidak ada di dalam string
print(huruf + " tidak ada di " + nama_lengkap +" = "+ str(status))

'''
Note : Pencarian karakter harus sesuai atau spesifik dengan string yg di cari
contoh : huruf besar dan kecil berpengaruh dalam pencarian
'''

# Mengulang string
print("wk"*15)
print(15*"wk")

# Indexing
print("index ke-0 : " + nama_lengkap[0]) # akan memberikan info char pertama dari nama lengkap Ilham Depok adalah I
print("index ke-(-1) : " + nama_lengkap[-1]) # akan memberikan info char pertama dari belakang nama lengkap Ilham Depok adalah K
print("index ke-0 sampai 4 : " + nama_lengkap[0:5]) # akan memberikan info range char dari urutan 0 sampai 5 dari nama lengkap Ilham Depok adalah Ilham