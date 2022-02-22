# Menggabungkan string dari list

list_kata =  ['aku', 'mahasiswa', 'Fakultas', 'Informatika', 'Telkom', 'University']

kalimat = ' '.join(list_kata[0:3]).upper() + ' ' + ' '.join(list_kata[3:]).lower()
print(kalimat)

# menggunakan loop
list_kata =['aku', 'mahasiswa', 'Fakultas', 'Informatika', 'Telkom', 'University'] 
for i, string in enumerate(list_kata):
    if i < len(list_kata) / 2:
        list_kata[i] = string.upper ()
    else:
        list_kata[i] = - string.lower() 

kalimat = ' '.join(list_kata)
print(kalimat)