from typing import List

def read_integers() -> List[int]:
    user=input()
    user=user.split(",")
    for i in range(len(user)):
        user[i] = int(user[i])
    return user

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
