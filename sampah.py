import pandas as pd


data = {
    'Kabupaten/Kota': ['Kota Bandung', 'Kabupaten Bogor', 'Kota Bekasi', 'Kabupaten Bandung',
                       'Kota Depok', 'Kabupaten Garut', 'Kota Cimahi', 'Kabupaten Cianjur',
                       'Kota Sukabumi', 'Kabupaten Sukabumi', 'Kota Tasikmalaya', 'Kabupaten Tasikmalaya',
                       'Kota Bandung', 'Kabupaten Bogor', 'Kota Bekasi', 'Kabupaten Bandung',
                       'Kota Depok', 'Kabupaten Garut', 'Kota Cimahi', 'Kabupaten Cianjur',
                       'Kota Sukabumi', 'Kabupaten Sukabumi', 'Kota Tasikmalaya', 'Kabupaten Tasikmalaya',
                       'Kota Bandung', 'Kabupaten Bogor', 'Kota Bekasi', 'Kabupaten Bandung',
                       'Kota Depok', 'Kabupaten Garut', 'Kota Cimahi', 'Kabupaten Cianjur',
                       'Kota Sukabumi', 'Kabupaten Sukabumi', 'Kota Tasikmalaya', 'Kabupaten Tasikmalaya',
                       'Kota Bandung', 'Kabupaten Bogor', 'Kota Bekasi', 'Kabupaten Bandung',
                       'Kota Depok', 'Kabupaten Garut', 'Kota Cimahi', 'Kabupaten Cianjur',
                       'Kota Sukabumi', 'Kabupaten Sukabumi', 'Kota Tasikmalaya', 'Kabupaten Tasikmalaya'],
    'Tahun': [2020, 2020, 2020, 2020, 
              2020, 2020, 2020, 2020,
              2020, 2020, 2020, 2020,
              2021, 2021, 2021, 2021,
              2021, 2021, 2021, 2021,
              2021, 2021, 2021, 2021,
              2022, 2022, 2022, 2022,
              2022, 2022, 2022, 2022,
              2022, 2022, 2022, 2022,
              2023, 2023, 2023, 2023,
              2023, 2023, 2023, 2023,
              2023, 2023, 2023, 2023],
    'Produksi Sampah' : [50000, 75000, 60000, 85000, 
                         47000, 56000, 52000, 48000,
                         49000, 53000, 51000, 55000,
                         55000, 77000, 62000, 88000,
                         47000, 57000, 54000, 50000,
                         52000, 58000, 56000, 59000,
                         58000, 79000, 65000, 89000,
                         50000, 59000, 57000, 52000,
                         54000, 60000, 58000, 61000,
                         60000, 80000, 68000, 91000,
                         52000, 61000, 59000, 55000,
                         56000, 63000, 60000, 65000]
}

df = pd.DataFrame(data)
print("\nDataFrame Awal:")
print(df)

print("Soal Ke-2")
tahun_tertentu = 2023
total_produksi_tahun = df[df['Tahun'] == tahun_tertentu]['Produksi Sampah'].sum()
print(f"\nTotal Sampah pada Tahun {tahun_tertentu}: {total_produksi_tahun} ton")

print("Soal Ke-3")
df_produksi_per_tahun = df.groupby('Tahun')['Produksi Sampah'].sum().reset_index()
df_produksi_per_tahun.rename(columns={'Produksi Sampah': 'Total Produksi Sampah'}, inplace=True)
print("\nTotal Sampah Per Tahun:")
print(df_produksi_per_tahun)

print("Soal Ke-4")
df_produksi_per_kota_tahun = df.groupby(['Kabupaten/Kota', 'Tahun'])['Produksi Sampah'].sum().reset_index()
df_produksi_per_kota_tahun.rename(columns={'Produksi Sampah': 'Total Produksi Sampah'}, inplace=True)
print("\nTotal Sampah Per Kota/Kabupaten Per Tahun:")
print(df_produksi_per_kota_tahun)

df_produksi_per_tahun.to_csv('SampahTahun.csv', index=False)
df_produksi_per_kota_tahun.to_excel('SampahKotaTahun.xlsx', index=False)
print("\nHasil telah diexport ke 'PSampahTahun.csv' dan 'SampahKotaTahun.xlsx'")
