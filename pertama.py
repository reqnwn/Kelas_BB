data_panen={
    'lokasi1':{
        'nama_lokasi':'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2':{
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3':{
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4':{
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5':{
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("\nSoal 1")
for lokasi, detail in data_panen.items():
    print(f"Nama Lokasi: {detail['nama_lokasi']}, Hasil Panen: {detail['hasil_panen']}")

print("\nSoal 2")
jumlah_jagung_lokasi2=data_panen["lokasi2"]["hasil_panen"]["jagung"]
print(f"Jumlah hasil panen jagung di lokasi2: {jumlah_jagung_lokasi2}")

print("\nSoal 3")
nama_lokasi3=data_panen["lokasi3"]["nama_lokasi"]
print(f"Nama lokasi 3: {nama_lokasi3}")

print("\nSoal 4 & 5")
hasil_padi={lokasi: detail['hasil_panen']['padi'] for lokasi,detail in data_panen.items()}
hasil_keledai={lokasi: detail['hasil_panen']['kedelai'] for lokasi,detail in data_panen.items()}

print("Jumlah hasil panen padi setiap lokasi: ")
print(hasil_padi)

print("\nJumlah hasil panen keledai setiap lokasi:")
print(hasil_keledai)

print("\nSoal 6")
for lokasi, detail in data_panen.items():
    padi=detail['hasil_panen']['padi']
    jagung=detail['hasil_panen']['jagung']

    if padi > 1300 or jagung > 800:
        print(f"Lokasi {detail['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {detail['nama_lokasi']} dalam kondisi baik.")