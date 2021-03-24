try:
    x = int("zero")
    print(10 / x)
except NameError:
    print("Value error")
except ValueError:
    print("Value error")

x = str(1.0)
print(x[0])
(x[-1]) = '2'
