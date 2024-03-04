from tabulate import tabulate

# DEKLARASI FUNGSI

# FUNGSI TAMPIL SEMUA BENEFIT

def all_benefit():
    header = ["Membership", "Benefit", "Discount"]
    benefit = [["Platinum", "Benefit Silver + Benefit Gold + Voucher Liburan + Cashback Max 30%", "15%"],
               ["Gold", "Benefit Silver + Voucher Ojek Online", "10%"],
               ["Silver", "Voucher Makan", "8%"]]
    return tabulate(benefit,header)

# FUNGSI TAMPIL REQUIREMENT

def requirement():
    header = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]
    req = [["Platinum", 8, 15], ["Gold", 6, 10], ["Silver", 5, 7]]
    return tabulate(req, header)

# FUNGSI HITUNG BENEFIT

def hitung(x,y):
    from math import sqrt
    hitung = sqrt(((x[0]-y[0])**2)+((x[1]-y[1])**2))
    return(hitung)

# FUNGSI PICK BENEFIT

def pick_benefit(monthly_expanse, monthly_income):
    tuple_req = (["platinum", 8, 15], ["gold", 6, 10], ["silver", 5, 7])
    pick_value = [monthly_expanse, monthly_income]
    hasil = []
    x = 0
    for i in tuple_req:
        pick_tupel = []
        pick_tupel.append(tuple_req[x][1])
        pick_tupel.append(tuple_req[x][2])
        hasil_tupel = hitung(x=pick_value, y=pick_tupel)
        hasil.append(hasil_tupel)
        x += 1
    hasil_req = min(hasil)
    if hasil_req == hasil[0]:
        kesimpulan = tuple_req[0][0]
        return kesimpulan
    elif hasil_req == hasil[1]:
        kesimpulan = tuple_req[1][0]
        return kesimpulan
    elif hasil_req == hasil[2]:
        kesimpulan = tuple_req[2][0]
        return kesimpulan
    else:
        return ("ada kesalahan input")

# FUNGSI DISKON
    
def pick_diskon(belanja,membership):
    if membership.lower() == "silver":
        hasil = belanja*0.08
        return f'anda mendapat diskon sebesar Rp{hasil},-'
    elif membership.lower() == "gold":
        hasil = belanja*0.1
        return f'anda mendapat diskon sebesar Rp{hasil},-'
    elif membership.lower() == "platinum":
        hasil =  belanja*0.3
        cashback = hasil*0.15
        return f'anda mendapat diskon sebesar Rp{hasil},- dan cashback sebesar Rp{cashback},-'
    else:
        return "tidak ada layanan"




#daftar = all_benefit()
#req = requirement()
#tupel = pick_benefit(12,20)
#print(f'anda adalah member {tupel}')

