ipk_memenuhi = False
penghasilan_rendah = False

# LOGIKA
if ipk_memenuhi and penghasilan_rendah:
    beasiswa = True
else:
    beasiswa = False

# OUTPUT
if beasiswa:
    print("Mahasiswa mendapat beasiswa")
else:
    print("Mahasiswa tidak mendapat beasiswa")