import os, sys

os.system('clear')

print ("=====================")
print ("KALKULATOR SEDERHANA")
print ("=====================")

operator = input("Masukan Operator '(+*-/%)' : ")
angka_a  = int(input("Masukan Angka Pertama : "))
angka_b  = int(input("Masukan Angka Kedua : " ))

if operator == "+":
	hasil = angka_a + angka_b
	print (f"Hasil Dari : {angka_a} + {angka_b} = {hasil}")
elif operator == "-":
	hasil = angka_a - angka_b
	print (f"Hasil Dari : {angka_a} - {angka_b} = {hasil}")
elif operator == "*":
	hasil = angka_a * angka_b
	print (f"Hasil Dari : {angka_a} * {angka_b} = {hasil}")
elif operator == "/":
	hasil = angka_a / angka_b
	print (f"Hasil Dari : {angka_a} / {angka_b} = {hasil}")
elif operator == "%":
	hasil = angka_a % angka_b
	print (f"Hasil Dari : {angka_a} % {angka_b} = {hasil}")
else:
	print("Error")

