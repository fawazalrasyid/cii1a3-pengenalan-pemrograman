# Fungsi baca data
def baca_data():
    f = open("data.txt", "r")

    # inisialisasi dictionary
    dict_kalimat = {}

    # inisialisasi baris
    i = 1

    for baris in f:

        kalimat = baris.lower()

        kalimat = kalimat.replace(",", "").replace(".", "")

        # memasukan data kalimat ke dictionary
        dict_kalimat[i] = kalimat.split()
        
        i += 1

    f.close()
    return dict_kalimat


def jumlah_num(data):

    # inisialisasi list
    list_jumlah = []

    for e in data.values():

        numerik = [int(s) for s in e if s.isdigit()]

        # memasukan data hasil penjumlahan ke dalam list
        list_jumlah.append(sum(numerik))

    return sum(list_jumlah)


def frekuensi_tinggi(data):

    # inisialisasi list
    list_kata = []

    for e in data.values():

        for word in e:

            # memasukan setiap kata kedalam list
            list_kata.append(word)

    # mencari kata yang paling sering muncul
    kata = max(set(list_kata), key = list_kata.count)

    return kata


def kata_berawalan(data):

    # inisialisasi list
    list_kata = []

    for e in data.values():

        for word in e:

            if word[0] in 'mantp':
                # memasukkan kata jika kata tersebut berawalan [m, a, n, t, p]
                list_kata.append(word)

    # mengubah tipe data list ke dictionary untuk menghapus kata yang duplikat
    # kemudian di ubah kembali ke tipe data list
    list_kata = list(dict.fromkeys(list_kata))

    return list_kata


def main():
    data = baca_data()
    print("Data :", data)

    jumlah = jumlah_num(data)
    print("\nPenjumlahan karakter numerik : ", jumlah)

    frekuensi = frekuensi_tinggi(data)
    print("\nKata yang paling banyak muncul : ", frekuensi)

    kata = kata_berawalan(data)
    print("\nKata yang berawalan [m, a, n, t, p] : ", ", ".join(kata))

main()
