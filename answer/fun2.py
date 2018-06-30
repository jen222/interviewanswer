#查找6是否在列表中
def chazhao():
    l = [1,5,7,8,9]
    a = 6
    if a in l:
        print("found")
    elif a not in l:
        print("not found")
if __name__ == "__main__":
    chazhao()