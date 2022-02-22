def penjumlahan(dict_data):
    for k, v in dict_data.items():
        return dict_data.append(sum(v[1:]))

def baca_data():
    f = open('input.txt', 'r')

    # inisialisasi
    dict_data = dict()

    # membaca isi file menggunkan perulangan
    for baris in f:
        b = baris.split()
        list_value = list()
        list_value.append(b[1])
        list_value.extend(list(map(int, b[2:])))
        dict_data[b[0]] = list_value

    f.close()
    return dict_data

def cetak_data(dict_data):
    for v in dict_data.values():
        print(v[-1])

def main():
    data = baca_data()
    print(data)
    data = penjumlahan(data)
    cetak_data(data)

if __name__ == '__main__':
    main()