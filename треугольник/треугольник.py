print("����� ��������� ������� ����� ������������, � ����������� �� �������� ���� ������")
print("������������ ����� ����: ��������������, ��������������, ��������������")
line1 = float(input("������� ������ ������ �������:"))
line2 = float(input("������� ������ ������ �������:"))
line3 = float(input("������� ������ ������� �������:"))
a = bool(line1 + line2 > line3)
b = bool(line1 + line3 > line2)
c = bool(line2 + line3 > line1)
if a and b and c == True :
    if line1 == line2 == line3 :
        print('����������� �������������')
    elif(ine1 == line2) or (line2 ==line3) or (line1 ==line3):
        print('����������� ��������������')
    else :
        print("����������� ��������������")
else:
    print("����������� �� ����������")