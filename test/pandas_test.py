# 定义多个全局变量
var1 = 1
var2 = 2
var3 = 3

# 动态访问全局变量
for i in range(1, 4):
    var_name = f'var{i}'
    print(globals()[var_name])
