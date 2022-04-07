while 1:
    #用户输入密码
    user_password = input("请输入新密码: ")
    #判断密码是否合格
    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWER = 'abcdefghijklmnopqrstuvwxyz'
    DIGIT = '0123456789'


    have_upper = False
    have_lower = False
    have_digit = False
    have_punctuation = False

    for char in user_password:
        if char in UPPER:
            have_upper = True
        elif char in LOWER:
            have_lower = True
        elif char in DIGIT:
            have_digit = True
        else:
            have_punctuation = True
    have_enough_char = len(user_password) >= 8
    is_secure = (have_enough_char
                and have_upper
                and have_digit
                and have_lower
                and have_punctuation)
    #输出


    if is_secure:
        print('密码符合要求!')
        break
    else:
        prompt = '密码不符合要求,'
        if not have_enough_char:
            prompt = prompt + '长度不足八,'
        if not have_lower:
            prompt = prompt + '没有小写符号,'
        if not have_upper:
            prompt = prompt + '没有大写符号,'
        if not have_digit:
            prompt = prompt + '没有数字,'
        if not have_punctuation:
            prompt = prompt + '没有标点,'
        prompt = prompt[:-1]
        print(prompt)
