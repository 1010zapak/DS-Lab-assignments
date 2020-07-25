def sum_of_natural_nos(n):
    return int((n*(n+1))/2)

def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact *= i
    return fact

def multiplication_table(n,m):
    for i in range(1,m+1):
        print(n,"x",i,"=",n*i)

def fibonacii(n):
    i_minus1,i_minus2 = 1,0
    if n==1:
        return i_minus1
    for i in range(n+1):
        fibo = i_minus1 + i_minus2
        i_minus1,i_minus2 = fibo,i_minus1
    return fibo

def no_of_digits(n):
    no_of_dig = 0
    while n:
        no_of_dig,n = no_of_dig+1, n//10
    return no_of_dig

def reverse_number(n):
    m = 0
    while n:
        m,n =  m*10 + n%10,n//10
    return m

def palindrome(n):
    if n==reverse_number(n):
        return ("No. is a palindrome")
    else:
        return  ("No. is not a palindrome")

def prime(n):
    for i in range(2,n//2):
        if n%i==0 :
            return (n,"is not a prime")

    return(n,"is a prime")

def rang_of_primes(n,m):
    prime_nos = []
    for i in range(n,m+1):
        if (i,"is a prime")==prime(i):
            prime_nos.append(i)
    return prime_nos

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

print(sum_of_natural_nos(5))
print(factorial(5))
print(multiplication_table(10,5))
print(fibonacii(5))
print(no_of_digits(139))
print(reverse_number(139))
print(palindrome(2567652))
print(prime(7))
print(rang_of_primes(12,17))
print(calculator())

