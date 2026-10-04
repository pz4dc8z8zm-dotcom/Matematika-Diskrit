kartu_mahasiswa = False
kartu_anggota = True

# LOGIKA OR
boleh_masuk = kartu_mahasiswa or kartu_anggota

# OUTPUT
if boleh_masuk:
    print("Boleh masuk perpustakaan")
else:
    print("Tidak boleh masuk perpustakaan")