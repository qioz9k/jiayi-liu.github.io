# 定义人口数据
a = 5.08  # 2004年人口
b = 5.33  # 2014年人口
c = 5.55  # 2024年人口

# 计算两个十年的人口增长数
d = b - a  # 2004-2014年增长：0.25（百万）
e = c - b  # 2014-2024年增长：0.22（百万）

# 计算结果打印
print("=== 苏格兰人口增长计算 ===")
print(f"2004-2014年增长：{d} 百万")
print(f"2014-2024年增长：{e} 百万")

# 判断增长趋势
is_decelerating = d > e  # 0.25>0.22 → True（减速）
print(f"人口增长是否减速：{is_decelerating}")
print(f"结论：苏格兰人口增长：{'减速' if is_decelerating else '加速'}")

# 布尔运算部分
X = True
Y = False

# 运算结果
M = X or Y

# 布尔运算打印
print("=== 布尔[X or Y]运算 ===")
print(f"X = {X}, Y = {Y}, M = X or Y = {M}")