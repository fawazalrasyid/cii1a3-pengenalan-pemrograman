def baca_data():

    f = open("data.txt", "r")

    # inisialisasi dictionary
    dict_toko = {}

    # perulangan untuk membaca data di setiap baris
    for row in f:

        barang = row.split()

        for i in range(1, len(barang)):

            harga_barang = int(barang[i].replace(".", ""))

            if dict_toko.get("toko" + str(i)) == None:
                dict_toko["toko" + str(i)] = {barang[0]: harga_barang}
            else:
                dict_toko["toko" + str(i)].update({barang[0]: harga_barang})

    f.close
    return dict_toko


def cari_termurah(data, barang):

    # inisialisasi dictionary untuk menyimpan data sementara
    temp_data = {}

    for k, v in data.items():

        for m, n in v.items():

            if m.lower() == barang.lower():
                temp_data.update({k: n})

    if temp_data != {}:
        termurah = min(temp_data.values())
        nama_toko = [k for k in temp_data if temp_data[k] == termurah]
    else:
        nama_toko = None

    return nama_toko


def report(data):

    Beras = []
    Minyak = []
    Gula = []
    Terigu = []
    Telur = []

    for e in data.values():

        Beras.append(e["Beras"])
        Minyak.append(e["Minyak"])
        Gula.append(e["Gula"])
        Terigu.append(e["Terigu"])
        Telur.append(e["Telur"])

    dict_barang = {
        "Beras": round(sum(Beras) / len(Beras)),
        "Minyak": round(sum(Minyak) / len(Minyak)),
        "Gula": round(sum(Gula) / len(Gula)),
        "Terigu": round(sum(Terigu) / len(Terigu)),
        "Telur": round(sum(Telur) / len(Telur)),
    }

    f = open("report.txt", "w")

    for k, v in dict_barang.items():
        row = k + " " + str(v)
        f.write(row + "\n")

    f.close


def main():
    # fungsi untuk membaca data dari file text
    data_barang = baca_data()
    # print(data_barang)

    # fungsi untuk mencari harga termurah dari barang yg dicari
    print("\n*********** Fungsi Termurah ***********\n")

    nama_barang = input("\nMasukkan nama barang : ")
    toko = cari_termurah(data_barang, nama_barang)

    if toko != None:
        print(
            "\nToko yang menjual",
            nama_barang,
            "dengan harga termurah adalah",
            ", ".join(toko),
        )
    else:
        print("\nbarang yang di cari tidak ditemukan")

    # fungsi report
    report(data_barang)


if __name__ == "__main__":
    main()
