def main():
    my_list = ['a', [1, 2, 3], 'z']
    print(my_list[0])
    print(my_list[1])
    print(my_list[1][1])
    print()
    print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18][15])
    print()
    myList = list('xyzabc')
    print(myList)
    myList.sort()
    print(myList)
    print()
    from operator import itemgetter
    data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9], ['Aaron', 5], ['Bob', 4], ['Aaron', 11],
            ['Carrie', 9]]
    print(data)
    data.sort(key=itemgetter(1, 0))
    print(data)
    print()
    my_str = 'This is a test'
    string_elements = my_str.split()
    print(string_elements)
    reversed_elements = []
    for element in string_elements:
        reversed_elements.append(element[::-1])
    print(reversed_elements)
    new_str = 'SPACE'.join(reversed_elements)
    print(new_str)
    print()
    numbers = [10, 20, 30]
    things = numbers
    new_things = [10, 20, 30]
    print(things == numbers)
    print(things is numbers)
    print(new_things == numbers)
    print(new_things is numbers)
    print()
    print()
    scores = []
    score = int(input("Score: "))
    while (score > 0):
        scores.append(score)
        score = int(input("Score: "))
    print("Your highest score is ", max(scores))
    print()
    tup = 2, 3
    print(tup)
    print()
    x, y = 'a', 3.14159
    print(x)
    print(y)
    print()
    x, y
    print()
    myTuple = 1, 2
    print(myTuple)
    myTuple = (1,)
    print(myTuple)
    myTuple = 27,
    print(myTuple)
    print()
    print(myTuple[0])
    myTuple = 34
    print(myTuple)
    print()
    date_input = input("Enter DOB (d/m/y)")
    parts = date_input.split("/")
    print(date_input)
    print()
    myList = [5, 14, 21, 3, 8, 6, 18, 28, 12, 16]

    low, high = get_low_high(myList)

    print(low, type(low))

    z = get_low_high(myList)
    print(z, type(z))

    print()

    new_list = [p ** 2 for p in range(1,6)]

    print(new_list)

    print()

    arg_list = [1, 2, 3]
    my_function(arg_list)
    print(arg_list)

    print()

    box()

    print()

    box(length=80, width=30)

    print()

    my_list2 = [1, 2, 3]

    print(fn1(my_list2, 4))
    print(fn1(my_list2))
    print(fn1())
    print(fn1())
    print(fn1())
    print(fn1())

    print()

    my_func(1, 2.0)
    my_func(1, 2)
    my_func('a', 'b')

    print(my_func.__annotations__)

def get_low_high(values):
    return min(values), max(values)

def my_function(param_list):
    param_list[0] = 100
    print(param_list)

def box(height=10, width=10, length=10):
    print(height, width, length)

def fn1(arg1=[], arg2=27):
    arg1.append(arg2)
    return arg1

def my_func(param1 : int, param2 : float) -> None :
    print("Result is:", param1 + param2)


main()