"""
print("第一题\n")

x = input("请输入两个数，以空格相隔： ").split()

a = int(x[0])

b = int(x[1])

print(a+b, a-b, a*b, int(a/b), float(a/b), sep="\n")

print("第二题\n")

x = input("请输入一个九位数的长整数： ")

x = int(x)

a = int(x/1000000)

b = int((x - a*1000000)/1000)

c = x - a*1000000 - b* 1000

print(a,b,c,sep="\n")



print("第三题\n")

x = int(input("请输入一个分钟数： "))

min = x%60

x = (x - min)/60

hour = int(x%24)

x = (x-hour)/24

day = int(x%365)

x = int((x-day)/365)


print(f'{x}years {day}days {hour}hours {min}mins')


print("第四题\n")

s = input("请输入水的质量、初始温度和终止温度，以空格分隔")

x = s.split()

e = float(x[0])*(float(x[2])-float(x[1]))*4184

print(e)


print("第五题\n")

s = input("请输入四位正整数")

r1 = int(s[3]+s[2]+s[1]+s[0])

s = int(s)

r2 = 1000*(s%10)+100*int(((s%100)/10))+10*int((s%1000)/100)+int(s/1000)

print(r1)

print(r2)



print("第六题\n")

x = float(input())

y = x**2 + 2*x-10

y = str(y)

temp = y.split('.')

dec = temp[1]

print(dec)


"""