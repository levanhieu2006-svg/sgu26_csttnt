import math
# Nhập dữ liệu
n = int(input("Moi ban nhap so nguyen n: "))
# Xử lý
lant = True
if n<2:
    lant = False
else:
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            lant = False
            break
# Xuất dữ liệu
if lant == True:
    print(f'{n} la so nguyen to.')
else:
    print(f'{n} khong la so nguyen to.')