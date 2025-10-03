print("анная программа выводит форму треугольника, в зависимости от задданых длин сторон")
print("Треуголиники могут быть: равносторонний, равнобедренный, разносторонний")
line1 = float(input("введите длинну первой стороны:"))
line2 = float(input("введите длинну второй стороны:"))
line3 = float(input("введите длинну третьей стороны:"))
a = bool(line1 + line2 > line3)
b = bool(line1 + line3 > line2)
c = bool(line2 + line3 > line1)
if a and b and c == True :
    if line1 == line2 == line3 :
        print('треугольник равностороний')
    elif (line1 == line2) or (line2 ==line3) or (line1 ==line3):
        print('треугольник равнобедренный')
    else :
        print("треугольник разносторонний")
else:
    print("треугольник не существует")
