import sys
import os

print("SSSS>>", sys.path)
print("__file__==>", __file__)
print("dirname ==>", os.path.dirname(__file__))
print("abspath ==>", os.path.abspath(__file__))

dir_name = os.path.dirname(__file__)
a_path = os.path.abspath(dir_name)
print("a_path>>>", a_path)
up_dir = os.path.join(a_path, '..') # c:\ws\ ... 
print("BASE CAMP>>>",os.path.abspath(up_dir))
sys.path.append(up_dir)

print("++++++++++++++>>", sys.path)



from mysys import clear
clear()


print(sys.argv, len(sys.argv))


def print_sys_vars():
    for i in [sys.version, sys.copyright, sys.platform]:
        print("-->", i)

sa = sys.argv
if len(sa) < 2:
    sys.exit()

with open(sa[1], "r", encoding='utf-8') as file:
    for line in file:
        print(line.strip())
