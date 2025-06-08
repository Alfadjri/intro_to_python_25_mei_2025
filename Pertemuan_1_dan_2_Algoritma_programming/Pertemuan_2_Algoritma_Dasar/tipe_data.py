#integer (int)
#ini bilangan bulat
# contoh 0123
x = 32767 #limit dari integer karakter 
print("Ini contoh tipe data Integer : {0}".format(x))

#float (bilangan desimal)
y = 3.14
print("Ini contoh tipe data float : {0}".format(y))

# kompleks
z = 2 + 3j
print("Ini contoh tipe data kompleks : {0}".format(z))


# tipe data squenc
a = [1,2,3] # list sifat tipe data nya value nya sebisa mungkin tipedatanya sama
print("Ini contoh tipe data list : {0}".format(a))
b = (4,5,6) # truplet sifat tipe data nya tidak bisa di ganti
print("Ini contoh tipe data trueplet : {0}".format(b))
c = range(0,5)
print("Ini contoh tipe data range : {0}".format(c))

# text
nama = "Alfadjri Dwi Fadhilah" #tipe data string
print("Ini contoh tipe data string atau text : {0}".format(nama))
#sejarahnya dia terdiri dari char(255)
karakter = 'A'
print("Ini contoh tipe data karkater : {0}".format(karakter))

# set
f = {1,2,3} # set tipe data yang tidak bisa di ubah"
print("Ini contoh tipe data set : {0}".format(f))
g = frozenset({4,5,6}) #frozenset
print("Ini contoh tipe data frozenset : {0}".format(g))


#Tipe data Kondisi
#booleal (bool)
#inisnya hanya dua True(1) atau False(0)
kondisi_badab = True


# tipe data binery
i = 0b1000001
print("Tipe data binary : {0}".format(i))
# desimal = int(i)
# print("Conversi binary to Desimal : {0}".format(desimal))
# char = chr(desimal)
# print("Conversi Desimal to char : {0}".format(char))
print("Singkat binary to char : {0}".format(chr(int(i))))
j = bytearray(a)
print("Isi binary dalam array variabel a : {0}".format(j))
z = memoryview(j)
print("lokasi array dalam memory (Ram) : {0}".format(z))
