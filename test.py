def calculater(x,y,op):
    if op=='+':
        return x+y
    elif op=='-':
        return x-y
    elif op=='*':
        return x*y
    elif op=='/':
        return x/y
    else:
        return "Invalid"
result=calculater(5,6,'()')
print(result)
