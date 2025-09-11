# What are Exceptions?
# An exception is an error that occurs during program execution.
# If not handled → program crashes.
# We handle exceptions using try-except.

try:
    a=int(input("enter num: "))
    b=int(input("enter denominator: "))
    result=a/b
    print("results: ",result)
except ZeroDivisionError:
    print("cannot divided by 0")
except ValueError:
    print("enter valid numbers")