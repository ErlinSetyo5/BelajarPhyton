'''
Membuat Program Konversi Suhu Sederhana dengan menggunakan Aritmatika Python
'''

print("\nPROGRAM KONVERSI SUHU\n")

celcius = float(input("Masukan suhu dalam celcius :"))
print("Suhu adalah",celcius,"celcius")

# Reamur
reamur = (4/5) * celcius #Operasi dalam kurung akan dieksekusi lebih awal dalam Operasi Aritmatika di Python
print("Suhu dalam Reamur adalah",reamur,"Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32 #Operasi dalam kurung akan dieksekusi lebih awal dalam Operasi Aritmatika di Python
print("Suhu dalam Fahrenheit adalah",fahrenheit,"Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah",kelvin,"kelvin") 