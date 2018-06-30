#替换
def tihuan(student,chengdu):
    a = "i,am,a,student,in,chengdu"
    a = a.replace(","," ")
    a = a.replace("student","%s").replace("chengdu","%s")
    new_a = a%(student,chengdu)
    print(new_a)
if __name__ == "__main__":
    tihuan(123,456)