# def fun(a: int, b: int):
#     return a * b

# print(fun(2, 3))

# ---------------------------------------------------------
# l = [1, 2, 3 , 4]
# val = 10
# idx = 0

# while idx < len(l):
#     if l[idx] == val:
#         break
#     idx += 1
# else:
#     l.append(val)

# print(l)

# ---------------------------------------------------
import sys
import ctypes

def f(x,l=[]):
    print(hex(id(l)))
    # print(sys.getrefcount(l))
    print(ctypes.c_long.from_address(id(l))).value

    for i in range(x):
        l.append(i*i)
    print(l) 

f(2)
f(3,[3,2,1])
f(3)

