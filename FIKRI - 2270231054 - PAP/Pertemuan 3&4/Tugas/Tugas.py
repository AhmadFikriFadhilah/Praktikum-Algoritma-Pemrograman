print("""
=====================================
            Udin Cellular
        JL. Raya Cikunir No. 99
        Jakamulya - Kota Bekasi
=====================================
A. XIAOMI               : Rp. 3.000.000
B. SAMSUNG              : Rp. 5.000.000
C. OPPO                 : Rp. 6.500.000
D. VIVO                 : Rp. 7.000.000
=====================================""")
nama=input("Nama Pembeli           : ")
pesan=str(input("Nama Produk            : "))
jumlahpesanan=int(input("Jumlah Unit            : "))
nomor=input("Nomor HP               :")
alamat=input("Alamat                 :")
if pesan == "XIAOMI":
    harga=(3000000*jumlahpesanan)
elif pesan == "SAMSUNG":
    harga=(5000000*jumlahpesanan)
elif pesan == "OPPO":
    harga=(6500000*jumlahpesanan)
elif pesan == "VIVO":
    harga=(7000000*jumlahpesanan)
else:1

ppn = 50000+harga
print("---------------------------------")
print("Harga Satuan             :   Rp. {}".format(harga))
print("PPN                      :   Rp. 50000")
print("Total                    :   Rp. {}".format(ppn))
import time;
localtime = time.asctime( time.localtime(time.time()) )
print("Tanggal Pembelian        :", localtime)
print("---------------------------------")
print(""" 
     Syarat Dan Ketentuan Berlaku
   Garansi Hangus Jika Segel Rusak
  Jika Ada Masalah Silahkan Hubungi
        Telp. 0857-7728-4703
============TERIMAKASIH============
""")