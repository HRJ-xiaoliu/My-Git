temper=input("你好，请输入摄氏度（例：23C）或华氏度（例：67F）：")
if temper[-1] in ['f','F']:
    C= (eval(temper[0:-1]-32))/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif temper[-1] in ['c','C']:
    F = 1.8*eval(temper[0:-1])+32
    print('转换后的温度是{:.2f}F'.format(F))
else:
    print("输入格式错误")

