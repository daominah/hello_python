import random
from typing import List

default_len = 12
lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "_"
# symbols = "~!#^_+-"
all_chars = "".join([lowers, uppers, digits, symbols])


def gen_password(len=default_len):
    force_indices: List[int] = random.sample(range(len), 4)
    password = ["a"] * len
    for i, char_type in [(0, lowers), (1, uppers), (2, digits), (3, symbols)]:
        force_index = force_indices[i]
        password[force_index] = random.choice(char_type)
    for i in range(len):
        if i not in force_indices:
            password[i] = random.choice(all_chars)
    return "".join(password)


if __name__ == "__main__":
    for i in range(10):
        print(gen_password(12))

