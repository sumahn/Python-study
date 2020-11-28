g_x = 1000

def change_x():
    global g_x
    g_x = 300
    print("inner def>>>", g_x)

change_x()
print("outer def>>>", g_x)

