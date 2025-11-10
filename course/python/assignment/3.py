def workA():
    # 计算两个数组的最小距离
    # 先全部转为整数
    arr1, arr2 = list(map(int, input().split(' '))), list(map(int, input().split(' ')))
    min_distance = -1
    for num1 in arr1:
        for num2 in arr2:
            # 遍历数组，计算距离
            distance = abs(num1 - num2)
            if min_distance == -1 or distance < min_distance:
                min_distance = distance
    print(min_distance)

def workB():
    # 简易计算器
    a, b = input().split(',')
    num1, num2 = int(a), int(b)
    while True:
        op = input()
        if op == '1':
            print("{}+{}={}".format(num1, num2, num1 + num2))
        elif op == '2':
            print("{}-{}={}".format(num1, num2, num1 - num2))
        elif op == '3':
            print("{}*{}={}".format(num1, num2, num1 * num2))
        elif op == '4':
            print("{}//{}={}".format(num1, num2, num1 // num2))
        else:
            break

def is_prime(num):
    # 检查num是否是素数，辅助的工具函数，后面在任务C和任务D都有使用
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def workC():
    for i in range(4, 2002, 2):
        for j in range(2, i - 1):
            if is_prime(j) and is_prime(i - j):
                print("{}={}+{}".format(i,j, i-j))
                break

def is_valid_date(year, month, day):
    """检查日期是否有效"""
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    # 检查每个月的天数
    if month in [4, 6, 9, 11]:
        return day <= 30
    elif month == 2:
        # 检查闰年
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            return day <= 29
        else:
            return day <= 28
    else:
        return day <= 31

def find_prime_dates(year):
    """找出给定年份中所有八位数素数的日期"""
    for month in range(1, 13):
        # 遍历生成有效的日期
        max_day = 31
        if month in [4, 6, 9, 11]:
            max_day = 30
        elif month == 2:
            if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
                max_day = 29
            else:
                max_day = 28
        for day in range(1, max_day + 1):
            date = year * 10000 + month * 100 + day
            # 对有效日期，判断是否是素数
            if is_prime(date):
                print(date)

def workD():
    # 输入指定年份，输出该年份所有的8位日期中的素数
    year = input()
    find_prime_dates(int(year))

def workE():
    # 编写程序，将给定的字符串序列，按照字符ASCII码顺序从小到大排序后输出。
    input_str = input()
    sorted_str = sorted(input_str, key=lambda x: x)
    print("".join(sorted_str))

def workF():
    # 1. 读取输入并处理成整数列表
    # 输入格式为逗号隔开的字符串，先按逗号分割，再将每个元素转为整数
    input_str = input()
    score_list = list(map(int, input_str.split(',')))

    # 2. 初始化两个列表，分别存储不及格和甲等成绩
    fail_scores = []  # 不及格：成绩 < 60
    grade_a_scores = []  # 甲等：成绩 > 85（题目明确85分不算甲等）

    # 3. 遍历所有成绩，分类存入对应列表
    for score in score_list:
        if score < 60:
            fail_scores.append(score)
        elif score > 85:  # 题目说明有85分学生，且85分不算甲等
            grade_a_scores.append(score)

    # 4. 计算平均分（题目保证两类数据都存在，无需处理空列表）
    # 平均分 = 总分 / 人数
    fail_average = sum(fail_scores) / len(fail_scores)
    grade_a_average = sum(grade_a_scores) / len(grade_a_scores)

    # 5. 按要求保留两位小数输出，分行显示
    print("{:.2f}".format(fail_average))
    print("{:.2f}".format(grade_a_average))

def workG():
    # 读取输入并转换为列表
    nums = eval(input())

    # 选择排序

    # 外层循环：控制需要确定位置的元素数量（共n-1轮，n为列表长度）
    for i in range(len(nums) - 1):
        # 内层循环：找到从i到末尾的最大绝对值元素
        max_index = i  # 假设当前位置是最大绝对值元素的位置
        for j in range(i + 1, len(nums)):
            # 比较绝对值大小，更新最大绝对值元素的位置
            if abs(nums[j]) > abs(nums[max_index]):
                max_index = j
        # 将找到的最大绝对值元素交换到当前位置i
        nums[i], nums[max_index] = nums[max_index], nums[i]

    # 输出排序后的列表
    print(nums)

def workH():
    n = int(input())

    # 外层循环控制行数（共n行）
    for i in range(n):
        # 每行的空格数：第i行有i个空格（从0开始计数）
        spaces = ' ' * i
        # 每行的#数量：第i行有(2*(n-i) - 1)个#
        # 例如n=5时，第0行：2*5-1=9，第1行：2*4-1=7，以此类推
        hashes = '#' * (2 * (n - i) - 1)
        # 拼接空格和#并输出
        print(spaces + hashes)

def workI():
    n1, n2 = map(int, input().split())
    a_numbers = []

    for num in range(n1, n2 + 1):
        if num == 0:
            # 0的二进制是0，1的个数为0，0的个数为1，不满足条件
            continue
        count_1 = 0
        count_0 = 0
        temp = num  # 用临时变量保存当前数字，避免修改原数
        # 循环计算二进制中1和0的个数
        while temp > 0:
            remainder = temp % 2  # 取当前最低位（0或1）
            if remainder == 1:
                count_1 += 1
            else:
                count_0 += 1
            temp = temp // 2  # 移除最低位，继续处理更高位
        # 判断是否为A类数
        if count_1 > count_0:
            a_numbers.append(num)

    # 输出结果
    if a_numbers:
        for num in a_numbers:
            print(num)
    else:
        print("Not Found")

def workJ():
    def min_num(*args):
        # 把数字转成字符串
        nums = []
        for num in args:
            nums.append(str(num))  # 逐个添加到列表
        n = len(nums)

        # 用基础冒泡排序：两两比较，小的放前面
        for i in range(n):
            for j in range(i + 1, n):
                # 比较两种拼接方式的大小（比如"10"和"01"）
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    # 交换位置
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

        # 处理首位为0的情况：找第一个非0数字交换
        if nums[0] == '0':
            for k in range(1, n):
                if nums[k] != '0':
                    # 交换首位和第一个非0数字
                    temp = nums[0]
                    nums[0] = nums[k]
                    nums[k] = temp
                    break

        # 拼接结果（用基础循环拼接，不依赖join的话也可以这样写）
        result = ""
        for s in nums:
            result = result + s
        return result

    # 读取输入
    input_str = input()
    # 按逗号分割成字符串列表
    str_list = input_str.split(',')
    # 转成整数列表
    numbers = []
    for s in str_list:
        numbers.append(int(s))

    # 调用函数并输出
    print(min_num(*numbers))

if __name__ == "__main__":
    workE()
    pass