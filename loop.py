kapaciteti = 5
studentet_regjistruar = 0


while studentet_regjistruar < kapaciteti:
    print(f"Studenti {studentet_regjistruar + 1} është regjistruar.")
    studentet_regjistruar += 1

    print(f"Total i studenteve te regjistruar: {studentet_regjistruar}")
WHILE LOOP

depozitat = [100,250,300,450,500]

total_depozita = 0
for i in range(len(depozitat)):
    total_depozita += depozitat[i]


    print(f"Shuma totale e depozitave eshte: {total_depozita} $")
RANGE LOOP

studentet = ["Engjulli","Ovesa","Priam","Ylljon","Enzo"]

print("Studentet e regjistruar jane:")
for student in studentet:
    print(student)
FOR LOOP
