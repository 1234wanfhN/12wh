import string

while 1:
    #用户输入密码
    user_password = input("请输入新密码: ")
    #判断密码是否合格
    password_state = 0b00000

    for char in user_password:
        if char in string.ascii_uppercase:
            password_state |= 0b10000
        elif char in string.ascii_lowercase:
            password_state |= 0b01000
        elif char in string.digits:
            password_state |= 0b00100
        else:
            password_state |= 0b00010
    if len(user_password) >= 8:
        password_state |= 0b00001
    #输出
    if password_state == 0b11111:
        print('密码符合要求!')
        break
    else:
        prompt = '密码不符合要求,'
        if password_state & 0b00001 == 0:
            prompt = prompt + '长度不足八,'
        if password_state & 0b01000 == 0:
            prompt = prompt + '没有小写符号,'
        if password_state & 0b10000 == 0:
            prompt = prompt + '没有大写符号,'
        if password_state & 0b00100 == 0:
            prompt = prompt + '没有数字,'
        if password_state & 0b00010 == 0:
            prompt = prompt + '没有标点,'
        prompt = prompt[:-1]
        print(prompt)
