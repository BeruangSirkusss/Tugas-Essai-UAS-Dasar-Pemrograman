import pandas as pd

df = pd.read_excel(r'sensus.xlsx')

print("Data Awal:")
print(df)

df_sorted = df.sort_values(by='JENIS\nKELAMIN')

print("\nData Setelah Diurutkan berdasarkan jenis kelamin:")
print(df_sorted)

male_count = df[df['JENIS\nKELAMIN'] == 'L'].shape[0]
female_count = df[df['JENIS\nKELAMIN'] == 'P'].shape[0]
print("\nJumlah Laki-laki:", male_count)
print("Jumlah Perempuan:", female_count)

print("\nData dengan Umur Lebih dari 50 Tahun:")
print(df[df['USIA'] > 50])

moved_count = df[df['NAMA'] == 'Y'].shape[0]
print("\nJumlah Orang yang Pindah Memilih:", moved_count)