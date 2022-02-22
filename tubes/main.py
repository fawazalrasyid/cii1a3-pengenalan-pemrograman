def read_data():
    """
    fungsi untuk membaca data dari file data.txt
    """

    f = open("data.txt", "r")

    data_rumah = {}

    data_penghuni = {}

    baris = 0

    for row in f:

        # jika baris pertama berarti menyatakan no rumah anda dan jumlah rumah
        if baris == 0:
            rumah_anda, jumlah_rumah = list(map(int, row.split()))

        # jika bukan baris pertama maka data akan dibaca perbaris
        else:
            r = row.split()
            jarak = int(r[0])
            posisi = r[2]
            arah = r[3]
            tetangga = r[5]
            pemilik = r[-1]

            # inisialisasi no rumah
            nr = 0

            # jika dict masih kosong maka no rumah di inisialisasi dengan no rumah anda
            if data_penghuni == {}:
                nr = rumah_anda
            # jika dict sudah ada data maka no rumah di inisialisasi dengan no rumah tetangga
            else:
                nr = data_penghuni[tetangga]["no_rumah"]

            # fungsi untuk menentukan no rumah

            # jika posisi di seberang
            if posisi == "seberang":
                # jika no rumah ganjil
                if nr % 2 != 0:
                    nr += 1
                    if arah == "kiri":
                        nr -= jarak * 2
                    else:
                        nr += jarak * 2
                else:
                    nr -= 1
                    if arah == "kiri":
                        nr -= jarak * 2
                    else:
                        nr += jarak * 2
            else:
                # jika no rumah ganjil
                if nr % 2 != 0:
                    if arah == "kiri":
                        nr -= jarak * 2
                    else:
                        nr += jarak * 2
                else:
                    if arah == "kiri":
                        nr -= jarak * 2
                    else:
                        nr += jarak * 2

            # update data dictionary
            data_penghuni[pemilik] = {
                "nama_penghuni": pemilik,
                "no_rumah": nr,
            }

        baris += 1

    data_rumah = {
        "penghuni": data_penghuni,
        "jumlah_rumah": jumlah_rumah,
    }

    f.close
    return data_rumah


def prosses_data(data_rumah):
    """
    fungsi untuk memproses dictionary dari data yg sudah dibaca sebelumnya,
    data akan diproses dan dimasukkan ke dalam dict sesuai no rumah ganjil atau genap.
    Kemudian setelah data diprosses fungsi akan mengemblikan data dictionary rumah,
    yang didalamnya terdapat dict ganjil dan genap.
    """

    temp_rumah = {}
    jumlah_rumah = data_rumah["jumlah_rumah"]

    ganjil = {}
    genap = {}

    rumah = {}

    for m in data_rumah["penghuni"].values():
        np = m["nama_penghuni"]
        nr = m["no_rumah"]
        temp_rumah[nr] = np

    for i in range(1, jumlah_rumah + 1):
        np = temp_rumah.get(i)
        if i % 2 != 0:
            ganjil[i] = {
                "no_rumah": i,
                "penghuni": np if np != None else "tidak diketahui",
            }
        else:
            genap[i] = {
                "no_rumah": i,
                "penghuni": np if np != None else "tidak diketahui",
            }

    rumah = {
        "ganjil": ganjil,
        "genap": genap,
    }

    return rumah


def nomor_rumah(data, nama_penghuni):
    """
    fungsi untuk mencari nomor rumah dengan parameter nama penghuni
    """

    nomor_rumah = "tidak tahu"

    for k, v in data.items():

        for m, n in v.items():

            if nama_penghuni.lower() == n["penghuni"].lower():
                nomor_rumah = n["no_rumah"]

    return nomor_rumah


def penghuni_rumah(data, no_rumah):
    """
    fungsi untuk mencari nama penghuni rumah dengan parameter nomor rumah
    """

    penghuni_rumah = "tidak tahu"

    for k, v in data.items():

        for m, n in v.items():

            if no_rumah == n["no_rumah"]:
                penghuni_rumah = n["penghuni"]

    return penghuni_rumah


def main():
    data_input = read_data()
    # print(data_input)

    data = prosses_data(data_input)
    # print(data)

    print("\nTugas Besar Pengenalan Pemrograman\n")

    print("Nama\t: Fawaz Al Rasyid")
    print("NIM\t: 1301213016")
    print("No Soal\t: 23. Gosip Kang Sayur")

    print("\n=============== Main Menu ===============\n")

    print("1. Cari Nomor Rumah")
    print("2. Cari Penghuni")
    print("3. Print Dictionary")

    pilih_menu = input("\nSilahkan pilih menu [1/2/3] : ")

    print("\n=========================================\n")

    if pilih_menu == "1":
        nama_penghuni = input("Masukkan nama penghuni : ")
        nr = nomor_rumah(data, nama_penghuni)

        print("\nNomor rumah dengan penghuni", nama_penghuni, "adalah", nr, "\n")

    elif pilih_menu == "2":
        no_rumah = int(input("Masukkan nomor rumah : "))
        np = penghuni_rumah(data, no_rumah)

        print("\nNama penghuni dengan nomor rumah", no_rumah, "adalah", np, "\n")

    elif pilih_menu == "3":
        print(data)

    else:
        print("Menu tidak tersedia")


if __name__ == "__main__":
    main()
