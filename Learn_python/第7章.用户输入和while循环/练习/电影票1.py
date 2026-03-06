prompt = "你的孩子多少岁"
prompt += "\n 按quit退出"
while True:
    user_age = input(prompt)
    if user_age == 'quit':
        break
    else:
        user_age = int(user_age)
        if user_age < 3:
            print("你的孩子不需要买票")
        elif user_age >= 3 and user_age <12 :
            print("你的孩子需要收10美元")
        else:
            print("你的孩子需要收15美元")
