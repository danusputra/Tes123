# input  : Nama, Username, Password, Nama Kamar, Fasilitas, Harga, Charge,Tanggal Check-in, Lama Menginap 
# output : Detail Pemesanan Kamar

import datetime as dt

listkamar= [
           {
               "namakamar":"Reguler",
               "fasilitas":"\n 1. AC\n 2. Air Panas\n 3. Pembuat Kopi",
               "harga":"100000",
           },
           {
               "namakamar":"Golden",
               "fasilitas":"\n 1. AC\n 2. Air Panas\n 3. Pembuat Kopi\n 4. Balkon",
               "harga":"200000",
           },
           {
               "namakamar":"Platinum",
               "fasilitas":"\n 1. AC\n 2. Air Panas\n 3. Pembuat Kopi\n 4. Bath tub",
               "harga":"350000",
           },
           {
               "namakamar":"Presidental Suites",
               "fasilitas":"\n 1. AC\n 2. Air Panas\n 3. Pembuat Kopi\n 4. Balkon\n 5. Bath tub",
               "harga":"800000",
           }
]
charge =[
          {"Makan" : 100000},
          {"Sauna" : 150000},
          {"Salon" : 125000},
          {"Pijat" : 150000}
]
chargeterpilih={}

#Login
userpass={'admin':'123'}
userid=input('Masukkan username:')
password=input('Masukkan password:')
if userid in userpass and password == userpass[userid]:
    print('Login berhasil')
else:
    print('Login gagal')
    quit()

#Halaman awal
nama=input('Masukkan nama customer :')
print('='*50)
print('Selamat datang di ICL Hotel')
print('='*50)
print('Berikut merupakan jenis kamar yang tersedia di Hotel ICL')

#Daftar kamar
i=0
for indeks, item in enumerate(listkamar,start=1):
    namakamar=listkamar[i]['namakamar']
    fasilitas=listkamar[i]['fasilitas']
    harga=listkamar[i]['harga']
    print(indeks, 'Nama Kamar:', namakamar, '\nFasilitas:', fasilitas, "\nHarga:", harga, "\n")
    i+=1
    indeks+=1

#Pilih kamar
pilihan=int(input('Masukkan kode kamar yang dipilih:'))
kamarterpilih=listkamar[pilihan-1]['namakamar']
print('Anda akan memilih kamar', kamarterpilih)
harga=listkamar[pilihan-1]['harga']

#Daftar charge
print('Berikut daftar charge yang tersedia pada Hotel ICL:')
for i, item in enumerate(charge,start=1):
    for key, value in item.items():
        print(i,key,":", value)
    i+=1

#Pilih charge
q=input('Apakah anda ingin memilih charge yang tersedia ? (yes/no) ').lower()
while q =='yes':
    pilihan2=int(input('Masukkan kode charge:'))
    for key, value in charge[pilihan2-1].items():
        if key in chargeterpilih:
            print('Anda telah memilih charge tersebut')
            continue
        chargeterpilih[key]=value
    q=input('Apakah anda ingin memilih charge lagi ? (yes/no) ')

#Masukkan tanggal check in
checkin=input('Tanggal check in (yyyy-mm-dd) : ')
tanggalcheckin=dt.datetime.strptime(checkin, '%Y-%m-%d')
menginap=int(input('Lama menginap (hari) :'))
biayakamar=int(harga)*menginap
tanggalcheckout=tanggalcheckin+dt.timedelta(menginap)

#Detail
print('='*50)
print(''*10, 'Detail Pesanan')
print('='*50)
print('Nama Customer \t\t\t:', nama)
print('Nama Kamar \t\t\t:', kamarterpilih)
print('Lama Menginap \t\t\t:', menginap)
print('Tanggal Check In \t\t\t:', tanggalcheckin.date())
print('Tanggal Check Out \t\t\t:', tanggalcheckout.date())
if len(chargeterpilih)>0:
    print('Charge \t\t\t:')
    for key, value in chargeterpilih.items():
        print('\t',key,'\t\t:',value)
    print('Subtotal Charge \t:', sum(chargeterpilih.values()))
print('Subtotal Kamar \t\t:', biayakamar)
print('Total \t\t\t:', biayakamar+sum(chargeterpilih.values()))
print('='*50)