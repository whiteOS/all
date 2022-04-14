f = open("UP.txt","r")   # 设置文件对象
lis = f.read().splitlines()
f.close() # 关闭文件
for i in lis:
    print("ac_list.add("+'"'+i+'");')