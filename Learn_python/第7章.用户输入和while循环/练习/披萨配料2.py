prompt = "这里有很多的披萨配料:]"
prompt += "\napple, origin, berries, bnana"
prompt += "\n按quit退出"
user_sheets = []
while True:
    user_sheet = input(prompt)
    if user_sheet == 'quit':
        break
    else:
        print(f"你需要{user_sheet.title()}")
        user_sheets.append(user_sheet)
        print(f"现在这里有:{user_sheets}.")