# Nhập dữ liệu
n = int(input("Moi ban nhap so nguyen n: "))
# Xuất dữ liệu
s = 0
for i in range(n + 1):
    if i%2 == 0:
        s += i
# ...
print(f'Tong cac so chan tu 1 den {n} la {s}.')