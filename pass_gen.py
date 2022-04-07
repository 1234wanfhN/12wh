import string
import random

def evaluate_password(password,show_info=True):
    password_state = 0b00000
    result = False
    for char in password:
        if char.isupper():
            password_state |= 0b10000
        elif char.islower():
            password_state |= 0b01000
        elif char.isdigit():
            password_state |= 0b00100
        else:
            password_state |= 0b00010
    if len(password) >= 8:
        password_state |= 0b00001
    #输出
    if password_state == 0b11111:
        if show_info:
            print('密码符合要求!')
        result = True
    else:
        if show_info:
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

def generate_password():
    all_char__set=string.printable[:-6]
    all_char__set *= 9
    result = ' '.join(random.sample(all_char__set,k=9))
    return result

def create_password(pass_length,confuse=False):
    result = ''
    #先生成包含四类字符的前四位密码
    result += random.choice(string.ascii_uppercase)
    result += random.choice(string.ascii_lowercase)
    result += random.choice(string.digits)
    result += random.choice(string.punctuation)
    if confuse:
        result += 'Il'
        result += ''.join(random.sample(string.printable[:-6] * pass_length, pass_length - 6))
    else:
        result += ''.join(random.sample(string.printable[:-6]*pass_length,pass_length-4))
    #对生成密码进行随机打乱
    result = ''.join(random.sample(result,len(result)))
    return result

def main_userinput():
    while 1:
        user_password = input('请输入新密码!')
        if evaluate_password(user_password):
            break

def main_genpassword():
    while 1:
        user_password = generate_password()
        if evaluate_password(user_password,show_info=False):
            print(f"新生成密码为：{user_password}")
            break

def main():
    for i in range(1):
       print(f"新生成密码为:{create_password(9,True)}")

main()





