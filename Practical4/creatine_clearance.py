
"""
伪代码（实验文档要求）：
1. 定义输入变量：年龄(age)、体重(weight)、性别(gender)、肌酐浓度(Cr)
2. 输入合法性校验（按优先级）：
   - 年龄校验：age < 100
   - 体重校验：20 < weight < 80
   - 肌酐校验：0 < Cr < 100
   - 性别校验：gender为male/female（兼容大小写）
3. 校验不通过：打印具体错误信息（明确指出哪个变量出错）
4. 校验通过：计算CrCl：
   - 基础公式：CrCl = [(140 - 年龄) × 体重] / (72 × 肌酐浓度)
   - 女性修正：CrCl × 0.85
5. 打印计算结果（保留2位小数，更直观）
"""


age = 45               # 年龄（岁）
weight = 65            # 体重（kg）
gender = "female"      # 性别（male/female，兼容大写如Female）
cr = 80                # 肌酐浓度（μmol/l）


# age = 101
# weight = 18  # 体重<20kg
# cr = 105     # 肌酐>100μmol/l
# gender = "man" # 性别错误

error_msg = ""  # 初始化错误提示字符串

# 1. 校验年龄（优先级1）
if age >= 100:
    error_msg = f"年龄错误：{age}岁 ≥ 100岁，需小于100岁"
# 2. 校验体重（优先级2）
elif not (20 < weight < 80):
    error_msg = f"体重错误：{weight}kg，需在20-80kg之间（不含边界）"
# 3. 校验肌酐浓度（优先级3）
elif not (0 < cr < 100):
    error_msg = f"肌酐浓度错误：{cr}μmol/l，需在0-100μmol/l之间（不含边界）"
# 4. 校验性别（优先级4，兼容大小写）
elif gender.lower() not in ["male", "female"]:
    error_msg = f"性别错误：{gender}，只能为male或female（大小写均可）"

if error_msg == "":
    # 基础公式计算CrCl
    crcl = (140 - age) * weight / (72 * cr)
    # 女性需乘以0.85（统一转小写避免大小写问题）
    if gender.lower() == "female":
        crcl = crcl * 0.85
    # 输出结果（保留2位小数，符合实验输出要求）
    print("=== 肌酐清除率（CrCl）计算结果 ===")
    print(f"输入参数：年龄={age}岁，体重={weight}kg，性别={gender}，肌酐={cr}μmol/l")
    print(f"CrCl = {crcl:.2f} ml/min")
else:
    # 校验失败，输出具体错误
    print("❌ 输入不合法：", error_msg)