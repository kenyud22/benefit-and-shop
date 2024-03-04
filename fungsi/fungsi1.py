def jadwal_catering():
    hari = input("masukkan nama hari: ")
    if hari == 'Senin' or hari == 'senin':
        print(f'jadwal hari {hari} adalah Nasi Kuning')
    elif hari == 'Selasa' or hari == 'selasa':
        print(f'jadwal hari {hari} adalah Salad Sayur')
    elif hari == 'Rabu' or hari == 'rabu':
        print(f'jadwal hari {hari} adalah Soto Ayam')
    elif hari == 'Kamis' or hari == 'kamis':
        print(f'jadwal hari {hari} adalah Nasi Goreng')
    elif hari == 'Jumat' or hari == 'jumat':
        print(f'jadwal hari {hari} adalah Rawon')
    else:
        print("Catering tidak tersedia")

print("SELAMAT DATANG DI CATERING BERKAH")
print("Silahkan cek ketersediaan menu")
jadwal_catering()


