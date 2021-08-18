__version__ = "1.0.0"

__all__ = [

    'getPSMstr', 'getMoreStep', 'getOne','get_time','getRandomNum'

]

import random
import time
import re


def f1(s):
    '''
    搜索题中括号算式
    '''
    ss = re.search("\(\d+[\+\-\*/\d]+\)", s)
    if ss:
        return ss.group(0)


def f2(s):
    '''
    搜索题中乘除法算式
    '''
    ss = re.search("\d+[\*/]\d+", s)
    if ss:
        return ss.group(0)


def f3(s):
    '''
    搜索加减法算式
    '''
    ss = re.search("\d+[\+\-]\d+", s)
    if ss:
        return ss.group(0)


def f4(s):
    '''
    搜索加减法乘除算式
    '''
    ss = re.search("\d+[\+\-\*/\d]+", s)
    if ss:
        return ss.group(0)


def validator(s, result, carry, abdication):
    '''
    算式分解校验器
    '''

    if isResultOk(s, result):
        if f1(s):

            s = validator1(s, result, carry, abdication)

            if s:
                return validator2(s, result, carry, abdication)
            else:
                return False

        else:#校验无括号算式
            return validator2(s, result, carry, abdication)
    else:
        return False


def validator1(s, result, carry, abdication):
    '''
    算式分解校验器提取括号内算式，然后递归给validator2进行算式验证
    本方法可以递归提取括号嵌套算式
    '''
    while f1(s):
        fa = f1(s)
        fb = f4(f1(s))
        r = validator2(fb, result, carry, abdication)
        if r:
            s = s.replace(fa, "{}".format(int(float(r))))
        else:
            return False
    return s


def validator2(s, result, carry, abdication):
    '''
    分解乘除加减法计算结果并校验
    '''
    # 乘除法验证
    while f2(s):
        f = f2(s)
        if isMultDivOk(f, result):
            r = eval(f)
            s = s.replace(f, str(int(float(r))))
            # print(r,s)
        else:
            return False
    # 加减法验证
    while f3(s):
        f = f3(s)
        # print(f)
        if isAddSub(f, result, carry, abdication):
            r = eval(f)
            s = s.replace(f, str(r))
        else:
            return False

    return s


def isResultOk(str, result):
    '''
    验证算式结果是否正确
    '''
    try:
        # print('比较结果：',str)
        return result[0] <= eval(str) <= result[1]
    except(ZeroDivisionError):
        return False



def isMultDivOk(s, result):
    '''
    判断乘除法正确性
    '''
    if re.search("/", s):
        divs = re.split("/", s)
        if int(divs[1]) == 0:
            return False
        else:
            if isResultOk(s, result) and ((int(divs[0]) % int(divs[1])) == 0) and eval(s) > 0 : # 除法，除数不能为0，并且结果在范围内,并且整除无余数
                return True
            else:
                return False
    if re.search("\*", s):
        return isResultOk(s, result)  # 乘法结果在范围内


def isAddSub(s, result, carry, abdication):
    '''
    判断加减法正确性
    '''
    tmp = re.split("[\+\-]", s)
    if isResultOk(s, result):
        if re.search("\+", s):

            if carry == 1:
                return True
            elif carry == 2:
                return is_addcarry(int(tmp[0]), int(tmp[1]))
            elif carry == 3:
                # print("加法进位校验")
                return is_addnocarry(int(tmp[0]), int(tmp[1]))

        elif re.search("\-", s):
            # print("减法校验开始")
            if abdication == 1:
                return True
            elif abdication == 2:
                return is_abdication(int(tmp[0]), int(tmp[1]))
            elif abdication == 3:
                return is_noabdication(int(tmp[0]), int(tmp[1]))
        else:
            return False


def getOne(formulas, signum, result, carry, abdication, is_result):
    '''
    根据条件生成一道一步算式题
    '''
    return getMoreStep(formulas, result, [[signum], ], 1, carry, abdication, 0, is_result)


def getMoreStep(formulas, result, symbols, step, carry, abdication, is_bracket, is_result, ):
    f = getRandomNum(formulas, step)
    str = getPSMstr(f, symbols, step, is_bracket)
    if validator(str, result, carry, abdication):
        return getXStepstr(str, is_result)
    else:
        return False


def getPSMstr(formulas, symbols, step, is_bracket):
    '''
    生成算式题
    '''
    ss = ""
    sym = getRandomSymbols(symbols, step)
    for i in range(step):
        formulas.insert(i * 2 + 1, getSymbol(sym[i]))

    if is_bracket:
        k = getRandomBracket(step)  # 获得一个括号起始指针
        for i in range(2):

            if i == 0:
                formulas.insert(k + 4 * i, ('('))
            else:
                formulas.insert(k + 4 * i, (')'))

    for s in formulas:
        ss = ss + str(s)
    return ss


def getRandomBracket(step):
    '''
    返回一个括号起始随机数
    '''
    while True:
        k = random.randint(0, step * 2 + 1 - 3)  # 获得一个括号起始指针
        if not k % 2:
            return k


########2步算式相关判断设置##########


def getXStepstr(src, is_result):
    '''
    给定一组算式和其结果，根据条件生成求结果或是求算数项的题型
    '''
    if is_result == 0:
        return repSymStr(src) + "="
    elif is_result == 1:
        return getRandomItem(repSymStr(src) + "=" + str(int(eval(src))))
    else:
        raise Exception("is_result求结果，求算数项参数设置错误！")


def repSymStr(s):
    '''
    更换乘除法符号
    '''
    if re.search('\*', s):
        s = re.sub('\*', '×', s)
    if re.search('/', s):
        s = re.sub('/', '÷', s)
    return s


def getRandomItem(sr):
    '''
    把得到的算式转变成求算数项口算题
    '''
    p = re.compile('\d+')
    sc = p.findall(sr)
    i = random.randint(0, len(sc) - 2)  # -2防止替换结果
    sr = sr.replace(sc[i], "__", 1)
    return sr


def getSymbol(sym):
    '''
    获得运算符号，用来运算结果
    '''
    if sym == 1:
        return "+"
    elif sym == 2:
        return "-"
    elif sym == 3:
        return "*"
    elif sym == 4:
        return "/"


def getRandomSymbols(symbols, step):
    '''
    返回一组运算符号
    '''
    newList = []
    for i in range(step):
        index = random.randint(0, len(symbols[i]) - 1)
        newList.append(symbols[i][index])
    return newList


########加法相关判断设置##########


def is_addcarry(a, b, ):
    '''
    判断加法进位
    '''
    return (get_num(a) + get_num(b) > 10)


def is_addnocarry(a, b):
    '''
    判断加法无进位
    '''
    return not is_addcarry(a, b)


########减法相关判断设置##########


def is_abdication(a, b):
    '''
    判断减法退位
    '''
    if (get_num(a) < get_num(b)):
        return True
    else:
        return False


def is_noabdication(a, b):
    '''
    判断减法无退位
    '''
    return not is_abdication(a, b)


########乘法相关判断设置##########


def is_multcarry(a, b):
    '''
    判断乘法和乘法是否存在进位
    '''
    if (get_num(a) * get_num(b) < 10):
        return False
    else:
        return True


########除法相关判断设置##########


########其它相关判断设置##########


def is_int(num):
    '''
    判断一个数是否为整数
    '''
    return isinstance(num, int)


def get_num(number):
    '''
    返回一个整数的个位数
    '''
    value0 = number / 10
    value0 = int(value0)
    return number - value0 * 10


def getRandomNum(list, step):
    '''
    根据所给的数值范围，步数，返回合法的数值。
    '''
    newList = []
    for i in range(0, step + 1):
        newList.append(random.randint(list[i][0], list[i][1]))

    return newList

def get_time(func):
    '''定义一个程序运行时间计算装饰器无返回结果'''
    def wrapper(*args, **kwargs):
        start = time.time()  # 起始时间
        func(*args, **kwargs)  # 要执行的函数
        end = time.time()  # 结束时间
        print('程序运行时间:{:.2f}ms'.format((end - start) * 1000))
        return func
    return wrapper


def main():
    print(getMoreStep([[1, 55], [1, 99], [1, 99], [1, 9]], [1, 99], [[1, 3], [4], [4]], 2, 1, 1, 1, 0))

if __name__ == '__main__':
    main()
