"""
# Tugas Konversi Mata Uang Menggunakan REST API kurs.web.id
Buat Program untuk Konversi Mata Uang
Menu :
1. IDR to Mata Uang Asing
2. Mata Uang Asing to IDR

Pilihan 1 :
- Masukkan Nama Bank :
- Masukkan Mata Uang Asing :
- Masukkan Nilai Rupiah : 

Output :
Nilai uang anda (mata uang asing) dalam rupiah adalah ... (nilai konversi)
Punya Rupiah mau jadikan dollar pakai harga jual
Punya Dollar mau jadikan rupiah pakai harga beli

Error Handling:
Ketika nama bank tidak ada
Nama bank tidak bisa angka/simbol
Nama mata uang asing tidak bisa angka/simbol/nama yang tidak ada

Nama mata uang tidak bisa alfabet atau simbol
{'status': 'success', 'bank': 'BCA', 'matauang': 'USD', 'jual': 14465, 'beli': 14435, 'timestamp': '2021-03-09'}
"""

import requests
muter = True

while muter:
    try:
        print("Menu")
        print("1. IDR to Mata Uang Asing")
        print("2. Mata Uang Asing to IDR")
        no = int(input("Masukkan Pilihan Menu : "))
        if no == 1:
            print("\nIDR to Mata Uang Asing")
            muter1 = True
            while muter1:
                bank1 = str(input("Masukkan Nama Bank : ")).lower()
                if bank1.isalpha() != True:
                    print("Nama Bank yang anda masukkan salah !")
                    continue
                else:
                    pass
                asing1 = str(input("Masukkan Mata Uang Asing : ")).lower()
                if asing1.isalpha() != True:
                    print("Mata Uang Asing yang anda masukkan salah !")
                    continue
                else:
                    pass
                duit1 = str(input("Masukkan Jumlah Rupiah Anda : "))
                try:
                    link1 = "https://api.kurs.web.id/api/v1?token=AxxwDHs48WzLaLrKHO64O8uVnmehs73KhilhwR4z&bank="+bank1+"&matauang="+asing1
                    out1 = requests.get(link1) # line ini yang ke hit
                    data = out1.json()
                    # data = {'status': 'success', 'bank': 'BCA', 'matauang': 'USD', 'jual': 14465, 'beli': 14435, 'timestamp': '2021-03-09'}
                    if duit1.isdigit() == True:
                        duit1 = int(duit1)
                        jual = data['jual']
                        apa = data['matauang']
                        hasilbeli = duit1 / jual # user beli mata uang asing ke bank
                        print("Nilai tukar uang anda IDR", duit1,"di bank", bank1.upper(),"dalam", apa.upper(),"adalah", round(hasilbeli,2))
                        muter1 = False
                        muter = False
                        print("Terima Kasih sudah menggunakan Program Ini")
                    else:
                        print("Jumlah Mata Uang Harus Integer dan tidak menerima negatif !")
                        muter1 = True
                except:
                    print("Nilai Tukar Kurs tidak ditemukan, Silahkan cek Nama Bank dan Mata Uang Asing anda!")
                    muter1 = True
        elif no == 2:
            print("\nMata Uang Asing to IDR")
            muter2 = True
            while muter2:
                bank2 = str(input("Masukkan Nama Bank : ")).lower()
                if bank2.isalpha() != True:
                    print("Nama Bank yang anda masukkan salah !")
                    continue
                else:
                    pass
                asing2 = str(input("Masukkan Mata Uang Asing : ")).lower()
                if asing2.isalpha() != True:
                    print("Mata Uang Asing yang anda masukkan salah !")
                    continue
                else:
                    pass
                duit2 = str(input("Masukkan Jumlah Mata Uang Asing Anda : "))
                try:
                    link2 = "https://api.kurs.web.id/api/v1?token=AxxwDHs48WzLaLrKHO64O8uVnmehs73KhilhwR4z&bank="+bank2+"&matauang="+asing2
                    out2 = requests.get(link2) # line ini yang ke hit
                    data = out2.json()
                    # data = {'status': 'success', 'bank': 'BCA', 'matauang': 'USD', 'jual': 14465, 'beli': 14435, 'timestamp': '2021-03-09'}
                    if duit2.isdigit() == True:
                        duit2 = int(duit2)
                        if bank2 == data['bank'].lower() and asing2 == data['matauang'].lower() and duit2 >= 0:
                            beli = data['beli']
                            apa = data['matauang']
                            hasiljual = duit2 * beli # user jual mata uang asing ke bank
                            print("Nilai tukar uang anda", duit2, apa.upper(),"di bank", bank2.upper(),"dalam IDR adalah", round(hasiljual,2))
                            muter2 = False
                            muter = False
                            print("Terima Kasih sudah menggunakan Program Ini")
                    else:
                        print("Jumlah Mata Uang Harus Integer dan tidak menerima negatif !")
                        muter2 = True
                except:
                    print("Nilai Tukar Kurs tidak ditemukan, Silahkan cek Nama Bank dan Mata Uang Asing anda!")
                    muter2 = True
        else:
            print("Menu tidak ditemukan")
            continue
    except:
        print("Input yang anda masukkan salah!")
        continue
