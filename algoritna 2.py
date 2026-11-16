nama = input("Masukkan nama pelanggan: ")
pemakaian = int(input("Masukkan jumlah pemakaian listrik (kWh): "))

if pemakaian >= 1 and pemakaian <= 100:
    tarif = 1000
    biaya_pemakaian = pemakaian * tarif
    biaya_admin = 0

elif pemakaian >= 101 and pemakaian <= 200:
    tarif = 1500
    biaya_pemakaian = pemakaian * tarif
    biaya_admin = 0

elif pemakaian > 200:
    tarif = 2000
    biaya_pemakaian = pemakaian * tarif
    biaya_admin = 25000

else:
    print("Pemakaian listrik tidak valid!")
    

total_tagihan = biaya_pemakaian + biaya_admin

print("========== TAGIHAN LISTRIK ==========")
print("Nama Pelanggan      :", nama)
print("Pemakaian Listrik   :", pemakaian, "kWh")
print(f"Tarif per kWh       : Rp {tarif:,.0f}")
print(f"Biaya Pemakaian     : Rp {biaya_pemakaian:,.0f}")
print(f"Biaya Administrasi  : Rp {biaya_admin:,.0f}")
print("-------------------------------------")
print(f"Total Tagihan       : Rp {total_tagihan:,.0f}")
print("=====================================")
