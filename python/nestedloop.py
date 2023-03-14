panjang = int(input("Masukkan panjang deret angka:")) 
#membuat variabel untuk memasukkan panjang angka deret fibbonaci

fibo = [0, 1] 
#list fibo diawali dengan angka 0 dan 1

for i in range(2,panjang): 
    #menggunakan perulangan for 2-n kali
        while len(fibo) <= panjang: 
            #jika jumlah elemen dalam fibo kurang dari atau sama dengan n
                    print(fibo) 
                    #maka yang dicetak adalah fibo pada setiap i
                    angka1 = fibo[-2] 
                    #memanggil 2 elemen fibo
                    angka2 = fibo[-1]
                    #memanggil elemen fibo
                    angka_next = angka1 + angka2 
                    #2 elemen terakhir dijumlahkan
                    fibo.append(angka_next) 
                    #menambahkan hasil penjumlahan ke dalam fibo
                    i+=1 
                    #setiap perulangan maka i akan bertambah 1 dan seterusnya






