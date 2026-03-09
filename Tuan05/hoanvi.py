def docTapTin(fpath="HOANVI.INP"):

    with open(fpath,"rt") as f:
        content = f.readlines()
        n = int(content[0].strip())
        a = [line.strip() for line in content[1:n+1]]
    return n, a
def InKQ(x, a):
    for i in range(1, len(x)):
        print(a[x[i]], end=" ")
    print()
def Try(i, info):
    x = info["x"]
    used = info["used"]
    n = info["n"]
    for j in range(n):
        if not used[j]:

            x[i] = j
            used[j] = True

            if i == n:
                info["cnt"] += 1
                InKQ(x, info["a"])
            else:
                Try(i+1, info)

            used[j] = False
def LietKeHoanVi(n, a):
    x = [-1]*(n+1)
    used = [False]*n

    info = dict(x=x, used=used, n=n, a=a, cnt=0)

    Try(1, info)

    print("Tong so hoan vi:", info["cnt"])
def main():
    n,a = docTapTin()
    LietKeHoanVi(n,a)
if __name__ == "__main__":
    main()