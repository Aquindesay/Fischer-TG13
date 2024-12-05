
x = [1, 1, 2, 2, 3, 4, 5, 7, 7, 9, 5, 6, 7, 8, 8]
y = [4, 5, 3, 7, 6, 8, 7, 7, 8, 6, 1, 3, 9, 2, 3]

Farbe = ["Rot", "Rot", "Rot", "Rot", "Rot", "Grün", "Grün", "Grün", "Grün", "Grün", " Blau", " Blau", " Blau", " Blau", " Blau"]

Distanz = []

newX = int(input("X: "))
newY = int(input("Y: "))

for i in range(0, len(x)):
    for j in range(0, len(y)):
        distanz = abs(newX-i)^2+(newY-j)^2
        print(distanz)