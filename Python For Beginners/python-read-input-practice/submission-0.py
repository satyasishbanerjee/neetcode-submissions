def add_two_numbers() -> int:
    a = input()
    a = a.split(",")
    for i in range(2):
        a[i] = int(a[i])
    return sum(a)


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
