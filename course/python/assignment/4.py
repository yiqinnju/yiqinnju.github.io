# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 09:44:34 2025

@author: borak

Question A:
    
import math  # 导入math模块，以便使用 sqrt (开平方) 函数

# 1. 获取输入
# input().split() 将输入的一行字符串按空格分割成列表
# map(int, ...) 将分割后的字符串转换为整数
a, b, c = map(int, input().split())

# 2. 计算判别式 delta (b^2 - 4ac)
delta = b**2 - 4 * a * c

# 3. 计算两个根
# 使用求根公式：x = (-b ± √delta) / 2a
# math.sqrt(delta) 用于计算 delta 的平方根
root1 = (-b + math.sqrt(delta)) / (2 * a)
root2 = (-b - math.sqrt(delta)) / (2 * a)

# 4. 排序
# 题目要求从小到大输出，无论 a 是正还是负，
# 我们都可以直接使用 min() 和 max() 找出较小值和较大值
small_root = min(root1, root2)
large_root = max(root1, root2)

# 5. 输出结果
# 题目要求使用 round 函数保留一位小数
print(round(small_root, 1))
print(round(large_root, 1))

Question B:

# 1. 获取输入
# 输入是一个正整数 n
n = int(input())

# 2. 初始化计数器
# 用于记录一共进行了多少轮变化
rounds = 0

# 3. 开始循环
# 只要棋子数量 n 不等于 1，就继续进行游戏
while n != 1:
    rounds += 1  # 每一轮开始，轮数加 1
    
    # 判断当前 n 是奇数还是偶数
    if n % 2 == 0:
        # 如果是偶数，数量减半
        # 使用 // 进行整除，保证结果是整数（例如 4 // 2 = 2，而不是 2.0）
        n = n // 2
    else:
        # 如果是奇数，数量加 1
        n = n + 1
    
    # 题目要求输出“每轮改变后的棋子数”
    # 我们在每次变化后立即打印当前的 n
    print(f"当前棋子数: {n}")

# 4. 循环结束后，输出总轮数
print(f"总轮数: {rounds}")   

Question C:

# 1. 定义字典
# 使用字典结构存储数据，格式为 {姓名: QQ号}
# 注意：这里将QQ号存为字符串（引号包裹），方便后续使用 len() 判断长度
qq_data = {
    "xiaoyun": "88888",
    "xiaohong": "5555555",
    "xiaoteng": "11111",
    "xiaoyi": "1234321",
    "xiaoyang": "1212121"
}

# 2. 第一部分：查询功能
# 使用 while True 开启一个无限循环，直到用户输入正确的名字才停止
while True:
    # 提示用户输入
    name = input("Please input the name:")
    
    # 检查输入的名字是否在字典的键（Key）中
    if name in qq_data:
        # 如果存在，输出对应的QQ号
        print(qq_data[name])
        # 任务完成，使用 break 跳出循环
        break
    else:
        # 如果不存在，提示错误，循环会继续，让用户重新输入
        print("Not found, please try again.")

# 3. 第二部分：寻找靓号
print("Who has the nice number?")

# 创建一个空列表，用来暂存拥有靓号的大佬名字
nice_number_owners = []

# 遍历字典中的每一项
# .items() 方法可以同时获取键(k)和值(v)
for name, qq in qq_data.items():
    # 判断QQ号长度是否小于等于5
    if len(qq) <= 5:
        nice_number_owners.append(name)

# 4. 排序与输出
# 题目要求按 ASCII 码顺序输出
# 对于英文字符串，默认的 sort() 方法就是按照 ASCII (字典序) 排序的
nice_number_owners.sort()

# 遍历排好序的列表，依次输出名字
for name in nice_number_owners:
    print(name)


Question D

# 1. 获取输入
# 训练集坐标字符串，如 "(1,1),(9,4),(8,7)"
train_points_input = input()
# 训练集类别，如 "1,2,3"，用逗号分割成列表
train_labels = input().split(',')
# 测试样本坐标，如 "(2,2)"
test_point_input = input()

# 2. 解析测试样本坐标
# 去掉括号 "(2,2)" -> "2,2"
test_str = test_point_input.strip('()')
# 分割并转换为整数 -> x=2, y=2
test_coords = test_str.split(',')
test_x = int(test_coords[0])
test_y = int(test_coords[1])

# 3. 解析训练集坐标
# 这是一个难点。输入的格式是 (x1,y1),(x2,y2)
# 我们可以先处理一下字符串，把 "),(" 替换成一个特殊符号，比如 "|"
# 这样字符串就变成了 "(1,1|9,4|8,7)"
# 然后再去头去尾的括号，最后用 "|" 分割
temp_str = train_points_input.replace("),(", "|")
temp_str = temp_str.replace("(", "").replace(")", "")
# 分割后得到列表: ['1,1', '9,4', '8,7']
train_points_list = temp_str.split('|')

# 4. 初始化最小距离和预测类别
# 将最小距离初始化为一个无限大的数，确保第一个计算出的距离一定比它小
min_distance = float('inf') 
predicted_label = None

# 5. 遍历每一个训练样本，计算距离
# 使用 range(len(...)) 同时获取索引 i，以便找到对应的标签
for i in range(len(train_points_list)):
    # 获取当前训练点的坐标字符串，如 "1,1"
    p_str = train_points_list[i]
    p_coords = p_str.split(',')
    train_x = int(p_coords[0])
    train_y = int(p_coords[1])
    
    # 计算曼哈顿距离: |x1 - x2| + |y1 - y2|
    dist = abs(train_x - test_x) + abs(train_y - test_y)
    
    # 6. 比较并更新最近邻
    # 注意：题目要求“如果有多个最近，输出最靠前的”
    # 因此这里必须使用 < (小于)，不能用 <=
    # 只有当新距离 *严格小于* 当前最小距离时，才更新
    if dist < min_distance:
        min_distance = dist
        # 从对应的标签列表中取出类别
        predicted_label = train_labels[i]

# 7. 输出结果
print(predicted_label)


Question E_recursive

# 递归函数：计算兑换方法数
# money: 当前还需要凑的金额
# max_coin: 当前允许使用的最大面额硬币
def count_ways(money, max_coin):
    # 【终止条件1】：如果金额刚好减到0，说明找到了一种成功的换法
    if money == 0:
        return 1
    
    # 【终止条件2】：如果金额小于0，说明这种拆分方式无效
    if money < 0:
        return 0
    
    # 【终止条件3】：如果最大面额已经降到1元
    # 无论剩多少钱，都只能用1元硬币一个个凑，所以只有一种换法
    if max_coin == 1:
        return 1
    
    # 【递归核心逻辑】
    # 我们可以把情况分为两类：
    # 1. 至少使用一个当前的 max_coin。
    #    于是钱数减少了，我们继续递归调用自己。
    use_current = count_ways(money - max_coin, max_coin)
    
    # 2. 完全不使用当前的 max_coin（觉得它太大了，或者想换换口味）。
    #    钱数没变，但是最大面额降级（除以2）。
    skip_current = count_ways(money, max_coin // 2)
    
    # 两种情况的总和就是答案
    return use_current + skip_current

# --- 主程序开始 ---

# 1. 获取输入
n = int(input())

# 2. 寻找初始的最大面额硬币
# 题目要求硬币必须是 2 的次幂 (1, 2, 4, 8...)
# 我们需要找到一个最大的、但不超过 n 的 2 的次幂
start_coin = 1
while start_coin * 2 <= n:
    start_coin = start_coin * 2

# 3. 调用递归函数并输出结果
result = count_ways(n, start_coin)
print(result)

Question E_dynamic programming


# 1. 获取输入
n = int(input())

# 2. 准备硬币列表
# 我们需要找出所有小于等于 n 的 2 的次幂 (1, 2, 4, 8...)
coins = []
val = 1
while val <= n:
    coins.append(val)
    val *= 2
# 例如 n=5 时，coins 列表为 [1, 2, 4]

# 3. 初始化“方法数表格”
# ways[i] 代表凑出金额 i 的方法数量
# 列表长度为 n+1 (下标从 0 到 n)
ways = [0] * (n + 1)

# 基础情况：凑出金额 0 只有 1 种方法（就是什么都不给）
ways[0] = 1

# 4. 开始循环（核心逻辑）
# 外层循环：依次拿出一种硬币
for coin in coins:
    # 内层循环：更新从 coin 到 n 的每一个金额
    # 含义是：对于金额 i，如果我们要用这就这枚新硬币，
    # 那么方法数就等于“不包含这枚硬币时的方法数”加上“减去这枚硬币面值后的方法数”
    for i in range(coin, n + 1):
        ways[i] = ways[i] + ways[i - coin]

# 5. 输出结果
# 表格的最后一个数字，就是凑出金额 n 的总方法数
print(ways[n])

Question E_brutal force

# 1. 获取输入
n = int(input())

# 2. 寻找初始的最大面额硬币 (同上题)
start_coin = 1
while start_coin * 2 <= n:
    start_coin = start_coin * 2

# 3. 初始化变量
total_ways = 0

# 【待办清单】 (模拟栈 Stack)
# 每个元素是一个列表：[剩余金额, 当前最大硬币]
# 初始任务：用 start_coin 来凑 n
todo_stack = [[n, start_coin]]

# 4. 开始暴力循环
# 只要清单不为空，就一直干活
while len(todo_stack) > 0:
    # 取出最后一个任务 (pop)
    current_task = todo_stack.pop()
    
    rem_money = current_task[0]  # 剩余金额
    max_coin = current_task[1]   # 当前允许的最大面额
    
    # --- 判断是否到达终点 ---
    
    # 情况1：如果金额刚好减到0，说明找到了一种方案
    if rem_money == 0:
        total_ways += 1
        continue # 结束当前任务，进行下一个
        
    # 情况2：如果只能用1元硬币了
    # 无论剩多少钱，都只能全部用1元来填，这算1种方案
    if max_coin == 1:
        total_ways += 1
        continue
    
    # --- 如果没到终点，就拆解成两个新任务 ---
    
    # 任务A：【不使用】当前面额的硬币
    # 钱数不变，但是硬币面额降级 (比如从4元降到2元)
    # 我们先添加这个任务
    todo_stack.append([rem_money, max_coin // 2])
    
    # 任务B：【使用】一个当前面额的硬币
    # 只有当 剩余金额 >= 当前面额 时才能用
    if rem_money >= max_coin:
        # 钱数减少，硬币面额保持不变（因为下次还可以继续用它）
        todo_stack.append([rem_money - max_coin, max_coin])

# 5. 输出结果
print(total_ways)

Question_F

import math

# --- 第一步：定义判断素数的函数 ---
def is_prime(num):

    #判断一个整数 num 是否为素数 如果是素数返回 True，否则返回 False

    # 1. 处理特殊情况：小于2的数不是素数
    if num < 2:
        return False
    
    # 2. 循环判断是否有因子
    # 只需要判断到 num 的平方根即可，这样效率更高
    # int(math.sqrt(num)) + 1 确保取整后能覆盖到平方根
    limit = int(math.sqrt(num)) + 1
    
    for i in range(2, limit):
        # 如果能被 i 整除，说明不是素数
        if num % i == 0:
            return False
            
    # 如果循环走完都没有返回 False，说明它是素数
    return True

# --- 第二步：主程序逻辑 ---

# 获取输入 N
N = int(input())

# 初始化计数器
count = 0

# 遍历从 2 到 N 的所有整数 (包括 N)
for i in range(2, N + 1):
    
    # 1. 首先判断数字本身是不是素数
    if is_prime(i):
        
        # 2. 计算逆序数
        # 方法：转成字符串 -> 逆序切片 -> 转回整数
        # 例如：13 -> "13" -> "31" -> 31
        reversed_str = str(i)[::-1]
        reversed_num = int(reversed_str)
        
        # 3. 判断逆序数是不是素数
        if is_prime(reversed_num):
            # 如果两个条件都满足，计数器加 1
            count += 1

# 输出结果
print(count)

Question G

# 1. 获取输入
# 题目描述输入是一个列表，例如 [0, 0, 1]
# 在 Python OJ 中，如果输入格式形如 "[0, 0, 1]"，通常使用 eval() 来解析最直接
f = eval(input())

# 获取程序员的总人数
n = len(f)

# 2. 遍历每一个程序员，找出他的“代码源头”
for i in range(n):
    # 这里的 i 代表当前我们正在调查的程序员编号
    # current_source 代表他目前的上家
    current_source = f[i]
    
    # 3. 开始顺藤摸瓜 (While 循环)
    # 条件：如果 current_source 抄袭的对象不是他自己
    # (也就是说 f[current_source] != current_source)
    # 那么说明他也是抄的，我们需要继续往上找
    while f[current_source] != current_source:
        # 将当前上家更新为“上家的上家”
        current_source = f[current_source]
    
    # 4. 找到源头后，更新列表
    # 当循环结束时，current_source 就是那个没有抄袭别人的人（源头）
    # 我们直接把程序员 i 的抄袭对象修改为这个源头
    f[i] = current_source

# 5. 输出结果
print(f)

Question H

import math

# --- 第一步：定义计算因子之和的函数 ---
def get_factor_sum(num):
    
    #计算一个数 num 的所有真因子（包括1，不包括它自己）之和
    
    # 1是所有正整数的因子，先加上
    total = 1
    
    # 从2遍历到 num的平方根
    # 比如计算 100 的因子，只需要遍历到 10
    limit = int(math.sqrt(num)) + 1
    
    for i in range(2, limit):
        # 如果能整除，说明 i 是因子
        if num % i == 0:
            total += i
            # 找到一个因子 i，通常对应另一个因子 num // i
            # 例如 100能被2整除，得50。2和50都是因子。
            # 需要排除 i * i = num 的情况（比如 10*10=100，10只加一次）
            if i != num // i:
                total += num // i
                
    return total

# --- 第二步：主程序逻辑 ---

# 获取输入 n
n = int(input())

# 遍历每一个数 A，范围从 2 到 n
for A in range(2, n + 1):
    
    # 1. 计算 A 的因子和，假设这个和是 B
    B = get_factor_sum(A)
    
    # 2. 判断是否满足特殊数条件
    # 这里加一个条件 B > A，是为了：
    # (1) 避免重复输出：比如 A=220时找到了B=284；等循环到 A=284时，不要再输出一次 284,220
    # (2) 避免自身是特殊数：题目要求“两个不同的整数”，所以 A != B
    # (3) 确保 B 也在 n 的范围内 (题目通常隐含要求都在n以内)
    if B > A and B <= n:
        
        # 3. 验证 B 的因子和是否等于 A
        if get_factor_sum(B) == A:
            # 如果这一步也满足，说明互为特殊数
            print(f"{A},{B}")
            
Question I

# 1. 获取输入 n
n = int(input())

# 2. 初始化一个 n x n 的二维列表（矩阵）
# 先全部填上 0，表示这些格子还没被填过
# 注意：这里使用了列表推导式，生成了一个 n 行 n 列的矩阵
matrix = [[0] * n for _ in range(n)]

# 3. 定义方向控制
# 顺序是：右(0,1) -> 下(1,0) -> 左(0,-1) -> 上(-1,0)
# dr 表示行(row)的变化，dc 表示列(col)的变化
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 初始化位置和方向
row, col = 0, 0  # 从左上角 (0,0) 开始
dir_index = 0    # 初始方向是“右”，对应 dr[0], dc[0]

# 4. 循环填入数字 1 到 n*n
for num in range(1, n * n + 1):
    # 在当前位置填入数字
    matrix[row][col] = num
    
    # 5. 计算下一步的坐标
    next_row = row + dr[dir_index]
    next_col = col + dc[dir_index]
    
    # 6. 判断是否需要“拐弯”
    # 拐弯条件：
    # (1) 超出边界 (next_row 或 next_col < 0 或 >= n)
    # (2) 下一步的位置已经被填过了 (不等于 0)
    if not (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0):
        # 如果走不通，就顺时针旋转方向
        # (0->1, 1->2, 2->3, 3->0)
        dir_index = (dir_index + 1) % 4
        
        # 换了方向后，重新计算下一步坐标
        next_row = row + dr[dir_index]
        next_col = col + dc[dir_index]
    
    # 更新当前坐标，准备填下一个数
    row, col = next_row, next_col

# 7. 输出结果
for row_list in matrix:
    # 使用 * 号解包列表，打印出以空格分隔的数字
    print(*row_list)
    
Question J
"""
  
# 1. 获取输入
n = int(input())

# 2. 初始化丑数列表
# 题目规定 1 是第一个丑数
ugly_numbers = [1]

# 3. 初始化三个指针
# p2, p3, p5 分别指向“下一个有资格乘以 2、3、5 的丑数在列表中的下标”
# 一开始都指向第一个数（也就是 1）
p2 = 0
p3 = 0
p5 = 0

# 4. 循环生成，直到列表长度达到 n
while len(ugly_numbers) < n:
    # 计算三个候选值
    # 也就是当前指针指向的丑数，分别乘以 2, 3, 5
    val2 = ugly_numbers[p2] * 2
    val3 = ugly_numbers[p3] * 3
    val5 = ugly_numbers[p5] * 5
    
    # 5. 选出最小的一个作为下一个丑数
    # 这样能保证丑数列表是从小到大排列的
    next_val = min(val2, val3, val5)
    ugly_numbers.append(next_val)
    
    # 6. 移动指针（关键步骤）
    # 谁计算出的结果被选中了，谁的指针就往后移一位
    # 注意：这里要用 if，不能用 elif，因为可能出现重复值
    # 例如：2*3=6 和 3*2=6，如果 next_val 是 6，那么 p2 和 p3 都要往后移
    if next_val == val2:
        p2 += 1
    if next_val == val3:
        p3 += 1
    if next_val == val5:
        p5 += 1

# 7. 输出第 n 个丑数
# 列表下标从 0 开始，所以第 n 个就是 list[n-1]，或者直接取最后一个 list[-1]
print(ugly_numbers[-1])    