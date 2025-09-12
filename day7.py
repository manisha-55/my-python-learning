# What are Exceptions?
# An exception is an error that occurs during program execution.
# If not handled → program crashes.
# We handle exceptions using try-except.

####### 1. Multiple except blocks
# Use multiple excepts to handle different types of errors differently.
try:
    a=int(input("enter num: "))
    b=int(input("enter denominator: "))
    result=a/b
    print("results: ",result)
except ZeroDivisionError:
    print("cannot divided by 0")
except ValueError:
    print("enter valid numbers")

######## 2. else and finally with try
# else: runs if no exception occurs.
# finally: runs always, used for cleanup (closing files, releasing resources).
try:
    x=int(input("enter a no: "))
    print("square:",x*x)
except ValueError:
    print("invalid no")
else:
    print("no error")
finally:
    print("end of thr program")

######## 3. Raising Exceptions using raise
# Use raise when you want to manually throw an error.
x=int(input("enter a no: "))
if(x<0):
    raise ValueError("negative members not allowed0004")
else:
    print("num is positive")

######## 4. Creating User-Defined Exception Classes
# We can create custom exception types by inheriting from Exception.

class NegativeNoError(Exception):
    pass
try:
    n1=int(input("enter user num: "))
    if n1<0:
        raise NegativeNoError("Negative numbers are not allowed")
    print("Num is:",n1)
except NegativeNoError as e:
    print(e)
