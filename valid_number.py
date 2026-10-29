number = int(input("Geef cijfer tussen (1-10): "))


while number not in range(1, 11):
    number = int(input("Geef een geldig getal in: "))

print("Geldig getal ingevoerd!")
