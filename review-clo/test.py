# input dan casting
n = int(input())

# inisialisasi
jumlah = 1
w = 1

# perulangan
for i in range(1, n+1): 
    # jumlah += 1/(i*2)
    w *= 2
    print(w)

# output
print('{:.5f}'.format(jumlah))