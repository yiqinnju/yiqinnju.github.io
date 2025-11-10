def workA():
    # 统计指定单词出现的次数
    s = input().replace(",", "").replace(".", "")
    word = input()
    word_list = s.split(" ")
    print(word_list.count(word))

def workB():
    # 计算去掉最大值最小值后的平均数
    s = list(eval(input()))
    max_score, min_score = max(s), min(s)
    result = (sum(s) - max_score - min_score) / (len(s) - 2)
    print('{:.2f}'.format(result))

def workC():
    # 生成range对象
    print(list(range(1, 11)))
    print(list(range(2, 20, 2)))
    print(list(range(0, 55, 5)))
    print(list(range(10, 0, -1)))

def workD():
    monthdays = {
        'Jan': 31,
        'Feb': 28,
        'Mar': 31,
        'Apr': 30,
        'May': 31,
        'Jun': 30,
        'Jul': 31,
        'Aug': 31,
        'Sep': 30,
        'Oct': 31,
        'Thi': 40,
    }
    # 创建一个新的字典x = {'Nov':30,'Dec':31}，并将其包含的键值对追加到字典monthdays里
    x = {'Nov': 30, 'Dec': 31}
    monthdays.update(x)
    # 删除键为’Thi’的键值对
    del monthdays['Thi']
    # 按照ASCII码顺序，输出字典monthdays的键序列。
    print(sorted(monthdays.keys()))
    # 按大小排序显示字典monthdays的值序列。（从小到大）
    print(sorted(monthdays.values()))
    # 按照字典的键排序，显示字典monthdays的键值对序列。
    print(sorted(monthdays.items()))
    # 获取键‘Mar'对应的值。
    print(monthdays['Mar'])
    # 获取键’Abc'对应的值，没有则显示'No Found!'。
    print(monthdays.get('Abc', 'No Found!'))
    # 修改键‘Feb'的值为29，并输出该值。
    monthdays['Feb'] = 29
    print(monthdays['Feb'])

def workE():
    # 集合操作
    listA = ['red','blue','yellow','green','white','black']
    listB = ['green','purple','yellow','pink']
    setA, setB = set(listA), set(listB)
    print(sorted(setA.union(setB)))
    print(sorted(setA.difference(setB)))
    print(sorted(setB.difference(setA)))
    print(sorted(setA.intersection(setB)))
    print(sorted(setA.symmetric_difference(setB)))

def workF():
    number = eval(input())
    if number >= 90:
        print("A")
    elif number >= 80:
        print("B")
    elif number >= 70:
        print("C")
    elif number >= 60:
        print("D")
    else:
        print("F")

def workG():
    # 判断两个数是否互质
    numberA, numberB = eval(input()), eval(input())
    is_co_prime = True
    for num in range(2, numberA + 1):
        if numberA % num == 0 and numberB % num == 0:
            is_co_prime = False
            break
    if is_co_prime:
        print("{0} and {1} are coprime".format(numberA, numberB))
    else:
        print("{0} and {1} are not coprime".format(numberA, numberB))

def workH():
    # 计算BMI
    numbers = input().split(" ")
    weight, height = eval(numbers[0]), eval(numbers[1])
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            print("slim")
        elif bmi < 23.9:
            print("normal")
        else:
            print("fat")
    else:
        print("Invalid")

if __name__ == "__main__":
    workH()
    # workF()

