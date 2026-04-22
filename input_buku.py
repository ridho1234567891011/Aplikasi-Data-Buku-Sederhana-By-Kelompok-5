def inputBuku () :
    nama_petugas = input("Masukkan nama petugas hari ini : ")
    data_buku = []

    while True :
        for i in range(3) :
            judul_buku = input(f"Judul buku {i+1} : ")
            halaman_buku = int(input("Jumlah Hal : "))
        
            data_buku.append({
                "Judul" : judul_buku,
                "Halaman buku" : halaman_buku 
            })
        
        confirm = input("Mau input 3 judul buku lagi ? (y/n)")
        if confirm.lower() == "n" :
            break 
        
    hasil = {
            "nama_petugas" : nama_petugas,
            "data_buku" : data_buku
        }
    
    return hasil 
        

