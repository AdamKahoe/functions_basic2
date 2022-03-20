# 1 Countdown

def countdown5(num):
    output = []
    for i in range(num, -1, -1):
        output.append(i)
    return output

print(countdown5(5))


# 2 Print and Return

def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([1, 2]))


# 3 First Plus Length

def first_plus_length(list):
    print(list[0])
    return(len(list))
print(first_plus_length([1, 2, 3, 4, 5]))

# 4 Values greater than the second

def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = []
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))
    return newList
print(values_greater_than_second([5, 3, 4]))
print(values_greater_than_second([3]))

# 5 This Lenghth, That Value


def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))


