kontak = {}


def tambah_kontak():
    nama = input("masukkan nama:")
    nomer = input("masukkan nomer HP:")
    
    if nama in kontak:
        print("kontak sudah ada!")
    else:
        kontak[nama] = nomer
        print("kontak berhasil ditambahkan.")
        
        
def lihat_kontak():
    print("\n=== DAFTAR KONTAK ===")
    
    if not kontak:
        print("Belum ada kontak.")
        return
    
    for nama, nomer in kontak.items():
        print(f"Nama  : {nama}")
        print(f"Nomer : {nomer}")
        print("_" * 25)
        
        
def update_kontak():
    nama = input("Masukkan nama kontak yang ingin diubah: ")
    
    if nama in kontak:
        nomer_baru = input("Maukkan nomer HP baru: ")
        kontak[nama] = nomer_baru
        print("Kontak berhasil diubah.")
    else:
        print("Kontak tidak ditemukan.")
        
        
def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus :")
    
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")
        
        
def main():
    while True:
        print("\n=== CRUD KONTAK HP ===")
        print("1. Tambah Kontak")
        print("2. Lihat Kontak")
        print("3. Update Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tambah_kontak()
        if pilihan == "2":
            lihat_kontak()
        if pilihan == "3":
            update_kontak()
        if pilihan == "4":
            hapus_kontak()
        if pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
            
            
main()
