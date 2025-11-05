# Non-recursive Fibonacci Function
def non_recu_fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a,b = 0,1
    for i in range(2, n+1):
        a,b = b, a+b
        print(b)
    return b

# recursive Fibonacci Function 
def recu_fib(n):
    if n <=0:
        return 0
    elif n ==1:
        return 1
    return recu_fib(n-1) + recu_fib(n-2)

# Time & Space complexity
def time_space_complexity():
    print("\nFor Non-recursive Fibonacci :")
    print("Time Complexity : O(n)")
    print("Space Complexity : O(1)")

    print("\nFor Recursive Fibonacci :")
    print("Time Complexity : O(2^n)")
    print("Space Complexity : O(n)")

# Example
n = int(input("\nEnter a number :"))
print(f"Non-recursive Fibonacci of {n} : {non_recu_fib(n)}")
print(f"Recursive Fibonacci of {n} : {recu_fib(n)}")

time_space_complexity()
