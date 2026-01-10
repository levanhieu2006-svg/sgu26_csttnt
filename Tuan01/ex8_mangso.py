def NhapMang():
    """
    Input:
    Ban phim = 1 4 1 2 3 4 1 2 3 3 1 2 3 4 10 2
    Output:
    a = [1, 4, 1, 2, 3, 4, 1, 2, 3, 3, 1, 2, 3, 4, 10, 2]
    """
    line = input("Nhap mang: ")
    danh_sach_tam = line.split()
    a = []
    for i in danh_sach_tam:
        so = int(i)
        a.append(so)
    #...
    return a
# NhapMang
a = NhapMang() # 1 4 1 2 3 4 1 2 3 3 1 2 3 4 10 2
print(a)
# Moi ban nhap mang (cach nhau khoang trang): 1 4 1 2 3 4 1 2 3 3 1 2 3 4 10 2
# ['1', '4', '1', '2', '3', '4', '1', '2', '3', '3', '1', '2', '3', '4', '10', '2']

def XuatMang(a):
    """
    Input:
    a = [1, 4, 1, 2, 3, 4, 1, 2, 3, 3, 1, 2, 3, 4, 10, 2]
    Output:
    In ra man hinh:
    Mang co 16 phan tu: 1 4 1 2 3 4 1 2 3 3 1 2 3 4 10 2
    """
    n = len(a)
    print(f"Mang co {n} phan tu:", end=" ")
    for i in range(n):
        print(a[i], end=" ")
    # ...
# XuatMang
a = [1, 4, 1, 2, 3, 4, 1, 2, 3, 3, 1, 2, 3, 4, 10, 2]
XuatMang(a)
# Mang co 16 phan tu: 1 4 1 2 3 4 1 2 3 3 1 2 3 4 10 2

import random
def SinhNgauNhien(n, vmin = -10, vmax = 10):
    """
    Input:
    n = 30, vmin = -10, vmax = 10
    Output:
    a = [-1, -4, -8, 6, 4, -5, -1, -4, -9, -5, -10, 0, -6, 2, 1, -9, -9, 10, -8, -9, -7,
    9, 2, -4, -1, -6, 5, -6, 9, -8]
    """
    a = []
    for i in range(n):
        so_ngau_nhien = random.randint(vmin, vmax)
        a.append(so_ngau_nhien)
    # ...
    return a
# SinhNgauNhien

b = SinhNgauNhien(30, -10, 10)
print(b)
b = SinhNgauNhien(30, vmin = 0)
print(b)
b = SinhNgauNhien(30, vmax = 2)
print(b)

def DemTongChanLe(a):
    """
    Input: a[] = [1, 4, 2, 0, -1, -7, 3, -6, 4, 9, -5, 7, 7, -7, -10, 1, -10, 9, -4, -6, 10, -
    2, -10, -8, -3, 2, -7, -10, 6, 0]
    Output: tong, sochan, sole
    """
    tong = 0
    sochan = 0
    sole = 0
    
    for i in a:
        tong += i
        
        if i%2 == 0:
            sochan += 1
        else:
            sole += 1
    # ...
    return tong, sochan, sole
# DemTongChanLe
a = [1, 4, 2, 0, -1, -7, 3, -6, 4, 9, -5, 7, 7, -7, -10, 1, -10, 9, -4, -6, 10, -2, -10, -8, -
3, 2, -7, -10, 6, 0]
print(DemTongChanLe(a))
a = [9, 6, 5, 0, 8, 8, 1, 10, 0, 0, 1, 1, 2, 7, 1, 10, 9, 1, 10, 8, 2, 8, 4, 5, 4, 5, 5, 3, 6,
2]
print(DemTongChanLe(a))
# (-31, 17, 13)
# (141, 17, 13)

def DayChanLe(a): # Gia tri tra ve
    """
    Input:
    a = [1, 4, 2, 0, -1, -7, 3, -6, 4, 9, -5, 7, 7, -7, -10, 1, -10, 9, -4, -6, 10, -2, -
    10, -8, -3, 2, -7, -10, 6, 0]
    Output: (achan, ale)
    achan = [4, 2, 0, -6, 4, -10, -10, -4, -6, 10, -2, -10, -8, 2, -10, 6, 0]
    ale = [1, -1, -7, 3, 9, -5, 7, 7, -7, 1, 9, -3, -7]
    """
    achan = []
    ale = []
    
    for i in a:
        if i%2 == 0:
            achan.append(i)
        else:
            ale.append(i)
    # ...
    return achan, ale
# DayChanLe
a = [1, 4, 2, 0, -1, -7, 3, -6, 4, 9, -5, 7, 7, -7, -10, 1, -10, 9, -4, -6, 10, -2, -10, -8, -
3, 2, -7, -10, 6, 0]
achan, ale = DayChanLe(a)
print(f'DayChanLe:\nChan = {achan}\nLe = {ale}\n')
# DayChanLe:
# Chan = [4, 2, 0, -6, 4, -10, -10, -4, -6, 10, -2, -10, -8, 2, -10, 6, 0]
# Le = [1, -1, -7, 3, 9, -5, 7, 7, -7, 1, 9, -3, -7]