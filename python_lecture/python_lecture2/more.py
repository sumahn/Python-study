cmd = input("Input(usage: 이름, 나이, 성별)>>> ")
print("aaaa=" + cmd + ".")

error_msg = "정확히 입력해 주세요!"

# 1. 값이 존재여부 체크
if cmd == '':
    print(error_msg)
    exit()

# 2. , 가 있는지 체크
if cmd.find(',') == -1:
    print(error_msg)
    exit()

ifExistsComma = False
for i in cmd:
    if i == ',':
        ifExistsComma = True
        break

if ifExistsComma == False:
    print(error_msg)
    exit()
    

cmds = cmd.split(',')

# 3. 3개의 값이 있는지 체크
