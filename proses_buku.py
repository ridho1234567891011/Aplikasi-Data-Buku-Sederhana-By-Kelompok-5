def prosesBuku(proses) :
    print(" ")
    print(" ")
    print(f'===DAFTAR BUKU DENGAN PETUGAS {proses["nama_petugas"].upper()}===')    
    no = 0
    for data in proses["data_buku"] :
        no += 1
        print(f"No.{no}")
        for key,value in data.items() :
            print(f"{key} : {value}")
        print(" ")

    print("BUKU DENGAN HALAMAN TERBANYAK : ")
    data_halaman = []
    for data in proses["data_buku"] :
        for key,value in data.items() :
            if key == "Halaman buku" :
                data_halaman.append(value)

    data_halaman_terbanyak = max(data_halaman)
    for data in proses["data_buku"] :
        if data["Halaman buku"] == data_halaman_terbanyak :
            print(f"Judul : {data['Judul']}")
            print(f"Halaman buku : {data['Halaman buku']}")

    print(" ")
    print("TOTAL HALAMAN SELURUH DATA BUKU : ")
    print(f"Total Halaman : {sum(data_halaman)}")    