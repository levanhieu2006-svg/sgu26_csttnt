def docfile(fpath = "XEPHAU.INP"):
    with open(fpath, "rt") as file:
        content = file.read()
        n = int(content)
        pass
    return n
    pass


# n = 3
def LietKeHau(n, action = "list"):
    hau = [-1] * (n+1) #[-1, -1, -1, -1]
    dong = [0] * (n+1)  #[0, 0, 0, 0]
    cheo1 = [0] * (2*n) #[0, 0, 0, 0, 0, 0]
    cheo2 = [0] * (2*n) #[0, 0, 0, 0 ,0 ,0]
    info   = {"n" : n, "hau" : hau, "dong" : dong,
              "cheo1" : cheo1, "cheo2" : cheo2,
              "coDapAn" : False, "action" : action,
              "cnt" : 0, "laInDapAn": True }
    TryHau(1, info)

    return info
    pass

def InDapAn(info):
    print(info["cnt"])
    for i in range(1, info["n"]+1):
        for j in range(1, info["n"]+1):
            if info["hau"][j] == i:
                print("1", end = " ")
            else:
                print("0", end = " ")
        print()
    print
    pass

def TryHau(k, info):
    if info["coDapAn"] is True and info["action"] == "find":
        return
    n, hau, dong, cheo1, cheo2 = [info[x] for x in ["n", "hau", "dong", "cheo1", "cheo2"]]
    for vk in range(1, n+1):
        if dong[vk] == 0 and cheo1[vk-k+n] == 0 and cheo2[vk+k-1] == 0:
            hau[k] = vk
            dong[vk], cheo1[vk-k+n], cheo2[vk+k-1] = 1, 1, 1
            if k == n:
                info["coDapAn"] = True
                info["cnt"] = info["cnt"] + 1
                if info["laInDapAn"] is True:
                    InDapAn(info)
            else:
                TryHau(k+1, info)
            
            hau[k] = -1
            dong[vk], cheo1[vk-k+n], cheo2[vk+k-1] = 0, 0, 0
            pass
        pass
    pass

def main(sfile, **kwargs):
    n = docfile(sfile)
    info = LietKeHau(n, action = "find")
    if info["coDapAn"] is False:
        print("0")
    kwargs.get("debug",{}).update(locals())
    pass

def test1(**kwargs):
    n = docfile("XEPHAU.INP")

    print('-'*5, 'Doc File', '-'*5)
    print(f'n = {n}')
    print('Ket qua:')
    LietKeHau(n)

    kwargs.get("debug", {}).update(locals())
    pass

if __name__ == "__main__":
    import argparse


    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type = str,default = "help" ,help ="test1, main")
    parser.add_argument('--file', type = str, default = "XEPHAU.INP", help='file path')
    args, _ = parser.parse_known_args()
    params = vars(args)

    if params['action'] == "test1":
        test1(debug = globals())
    elif params['action'] == "main":
        main(sfile = params['file'], debug = globals())
    else:
        parser.print_help()
    pass           