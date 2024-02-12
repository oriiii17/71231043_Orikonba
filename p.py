harga_awal = 650000
harga_2 = 685000
emas_gram = 25

harga_awal_total = emas_gram * harga_awal
harga_2_total = emas_gram * harga_2
keuntungan_Rp = harga_2_total - harga_awal_total
keuntungan_persen = (keuntungan_Rp / harga_2_total) * 100

keuntungan_persen = round(keuntungan_persen, 1)

print("Keuntungan yang didapat oleh Gerard setelah kenaikan harga pertama:")
print("Dalam rupiah:", keuntungan_Rp)
print("Dalam persen:", keuntungan_persen,"%")

harga_3 = 715000
emas_2 = 40
tambahan_emas = 15

total_harga_emas = emas_gram * harga_awal + (emas_2 - emas_gram) * harga_2
total_emas_sekarang = emas_2 + tambahan_emas
keuntungan_sekarang = (harga_3 - harga_2) * tambahan_emas
total_harga_emas_akhir = total_harga_emas + (tambahan_emas * harga_3)
total_keuntungan = keuntungan_Rp + keuntungan_sekarang
keuntungan_persen = (total_keuntungan / total_harga_emas_akhir) * 100
keuntungan_persen = round(keuntungan_persen, 1)

print("\nKeuntungan yang didapat oleh Gerard setelah kenaikan harga kedua:")
print("Dalam rupiah:", total_keuntungan)
print("Dalam persen:", keuntungan_persen, "%")
