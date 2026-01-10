# Nhập dữ liệu
t = int(input('Nhap vao tong so giay: '))
# Xử lý
hh = t // 3600
mm = (t % 3600) // 60
ss = t % 60
# Xuất dữ liệu
print(f'{t} giay co dang {hh}:{mm}:{ss}')