bayar_tunai = False
bayar_transfer = True

# LOGIKA XOR
transaksi = bayar_tunai ^ bayar_transfer

# OUTPUT
if transaksi:
    print("Transaksi berhasil")
else:
    print("Pilih tepat satu metode pembayaran")