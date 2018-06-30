# 将字符串 s 拆分成两个字符串 s1、s2，其中 s1 只包含字母，转换为小写，以 [a-z] 排序，s2 只包含数值，升序排序
def chaifen():
    s = "aAsnr3id2d4b6gs7DZsf9e1AF"
    #将字符串转化为小写
    s = s.lower()
    s1_list = []
    s2_list = []
    for i in s:
        #判断元素是否为数字，是添加到s2中，反之添加到s1中
        if i.isdigit() == True:
            s2_list.append(i)
            s2_list.sort()
        else:
            s1_list.append(i)
            s1_list.sort()
    #将列表转化为字符串
    s1 = "".join(s1_list)
    s2 = "".join(s2_list)
    print("s1=%s"%s1)
    print("s2=%s"%s2)

if __name__ == "__main__":
    chaifen()


