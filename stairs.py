def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
def countways(s):
    return fib(s+1)
s=int(input("no.of.stair case"))
print("no of ways:-")
print(countways(s))