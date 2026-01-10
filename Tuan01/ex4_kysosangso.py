#Nhập dữ liệu
s = input("Moi ban nhap chuoi ky so s: ")
en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
vi = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#Xử lí
if s in en:
    index = en.index(s)
    chuoi_vi = vi[index]
    ky_so = num[index]
    #Xuất dữ liệu
    print(f"Chuoi vua nhap hop le!")
    print(f'"{s}" bieu dien cho "{ky_so}" va ung voi Tieng Viet "{chuoi_vi}"')
else:
    print(f"Chuoi vua nhap khong hop le!")

    