# List untuk menyimpan data mahasiswa
students = []

# Menghitung nilai akhir
def calculate_final_grade(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

# Program Nilai
while True:
    # Input data mahasiswa
    name = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    # Menghitung nilai akhir
    final_grade = calculate_final_grade(tugas, uts, uas)
    
    # Menyimpan data mahasiswa dalam list
    students.append({"No": len(students) + 1, "Nama": name, "NIM": nim, "Tugas": tugas, "UTS": uts, "UAS": uas, "Akhir": final_grade})
    
    # Tanya apakah ingin menambah data lagi
    add_more = input("Tambah data(y/t)? ")
    if add_more.lower() != 'y':
        break

# Tampilkan tabel data mahasiswa
print("="*80)
print("| No | Nama    | NIM   | Tugas | UTS  | UAS  | Akhir |")
print("="*80)

for student in students:
    print(f"| {student['No']:2} | {student['Nama']:7} | {student['NIM']:5} | {student['Tugas']:5} | {student['UTS']:5} | {student['UAS']:5} | {student['Akhir']:6.2f} |")

print("="*80)
