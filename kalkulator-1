#kalkulator.py

def kalkulator():
    print("=== KALKULATOR SEDERHANA ===")
    
    while True:
        print("\npilih operasi:")
        print("1. penjumlahan (+)")
        print("2. pengurangan (-)")
        print("3. perkalian (*)")
        print("4.pembagian (/)")
        print("5. keluar")
        
        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == "5":
            print("Program selesai.")
            break
        
        if pilihan not in {"1", "2", "3", "4"} :
                print("pilihan tidak valid!")
                continue
            
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
                
            if pilihan == "1":
                hasil = angka1 + angka2
            elif pilihan == '2':
                hasil = angka1 - angka2
            elif pilihan == "3":
                hasil = angka1 * angka2
            elif pilihan == "4": 
                if angka2 == 0:
                        print("Error: Tidak bisa membagi dengan nol!")
                        continue
                hasil = angka1/angka2
                    
            print(f"Hasil: {hasil}")
        
        except ValueError:
            print("Input harus berupa angka!")
            

kalkulator()
