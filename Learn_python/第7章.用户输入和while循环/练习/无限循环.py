prompt = '请输入一个数字:'
prompt += '\n输入quit也不会退出, 因为这是一个无线循环'
number = input(prompt)
action = 0
while action < 100:
    number = int(number)
    print(f"你输入的数字是{number}")
    action += number