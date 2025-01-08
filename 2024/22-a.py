#!/usr/bin/env python3

# TEST_RESULT = 37327623
# REAL_RESULT = 13185239446

secrets = []
with open("./data/22-real.txt") as file:
    for line in file.readlines():
        secrets.append(int(line.strip()))


def evolve(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret


result = 0
for root_secret in secrets:
    secret = root_secret
    for i in range(2000):
        secret = evolve(secret)
    result += secret

print(result)
