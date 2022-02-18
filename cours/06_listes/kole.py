l1=[1,2,3,4,5,6,7,8,9]
def khole(l):
    a = 0
    for i in range (len(l)):
        if l[i]% 2==0:
            a += 1
    return
b = khole(l1)
print(b)
