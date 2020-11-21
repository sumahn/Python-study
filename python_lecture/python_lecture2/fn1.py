def fn():
    print("fn called")

fn()

def exp(x):
    return x ** 2
 
print(exp(3))

def get_fruits():
    return ['오렌지','사과','바나나']

print(get_fruits()[1])

def get_name():
    return 'Kent', 'Back'

print(get_name())

def full_name(first_name, last_name):
    return first_name + ' ' + last_name 

name = get_name()
print(name, full_name('Steve', 'Cha'))

def var_param(a, *vp):
    print(type(vp))
    print(a, len(vp), vp[len(vp)-1])

var_param('AA', 'bbb','ccc')


# 두 수를 받아, 사칙연산(+,-,*,/)을 수행하는 함수를 만들어 보시오.

def my_calc():
    exp = input('수식을 입력하세요(usage: 2 + 3)> ')
    
    # 1. 양 쪽에 띄어쓰기가 있다면 제거
    exp = exp.strip(' ')

    # 2. 가운데 수식 기호가 무엇인지 확인
    if ' ' in exp:
        exp = exp.replace(' ', '')
        
    for e in exp:
        if e.isdigit() == False:
            sym = e
        
    
    exp = exp.split(sym)
            
    # 3. 수식 기호에 따라 계산 시작
    if sym == '+':
        ans = float(exp[0]) + float(exp[-1])
        
    elif sym == '-':
        ans = float(exp[0]) - float(exp[-1])
        
    elif sym == '*':
        ans = float(exp[0]) * float(exp[-1])
        
    elif sym == '/':
        if float(exp[-1]) == 0:
            print("나눌 수 없는 인자입니다.")
            exit()
        
        else:
            ans = float(exp[0]) / float(exp[-1])
    
    else:
        print("인식할 수 없는 수식입니다.")
    
    # 만약 ans가 정수라면 정수로 변환
    if ans.is_integer():
        ans = int(ans)

    print('Answer is', ans)
    



# Recursive Function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

factorial(4)

