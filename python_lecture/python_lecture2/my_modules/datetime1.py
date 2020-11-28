import datetime
import locale

print(locale.getlocale())
locale.setlocale(locale.LC_ALL, '')
print(locale.getlocale())

now = datetime.datetime.now()
now.strftime("%Y-%m-%d %H:%M:%S")
print(now.strftime("%Y{} %m{} %d{} %H{} %M{}".format(*"년월일시분")))