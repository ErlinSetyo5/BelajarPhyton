# a = 100, artinya a adalah variable dengain nilai 100

# Tipe Data Dalam Python 

# Tipe data angka bilangan bulat (integer)
data_integer = 100
print("Data :", data_integer)
print("Bertipe :", type(data_integer))

# Tipe data bilangan angka dalam koma (float)
data_float = 1.5
print("Data :", type(data_float))


# Tipe data dengan kumpulan karakter, biasanya di tandai dengan tanda "" (string)
data_string = "ayo belajar python"
print("Data :", data_string)
print("Bertipe :", type(data_string))

# Tipe data dengan biner true/false (boolean)
data_bool = True
print("Data :",data_bool)
print("Bertipe :",type(data_bool))

# Python juga dapat membuat type data dalam bahasa c
# import library untuk type data dalam bahasa c
from ctypes import c_double

data_c_double = c_double(10.5)
print("Data:", data_bool)
print("Bertipe :", type(data_bool))