#使用while循环打印 1 3 5 7 9
def xunhuan():
   i = 1
   while i<=9:
       if i%2 != 0:
           print(i)
           i+=2
if __name__ == "__main__":
    xunhuan()