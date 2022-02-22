def baca_data():
    f = open("data03.txt", "r")
    # inisialisasi list
    bilangan = []

    for baris in f:
        b = int(baris)
        bilangan.append(b)

    f.close()
    return bilangan


def simpan_data(data):
    fo = open("output_data03.txt", "w")
    fo.write(str(data))
    fo.close()


def penjumlahan(list_data):
    jumlah = 0
    for e in list_data:
        jumlah += e
    return jumlah


def main():
    data = baca_data()
    print("input :", data)

    hasil_penjumlahan = penjumlahan(data)
    print("output :", hasil_penjumlahan)

    simpan_data(hasil_penjumlahan)


if __name__ == "__main__":
    main()
