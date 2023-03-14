#Nama lengkap dan jumlah huruf
nama = input("Nama: ")
#user dapat memasukkan nama dengan menggunakan fungsi input
jumlah_huruf = len(nama)
#menggunakan fungsi len untuk menghitung jumlah huruf dalam nama yang telah dimasukkan
print("Nama saya adalah", nama)
#print untuk menampilkan output dengan memanggil variabel yang telah dibuat
print("Jumlah huruf dalam nama saya adalah", jumlah_huruf)
#print untuk menampilkan output dengan memanggil variabel yang telah dibuat


#Menghitung vokal
vokal = "aiueoAIUEO"
#memasukkan vokal dalam variabel vokal dengan huruf besar dan kecil akan semua font terbaca
jumlah_vokal = 0
#membuat variabel jumlah vokal diawali dengan 0
for huruf in nama:
    #menggunakan perulangan for
    if huruf in vokal:
        #program akan menginisialisasi huruf dalam nama termasuk vokal atau tidak
        jumlah_vokal += 1
        #jika huruf terbaca merupakan vokal maka akan tambah 1 dan seterusnya
print("Jumlah huruf vokal dalam nama saya adalah", jumlah_vokal)
#print untuk menampilkan output dan memanggil variabel jumlah vokal


#Menghitung konsonan
huruf_konsonan = 0 
#membuat variabel huruf konsonan mulai 0
for huruf in nama:
    #menggunakan perulangan for
    if huruf.isalpha() and huruf not in "aiueoAIUEO":
        #memastikan karakter atau huruf merupakan konsonan
         huruf_konsonan += 1
         #jika terbaca huruf merupakan konsonan maka jumlah akan menambah 1 dan seterusnya
print("Jumlah huruf konsonan dalam nama saya adalah", huruf_konsonan)
#print menampilkan output dan memanggil variabel huruf kosonan yang telah ada








