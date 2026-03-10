
"""
伪代码（实验文档要求）：
1. 定义初始参数：
   - 初始感染人数 = 5
   - 日增长率 = 40%（即0.4）
   - 班级总人数 = 91
   - 当日感染数 = 初始感染数
   - 天数 = 1（第1天为初始状态）
2. 打印初始感染信息（方便验证）
3. 启动while循环：当当日感染数 < 91时，持续计算：
   - 天数 +1
   - 当日感染数 = 前一日感染数 × (1 + 增长率)
   - 打印当日天数和感染数（保留1位小数，更直观）
4. 循环结束后，打印全员感染的总天数
"""


initial_infected = 5       # 初始感染人数
growth_rate = 0.4          # 日增长率40%
total_students = 91        # 班级总人数
current_infected = initial_infected  #每日感染人数
days = 1                   # 初始天数（第1天）


print("=== 班级感染扩散模拟 ===")
print(f"初始感染人数：{initial_infected} 人")
print(f"日增长率：{growth_rate*100}%")
print(f"班级总人数：{total_students} 人")
print("-" * 30)
print(f"第 {days} 天，感染人数：{current_infected} 人") 
# 循环条件：只要当日感染数 < 总人数，就继续计算
while current_infected < total_students:
    days += 1  # 天数加1（进入下一天）
    # 计算当日感染数：前一日感染数 × (1 + 增长率)
    current_infected = current_infected * (1 + growth_rate)
    # 打印当日数据（保留1位小数，避免小数位数过多）
    print(f"第 {days} 天，感染人数：{current_infected:.1f} 人")


print("-" * 30)
print(f"模拟结束，全员{total_students}人感染，共花费 {days} 天")