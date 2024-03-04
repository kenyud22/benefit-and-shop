import fungsi2
print("==========================")
print("SELAMAT DATANG DI PACCOMMERCE")
print("==========================")

print("BERIKUT FITUR PADA APLIKASI")
print("1. LAYANAN KAMI")
print("2. REQUIREMENT BENEFIT")
print("3. LAYANAN ANDA")
print("4. DISKON BELANJA YANG ANDA DAPATKAN")

ambil = int(input("Silahkan masukkan nomor fitur: "))
layanan = []
if ambil == 1:
    print(fungsi2.all_benefit())
elif ambil == 2:
    print(fungsi2.requirement())
elif ambil == 3:
    penghasilan_bulan = int(input("Masukkan penghasilan bulanan anda: "))
    pengeluaran_bulan = int(input("Masukkan pengeluaran anda sebulan: "))
    benefit = fungsi2.pick_benefit(monthly_income=penghasilan_bulan, monthly_expanse=pengeluaran_bulan)
    print(f'Anda berada pada layanan: {fungsi2.pick_benefit(monthly_income=penghasilan_bulan, monthly_expanse=pengeluaran_bulan)}')
    layanan.append(benefit)
elif ambil == 4:
    penghasilan_bulan = int(input("Masukkan penghasilan bulanan anda: "))
    pengeluaran_bulan = int(input("Masukkan pengeluaran anda sebulan: "))
    benefit = fungsi2.pick_benefit(monthly_income=penghasilan_bulan, monthly_expanse=pengeluaran_bulan)
    print(f'Anda berada pada layanan: {fungsi2.pick_benefit(monthly_income=penghasilan_bulan, monthly_expanse=pengeluaran_bulan)}')
    layanan.append(benefit)
    barang = []
    while True:
        belanja = input("Apakah anda akan belanja?(y/n): ")
        if belanja.lower() == "y" or belanja.lower() == "ya":
            harga = int(input("Masukkan harga barang anda: "))
            barang.append(harga)
            continue
        elif (belanja.lower() == "no" or belanja.lower() == "n") and len(barang) == 0:
            print("terimakasih atas kunjungan anda")
            break
        elif (belanja.lower() == "no" or belanja.lower() == "n") and len(barang) != 0:
            total = sum(barang)
            hasil = fungsi2.pick_diskon(belanja=total,membership=layanan[0])
            print(hasil)
            break
else:
    print("tidak ada")
