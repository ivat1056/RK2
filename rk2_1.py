"RK 2"

Strin = input("Введите слово ")
massivP =[]
massivR =[]
for char in Strin:
    massivP.append(char)
for char in Strin:
    massivR.append(char)
massivR.reverse()
if massivR == massivP:
    print("True")
else:
    print("False")
