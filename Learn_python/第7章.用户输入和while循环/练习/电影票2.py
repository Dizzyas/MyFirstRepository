prompt = "你的孩子多少岁?"
prompt += "\n按quit退出"

action = True
while action:
    user_age = input(prompt)
    if user_age == 'quit':
        action = False
    else:
        user_age = int(user_age)
        if user_age < 3:
            print('你的孩子观看免费')
        elif user_age < 12:
            print('你的孩子观看收10美元')
        elif user_age >= 12:
            print('你的孩子观看收15美元')