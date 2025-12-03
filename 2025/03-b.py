#!/usr/bin/env python3

# TEST_RESULT = 3121910778619
# REAL_RESULT = 167384358365132
result = 0


with open("./data/03-real.txt") as file:
    for line in file.readlines():
        line = line.strip()
        lres = ""
        li = 0
        for i in range(11, -1, -1):
            fn = fi = 0
            for idx, c in enumerate(line[li : len(line) - i]):
                n = int(c)
                if n > fn:
                    fn, fi = n, idx
                if n == 9:
                    break
            lres += str(fn)
            li += fi + 1
        result += int(lres)

print(result)
