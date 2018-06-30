#字符串排序
s="hello world"
s_list =sorted(s)
#删除空白元素
s_list.remove(' ')
new_s = "".join(s_list)
print(new_s)