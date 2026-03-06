# 练习7.4:⽐萨配料 编写⼀个循环，提⽰⽤户输⼊⼀系列⽐萨配料，并在⽤户输⼊'quit'时结束循环。每当⽤户输⼊⼀种配料后，都打印⼀条消息，指出要在⽐萨中添加这种配料。
pizza_sheet = ['apple', 'origin', 'berries', 'bnanan']
prompt = "\n输入你想要的pizza_sheet:"
while True:
    print(prompt, pizza_sheet)
    user_sheet = input(prompt)

    if user_sheet == 'quit':
        break
    else:
        print(f"your need {user_sheet.title()}")