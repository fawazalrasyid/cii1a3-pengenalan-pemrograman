#input
list_str = input().split("/")

# inisialisasi
jumlah_O = 0
jumlah_X = 0

# perulangan
for i in range(len(list_str)):
    if list_str[i] == "O":
        jumlah_O += 1
    elif list_str[i] == "X":
        jumlah_X += 1

# cetak
print ('O: {}'.format(jumlah_O))
print('X: {}'.format(jumlah_X))