import string

def evaluate_password(password):
    password_state = 0b00000
    result = False
    for char in password:
        if char in string.ascii_uppercase:
            password_state |= 0b10000
        elif char in string.ascii_lowercase:
            password_state |= 0b01000
        elif char in string.digits:
            password_state |= 0b00100
        else:
            password_state |= 0b00010
    if len(password) >= 8:
        password_state |= 0b00001
    #输出
    if password_state == 0b11111:
        print('密码符合要求!')
        result = True
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
    return result

def main():
    while 1:
        user_password = input("请输入新密码: ")
        if evaluate_password(user_password):
            break

main()



