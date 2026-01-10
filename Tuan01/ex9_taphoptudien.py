def XuLyKhongTrung(a):
    """
    Input:
    a = ['A', 'G', 'C', 'A', 'C', 'F', 'F', 'T', 'H']
    Output:
    s = ['A', 'C', 'F', 'G', 'H', 'T']
    """
    s = set([])
    for i in a:
        s.add(i)
    # ...
    return sorted(s)
# XuLyKhongTrung
a = ['A', 'G', 'C', 'A', 'C', 'F', 'F', 'T', 'H']
b = XuLyKhongTrung(a)
print(b)
# ['A', 'C', 'F', 'G', 'H', 'T']

def DemSoLanXuatHien(a):
    """
    Input:
    a = ['A', 'G', 'C', 'A', 'C', 'F', 'F', 'T', 'H']
    Output:
    dem = {'A': 2, 'G': 1, 'C': 2, 'F': 2, 'T': 1, 'H': 1}
    """
    dem = {} # (k, v): k (ky tu) v (so lan xuat hien)
    
    for i in a:
        if i in dem:
            dem[i] += 1
        else:
            dem[i] = 1
    # ...
    return dem
# DemSoLanXuatHien
a = ['A', 'G', 'C', 'A', 'C', 'F', 'F', 'T', 'H']
b = DemSoLanXuatHien(a)
print(b)
# {'A': 2, 'G': 1, 'C': 2, 'F': 2, 'T': 1, 'H': 1}