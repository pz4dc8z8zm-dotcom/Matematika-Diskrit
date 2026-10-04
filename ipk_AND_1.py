ipk_memenuhi = True
penghasilan_rendah = True

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