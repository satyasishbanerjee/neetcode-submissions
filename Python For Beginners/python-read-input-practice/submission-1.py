def add_two_numbers() -> int:
    b = 0
    a = input()
    a = a.split(",")
    for i in range(2):
        a[i] = int(a[i])
    # return sum(a)
    for elements in a:
        b += elements
    return b



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
