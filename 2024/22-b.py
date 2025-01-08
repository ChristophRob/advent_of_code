#!/usr/bin/env python3

# TEST_RESULT = 23
# REAL_RESULT = 1501

secrets = []
with open("./data/22-real.txt") as file:
    for line in file.readlines():
        secrets.append(int(line.strip()))


def evolve(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret


BEST_SEQUENCES = {}

result = 0
for root_secret in secrets:
    secret = root_secret
    prices = [secret % 10]
    for i in range(2000):
        secret = evolve(secret)
        prices.append(secret % 10)
    result += secret
    price_changes = []
    for i, p in enumerate(prices):
        if i > 0:
            price_changes.append(p - prices[i - 1])
    sequences = {}
    for p in range(len(price_changes) - 1, 2, -1):
        key = f"{price_changes[p-3]},{price_changes[p-2]},{price_changes[p-1]},{price_changes[p]}"
        sequences[key] = prices[p + 1]
    for key, price in sequences.items():
        if key not in BEST_SEQUENCES:
            BEST_SEQUENCES[key] = 0
        BEST_SEQUENCES[key] += price

max_value = max(BEST_SEQUENCES.values())
for k, v in BEST_SEQUENCES.items():
    if v == max_value:
        print(v)
