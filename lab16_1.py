def check(*args):
    for char in args:
        if (type(char) != float and type(char) != int) or char<=0:
            return False
    return True

def triangle_ineq(func):
    def inner(a,b,c):
        if not check(a,b,c):
            return 'Error! Enter valid positive numbers.'
        if a+b <= c or b+c <= a or a+c <= b:
            return 'Error! The inequality of a triangle does not hold.'        
        return func(a,b,c)
    return inner

@triangle_ineq
def area_calculation(a, b, c):    
    p = (a+b+c) / 2
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    return round(area, 2)
       
print(area_calculation(3,4,5))

