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
