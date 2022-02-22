def baca_data():
    f = open('input_nilai.txt', 'r')

    list_siswa = []

    for baris in f:
        nim, nama, tugas, uts, uas = baris.split()
        list_siswa.append({
            'nim' : nim,
            'nama' : nama,
            'tugas' : float(tugas),
            'uts' : float(uts),
            'uas' : float(uas)
        })

    f.close
    return list_siswa

def hitung_na(siswa):
    siswa['nilai_akhir'] = (30/100) * siswa['tugas'] + (30/100) * siswa['uts'] + (40/100) * siswa['uas']
    return siswa

def tulis_data(list_siswa):
    f = open('output_nilai.txt', 'w')

    for siswa in list_siswa:
        baris = ' '.join([ str(x) for x in siswa.values() ])
        f.write(baris + '\n')

    f.close

def main():
    list_siswa = baca_data()
    print('input : ', list_siswa)
    nilai_siswa = list(map(hitung_na, list_siswa))
    print('output', nilai_siswa)
    tulis_data(list_siswa)

if __name__ == '__main__':
    main()