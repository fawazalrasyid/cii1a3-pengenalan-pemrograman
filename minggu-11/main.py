def baca_data():
    # radius = float(input())
    # return radius
    
    f = open('input.txt', 'r')

    # isi_file = f.read()

    # membaca isi file menggunkan perulangan
    for baris in f:
        b = list(map(int, baris.split()))
        print(b)

    f.close()
    # return float(isi_file)

def hitung_luas_lingkaran(jari_jari):
    luas = 3.14 * jari_jari ** 2
    return luas

def hitung_luas_persegi_panjang (panjang, lebar):
    luas = panjang * lebar
    return luas

def main():
    j = baca_data()
    # luas_L= hitung_luas_lingkaran(j)
    # print(j)

if __name__ == '__main__':
    main()