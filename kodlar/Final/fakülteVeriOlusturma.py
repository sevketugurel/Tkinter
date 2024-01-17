import random

# List of possible fakulte names
fakulte_names = ["Mühendislik", "Edebiyat", "Fen Bilimleri", "İktisat", "Hukuk", "Tıp", "İnsan ve Toplum Bilimleri"]

# List of possible bolum names
bolum_names = ["Bilgisayar Mühendisliği", "Kimya", "İngiliz Dili ve Edebiyatı", "Makine Mühendisliği", "İşletme", "Fizik", "Psikoloji"]

# List of possible ogretim elemani names
ogretim_elemani_names = ["Prof. Dr. Ahmet Yılmaz", "Doç. Dr. Ayşe Demir", "Yrd. Doç. Dr. Mehmet Aksoy", "Dr. Zeynep Can", "Öğr. Gör. Elif Aydın"]

# Number of fakulte entries
num_entries = 20

# Generate random data
with open("fakültelerVeri.txt", "w") as file:
    for _ in range(num_entries):
        fakulte = random.choice(fakulte_names)
        bolum = random.choice(bolum_names)
        ogretim_elemani = random.choice(ogretim_elemani_names)

        file.write(f"{fakulte},{bolum},{ogretim_elemani}\n")

print("Random data has been generated and written to 'fakültelerVeri.txt'.")
