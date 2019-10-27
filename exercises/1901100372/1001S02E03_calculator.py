number_1 = input('请输入第一个整数：')
number_1 = int(number_1)
operator = input('请输入你想做的计算：比如+、-、*、//')
number_2 = input('请输入第二个整数：')
number_2 = int(number_2)
if operator == '+':
    print(number_1+number_2)
elif operator == '-':
    print(number_1-number_2)
elif operator == '*':
    print(number_1*number_2)
else:
    print(number_1/number_2)