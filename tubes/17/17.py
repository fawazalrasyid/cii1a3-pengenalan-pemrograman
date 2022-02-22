# Fungsi baca data
def baca_data():
    f = open("17.txt", "r")

    list_barang = []

    for baris in f:
        data_barang = {}

        data = baris.split()

        if len(data) >= 10:
            barang = data[0] + " " + data[1]
            buat1 = data[2]
            jual1 = data[3]
            buat2 = data[4]
            jual2 = data[5]
            buat3 = data[6]
            jual3 = data[7]
            buat4 = data[8]
            jual4 = data[9]
        else:
            barang = data[0]
            buat1 = data[1]
            jual1 = data[2]
            buat2 = data[3]
            jual2 = data[4]
            buat3 = data[5]
            jual3 = data[6]
            buat4 = data[7]
            jual4 = data[8]

        data_barang[barang] = {
            "buat1": float(buat1),
            "jual1": float(jual1),
            "buat2": float(buat2),
            "jual2": float(jual2),
            "buat3": float(buat3),
            "jual3": float(jual3),
            "buat4": float(buat4),
            "jual4": float(jual4),
        }

        list_barang.append(data_barang)

    f.close()
    return list_barang


def peningkatan(data):

    for e in data:

        for m, n in e.items():

            temp_data = [n["buat1"], n["buat2"], n["buat3"], n["buat4"]]

            perkembangan = ""

            if temp_data[0] > temp_data[1] > temp_data[2] > temp_data[3]:
                perkembangan = "peningkatan"
            elif temp_data[0] == temp_data[1] == temp_data[2] == temp_data[3]:
                perkembangan = "stagnan"
            else:
                perkembangan = "fluktuatif"

            # update data dictionary
            e[m].update({"perkembangan": perkembangan})

    return data


def rata_rata(data):

    for e in data:

        for m, n in e.items():

            temp_data = [n["jual1"], n["jual2"], n["jual3"], n["jual4"]]

            rata_rata = sum(temp_data) / len(temp_data)

            # update data dictionary
            e[m].update({"rata_rata": rata_rata})

    return data


def write_data(data):
    f = open("report.txt", "w")

    for e in data:

        for k, v in e.items():
            row = k + " " + " ".join(str(x) for x in v.values())
            f.write(row + "\n")

    f.close


def main():
    data_input = baca_data()
    print("Data gudang:", data_input)

    perkembangan = peningkatan(data_input)
    print("\nPerkembangan produksi :", perkembangan)

    data_output = rata_rata(perkembangan)
    print("\nRata_rata :", data_output)

    write_data(data_output)


if __name__ == "__main__":
    main()
