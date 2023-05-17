#from xlwt import Workbook

#wb = Workbook()

#wb.add_sheet("Sheet 1")
def get_max_salary(f, max_sal_local):
    for line in f.readlines():
        data = line.split(",")
        data[1] = int(data[1])
        if max_sal_local < data[1]:
            max_sal_local = data[1]
    return max_sal_local

def sum_month(file, luna):
    sum_salary = 0
    for line in file.readlines():
        data = line.split(",")
        data[1] = int(data[1])
        if data[2] == luna:
            sum_salary += data[1]
    return sum_salary

def no_salary(file, luna):
    k = 0
    for line in file.readlines():
        data = line.split(",")
        if data[2] == luna:
            k += 1
    return k

f1 = open("f1.txt","r")
f2 = open("f2.txt","r")
f3 = open("f3.txt","r")

print(f1.readline())
print(f2.readline())
print(f3.readline())

# Salariul maxim

max_sal_local = 0
max_sal_f1 = get_max_salary(f1, max_sal_local)
max_sal_f2 = get_max_salary(f2, max_sal_local)
max_sal_f3 = get_max_salary(f3, max_sal_local)

max_sal = max_sal_f3
print(f'Salariul maxim este {max_sal}')

# Suma salariilor din Octombrie

f3 = open("f3.txt", "r")
print(f3.readline())
suma_Octombrie = sum_month(f3, " Octombrie\n")
print(f"Suma salariilor pe luna Octombrie {suma_Octombrie} lei")

#Media salariilor

f2 = open("f2.txt", "r")
f3 = open("f3.txt", "r")

print(f2.readline())
print(f3.readline())

no_August = no_salary(f2, " August\n")

no_Octombrie = no_salary(f3, " Octombrie\n")
print(no_August)
print(no_Octombrie)
f2 = open("f2.txt", "r")

print(f2.readline())

suma_August = sum_month(f2, " August\n")
print(suma_August)
media_Octombrie = suma_Octombrie/no_Octombrie
media_August = suma_August/no_August

print(f"Media salriilor pe luna Octombrie este {media_Octombrie} lei")
print(f"Media salriilor pe luna August este {media_August} lei")