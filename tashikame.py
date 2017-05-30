

path1 = "../1/"
path2 = "../2/"


def main():
    for i in range(300000):
        if i % 5000 == 0:
            print(i)
        try:
            f = open(path1 + str(i) + ".txt", "r")
            f.close()
            try:
                f1 = open(path2 + str(i) + "_1.txt", "r")
                f1.close()
            except IOError:
                print(str(i) + " | f : OK  f1 : NG")
                pass
        except IOError:
            try:
                f1 = open(path2 + str(i) + "_1.txt", "r")
                f1.close()
                print(str(i) + " | f : NG f1 : OK")
            except:
                pass

if __name__=="__main__":
    main()

