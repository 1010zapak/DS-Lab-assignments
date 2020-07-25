def sq(n):
    return n*n

def swap(a,b):
    return b,a

def factorial(n):       #for next function
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
def sum_of_series():
    n,sum=5,0
    for i in range(5,0,-1):
        sum += factorial(i)/i

    return int(sum)


def decimal_to_binary(n):
    a = str(bin(n))
    return a[2:]


def case_count(strin):
    upper,lower = 0,0
    for i in strin:
        if i.isupper()==True:
            upper += 1
        elif(i.islower()==True):
            lower +=1
    return upper,lower

def max_min(arr):
    arr = arr.sort()
    return arr,max(arr),min(arr)

def fibonacci(n):
    if n<2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def calculator():
    a = int(input("Enter a number for calculation"))
    b = int(input("Enter another number for calculation"))
    operator = input("ENter an operator")
    if operator=='+':
        return a+b
    elif operator=='-':
        return a-b
    elif operator=='*':
        return a*b
    elif operator=='/':
        return a/b

def linearsearch():
    arr = []
    n = int(input("Enter number of elements in an array"))
    for i in range(n):
        arr[i] = int(input("Enter element of array"))
    x = int(input("enter element to search"))
    for i in range(0,n):
        if arr[i]==x:
            print("Element found at index",i+1)


def decimal_to_hexadecimal(n):
    a = hex(n)
    return a[2:]

print(sq(9))
print(swap(3,4))
print(sum_of_series())
print(decimal_to_binary(6))
#print(max_min())
print(case_count('The quick Brow Fox'))
print(fibonacci(9))
#print(calculator())
#print(linearsearch())
print(decimal_to_hexadecimal(12))