import math
#Ham nhap du lieu
def NhapDuLieu():
    """
    Input:
    Ban phim = 1 5 6
    Output:
    (a, b, c) --> (1, 5, 6)
    """
    line = input("Moi ban nhap he so a, b, c: ")
    # Tách chuỗi và ép kiểu sang float
    a, b, c = map(float, line.split())
    return a, b, c
# NhapDuLieu
# Ham GiaiPhuongTrinhBac2
def GiaiPhuongTrinhBac2(a, b, c):
    """
    Input: a, b, c
    Output:
    + flag = -1 (VSN), 0 (VN), k (k nghiem)
    + () --> flag = -1, 0
    + (x) --> flag = 1
    + (x1, x2) --> flag = 2
    """
    flag = None
    x = ()
    #TH a=0
    if a == 0:
        if b == 0:
            if c == 0:
                flag = -1  # Vô số nghiệm
                x = ()
            else:
                flag = 0   # Vô nghiệm
                x = ()
        else:
            flag = 1       # 1 nghiệm: x = -c/b
            x = (-c/b,)
    #TH a!=0
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            flag = 0       # Vô nghiệm
            x = ()
        elif delta == 0:
            flag = 1       # Nghiệm kép
            x = (-b / (2*a),)
        else:
            flag = 2       # 2 nghiệm phân biệt
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            # Sắp xếp để x1 < x2
            x = tuple(sorted((x1, x2)))
            
    return flag, x

# Kết nối bài
a, b, c = NhapDuLieu()
# Gọi hàm giải
flag, x = GiaiPhuongTrinhBac2(1, 5, 6)
# Xuất dữ liệu
s = f'Phuong trinh bac 2 {a}x^2 + {b}x + {c} = 0'
if flag == -1:
    print(f'{s} co vo so nghiem!')
elif flag == 0:
    print(f'{s} vo nghiem!')
elif flag == 1:
    print(f'{s} co 1 nghiem, x = {x[0]}!')
elif flag == 2:
    print(f'{s} co 2 nghiem, x1 = {x[0]}, x2 = {x[1]}!')
# if
# Moi ban nhap he so a, b, c: 1 5 6
# Phuong trinh bac 2 1x^2 + 5x + 6 = 0 co 2 nghiem, x1 = -3.0, x2 = -2.0!
