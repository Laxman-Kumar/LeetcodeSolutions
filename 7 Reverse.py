def reverse(x):
    if(x<0):
        a = "-"+str(abs(x))[::-1]
        return int(a)
    else:
        return int(str(x)[::-1])

print(reverse(123))
print(reverse(-123))
print(reverse(120))
        
