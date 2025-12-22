# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 09:44:34 2025

@author: borak

Question A
"""
"""
# 1. 获取输入
# 输入是一个数字字符串，例如 "112223"
s = input()

# --- 第一步：统计每个数字出现的次数 ---
# count_dict 的结构形如：{'1': 2, '2': 3, '3': 1}
count_dict = {}

for char in s:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

# --- 第二步：构建“次数 -> 数字列表”的新字典 ---
# 我们需要把上面字典的“键”和“值”反过来组织
# result_dict 的结构形如：{2: ['1'], 3: ['2'], 1: ['3']}
result_dict = {}

# .items() 可以同时遍历键和值
for digit, count in count_dict.items():
    # 如果这个“次数”还没在字典里，先创建一个空列表
    if count not in result_dict:
        result_dict[count] = []
    
    # 把当前的数字加入到对应次数的列表中
    result_dict[count].append(digit)

# --- 第三步：排序并输出 ---
# 1. 对字典的键（次数）进行排序
# sorted() 函数会返回一个排好序的列表
sorted_counts = sorted(result_dict.keys())

# 2. 遍历排好序的次数
for count in sorted_counts:
    # 获取对应的数字列表
    digits_list = result_dict[count]
    
    # 题目要求列表内部的数字也要排序（比如 '1' 要在 '3' 前面）
    digits_list.sort()
    
    # 按格式输出：次数 和 对应的数字列表
    print(f"{count}:{digits_list}")
    
Question B    
"""
"""
# 1. 获取输入
n = int(input())

# 2. 建立初始名单
# 使用 range(1, n + 1) 生成 [1, 2, 3, ..., n]
people = list(range(1, n + 1))

# 3. 初始化索引
# index 代表当前我们要操作的人在列表中的下标（从0开始）
index = 0

# 4. 开始循环，直到只剩下一个人
while len(people) > 1:
    # --- 核心逻辑 ---
    # 我们要数 3 个数。
    # 新的下标 = (当前下标 + 2) % 当前剩余人数
    # 为什么要 +2？因为假设当前位置是数"1"，下一位是"2"，再下一位才是"3"(被淘汰者)
    # 为什么要取余(%)？为了模拟“围成一圈”，走到队尾自动回到队头
    index = (index + 2) % len(people)
    
    # 5. 将该位置的人移出列表
    # pop(index) 会删除指定下标的元素，后面的元素会自动前移填补空缺
    people.pop(index)
    
    # 注意：删除元素后，原本排在后面的人补位到了 index 这个位置
    # 所以下一次报数（数"1"）正好就应该从当前的 index 位置开始
    # 因此 index 不需要额外加 1

# 6. 输出最后剩下的人
print(people[0])

Question C
"""
"""
# 1. 获取输入
num = int(input())

# 2. 循环直到结果为 6174
while num != 6174:
    # --- 关键步骤：补齐4位 ---
    # 先转为字符串
    s = str(num)
    
    # 使用 .zfill(4) 方法
    # 它的作用是：如果字符串长度少于4，就在左边自动补0
    # 例如："456".zfill(4) 变成 "0456"
    s = s.zfill(4)
    
    # --- 排序生成最大数 ---
    # list(s) 将字符串拆成列表 ['0', '4', '5', '6']
    digits = list(s)
    
    # 从大到小排序 -> 最大数
    digits.sort(reverse=True)
    max_str = "".join(digits)
    max_num = int(max_str)
    
    # --- 排序生成最小数 ---
    # 从小到大排序 -> 最小数
    digits.sort()
    min_str = "".join(digits)
    min_num = int(min_str)
    
    # --- 计算差值 ---
    diff = max_num - min_num
    
    # --- 输出当前步骤 ---
    # 不使用 f-string，可以使用 .format() 方法
    # {} 是占位符，后面的变量会依次填入
    print("{} - {} = {}".format(max_num, min_num, diff))
    
    # --- 更新 num，进入下一轮循环 ---
    num = diff

Question D
"""
"""
# 1. 获取输入 n
# 输入的第一行是数量
n = int(input())

# 2. 获取小朋友的名字
names = []
for _ in range(n):
    names.append(input())

# 3. 获取候选的数字
numbers = []
for _ in range(n):
    # 注意：一定要转成整数 int()
    # 否则字符串排序时 "10" 会排在 "2" 的前面，导致结果错误
    numbers.append(int(input()))

# 4. 核心步骤：分别排序
# sort() 方法默认就是：字符串按字典序，数字按从小到大
names.sort()
numbers.sort()

# 5. 一一对应输出
# 因为两个列表长度都是 n，且都排好了序，直接用同一个下标 i 访问即可
for i in range(n):
    print(names[i], numbers[i])

QuestionF
"""
"""

# 1. 获取输入
# 输入格式为一行，用空格隔开的四个整数
a, n, m, x = map(int, input().split())

# 2. 初始化数组
# 我们需要记录每一站的情况。为了方便理解，数组大小设为 20 (题目通常n<=20)
# 或者直接动态创建大小为 n+1 的数组，方便使用下标 1~n
# up_a[i] 表示第 i 站【上车】人数中 a 的倍数
# up_u[i] 表示第 i 站【上车】人数中 u 的倍数
# sum_a[i] 表示第 i 站【开出时】车上总人数中 a 的倍数
# sum_u[i] 表示第 i 站【开出时】车上总人数中 u 的倍数

up_a = [0] * (n + 1)
up_u = [0] * (n + 1)
sum_a = [0] * (n + 1)
sum_u = [0] * (n + 1)

# 3. 设置初始状态 (第1站和第2站)
# 第1站：上车 a (1*a + 0*u)，开出时车上 a (1*a + 0*u)
up_a[1] = 1; up_u[1] = 0
sum_a[1] = 1; sum_u[1] = 0

# 第2站：上车 u (0*a + 1*u)，开出时车上 a (1*a + 0*u)
# 题目中说第2站上、下车人数相同，所以开出人数保持不变
up_a[2] = 0; up_u[2] = 1
sum_a[2] = 1; sum_u[2] = 0

# 4. 循环计算从第3站到第 n-1 站的情况
for i in range(3, n):
    # 【上车人数规律】：等于前两站上车人数之和
    up_a[i] = up_a[i-1] + up_a[i-2]
    up_u[i] = up_u[i-1] + up_u[i-2]
    
    # 【车上人数规律】：
    # 这一站开出人数 = 上一站开出人数 + 这一站上车 - 这一站下车
    # 题目规律：这一站下车人数 = 上一站上车人数
    # 所以：这一站开出人数 = 上一站开出人数 + 这一站上车 - 上一站上车
    # 也就是： sum[i] = sum[i-1] + up[i] - up[i-1]
    sum_a[i] = sum_a[i-1] + up_a[i] - up_a[i-1]
    sum_u[i] = sum_u[i-1] + up_u[i] - up_u[i-1]

# 5. 解方程算出 u
# 题目已知：最后一站下车人数是 m，意味着第 n-1 站开出时车上人数就是 m
# 方程： sum_a[n-1] * a + sum_u[n-1] * u = m
# 推导 u 的计算公式：
coefficient_a = sum_a[n-1]
coefficient_u = sum_u[n-1]

# 计算 u (第2站上车人数)
# 注意使用整除 //，因为人数必须是整数
u = (m - coefficient_a * a) // coefficient_u

# 6. 计算第 x 站的结果
# 既然知道了 u，就把 u 代入到第 x 站的公式里
result = sum_a[x] * a + sum_u[x] * u

print(result)

Question G
"""
"""
# 1. 获取输入
# 假设输入是 "10, 5, 20, 5, 12"
input_str = input()

# 2. 数据处理：分割 -> 转整数 -> 去重 -> 排序
# split(',') 将字符串按逗号切分成列表
# set() 集合自动去除重复元素
# sorted() 将集合排序并转回列表
# 这一行代码完成了所有预处理工作
nums = sorted(list(set(map(int, input_str.split(',')))))

# 3. 初始化变量
# min_diff 用于记录当前找到的最小差值
# 我们将其初始化为一个无穷大的数，确保第一个算出的差值一定能被记录下来
min_diff = float('inf') 

# result_pair 用于存储对应的两个数
result_pair = []

# 4. 遍历列表，寻找相邻的两个数
# 注意：循环范围是 range(len(nums) - 1)
# 因为我们要比较 nums[i] 和 nums[i+1]，如果是最后一个元素，它后面没有数了，不能比较
for i in range(len(nums) - 1):
    
    # 计算相邻两个数的差值
    # 因为已经从小到大排好序了，直接用 后一个 减 前一个
    current_diff = nums[i+1] - nums[i]
    
    # 5. 打擂台：比较当前差值是否比记录的最小差值更小
    if current_diff < min_diff:
        min_diff = current_diff
        # 记录下这两个数
        result_pair = [nums[i], nums[i+1]]

# 6. 按要求格式输出
# 这里假设输出格式为两个数中间用逗号隔开，例如 "10,12"
print(f"{result_pair[0]},{result_pair[1]}")

Question H
"""
"""
# 1. 获取输入
# 假设输入是 "10, 5, 20, 5, 12"
input_str = input()

# 2. 数据处理：分割 -> 转整数 -> 去重 -> 排序
# split(',') 将字符串按逗号切分成列表
# set() 集合自动去除重复元素
# sorted() 将集合排序并转回列表
# 这一行代码完成了所有预处理工作
nums = sorted(list(set(map(int, input_str.split(',')))))

# 3. 初始化变量
# min_diff 用于记录当前找到的最小差值
# 我们将其初始化为一个无穷大的数，确保第一个算出的差值一定能被记录下来
min_diff = float('inf') 

# result_pair 用于存储对应的两个数
result_pair = []

# 4. 遍历列表，寻找相邻的两个数
# 注意：循环范围是 range(len(nums) - 1)
# 因为我们要比较 nums[i] 和 nums[i+1]，如果是最后一个元素，它后面没有数了，不能比较
for i in range(len(nums) - 1):
    
    # 计算相邻两个数的差值
    # 因为已经从小到大排好序了，直接用 后一个 减 前一个
    current_diff = nums[i+1] - nums[i]
    
    # 5. 打擂台：比较当前差值是否比记录的最小差值更小
    if current_diff < min_diff:
        min_diff = current_diff
        # 记录下这两个数
        result_pair = [nums[i], nums[i+1]]

# 6. 按要求格式输出
# 这里假设输出格式为两个数中间用逗号隔开，例如 "10,12"
print(f"{result_pair[0]},{result_pair[1]}")

Question I
"""
"""
# 1. 获取输入
# 输入是一个加密后的字符串
encrypted_str = input()

# 2. 初始化结果字符串
decrypted_str = ""

# 3. 遍历字符串中的每一个字符
for char in encrypted_str:
    
    # --- 情况1：如果是小写字母 (a-z) ---
    if 'a' <= char <= 'z':
        # 步骤解析：
        # 1. ord(char) - ord('a')：算出该字母是第几个（0-25），比如 'd' 是 3
        # 2. - 3：往前推 3 位，解密
        # 3. % 26：处理循环。如果结果是负数（比如 'a' 的 0-3=-3），Python 会自动转成 23 ('x')
        # 4. + ord('a')：变回 ASCII 码
        # 5. chr(...)：把 ASCII 码变回字符
        new_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
        decrypted_str += new_char
        
    # --- 情况2：如果是大写字母 (A-Z) ---
    elif 'A' <= char <= 'Z':
        # 逻辑同上，只是基准变成了 'A'
        new_char = chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
        decrypted_str += new_char
        
    # --- 情况3：其他字符（空格、句号等） ---
    else:
        # 不做处理，直接拼接到结果中
        decrypted_str += char

# 4. 输出解密后的句子
print(decrypted_str)


# 1. 获取输入
encrypted_str = input()

# 2. 定义字母表“字典”
# 我们把所有小写和大写字母按顺序写好
# 这样每个字母在字符串里的索引（下标）就代表了它的顺序
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 3. 初始化结果
decrypted_str = ""

# 4. 遍历字符串中的每一个字符
for char in encrypted_str:
    
    # --- 情况1：如果是小写字母 ---
    if char in lower_case:
        # (1) 找到当前字符在字母表中的位置（下标 0-25）
        # .find() 方法会返回字符在字符串中的索引
        old_index = lower_case.find(char)
        
        # (2) 计算解密后的新位置
        # 往前推 3 位，同样使用 % 26 来处理“绕圈”的问题
        # Python 的 % 运算对负数非常友好：
        # 比如 'a' 是索引 0，(0 - 3) % 26 = -3 % 26 = 23 (对应 'x')
        new_index = (old_index - 3) % 26
        
        # (3) 从字母表中取出新字符拼接到结果里
        decrypted_str += lower_case[new_index]
        
    # --- 情况2：如果是大写字母 ---
    elif char in upper_case:
        # 逻辑完全一样，只是去大写字母表里查
        old_index = upper_case.find(char)
        new_index = (old_index - 3) % 26
        decrypted_str += upper_case[new_index]
        
    # --- 情况3：其他符号（空格、句点等） ---
    else:
        # 直接保留原样
        decrypted_str += char

# 5. 输出结果
print(decrypted_str)

Question G
"""

# 1. 获取输入 N
N = int(input())

# 2. 遍历大于 2 但不超过 N 的所有数字
# 题目要求 "大于 2"，所以从 3 开始
# "不超过 N"，所以 range 要写到 N + 1
for num in range(3, N + 1):
    
    # 备份当前数字，用于后续的计算，不破坏原本的循环变量 num
    temp = num
    
    # 3. 开始重复计算平方和 (While 循环)
    # 终止条件：变成 1 (快乐)，或者变成 4, 16, 37 (不快乐)
    while temp != 1 and temp != 4 and temp != 16 and temp != 37:
        
        # --- 计算各位数字的平方和 ---
        sum_sq = 0
        # 将数字转成字符串，方便遍历每一位
        # 例如：temp = 130 -> '1', '3', '0'
        for digit_char in str(temp):
            d = int(digit_char)
            sum_sq += d * d  # 累加平方
            
        # 更新 temp，进入下一轮判断
        temp = sum_sq
        
    # 4. 循环结束后，判断是因为什么停下来的
    # 如果是因为变成 1 停下来的，说明它是快乐数
    if temp == 1:
        print(num)